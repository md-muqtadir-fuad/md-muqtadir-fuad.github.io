import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const PUBLICATIONS_MD_PATH = path.resolve(rootDir, 'content/publications.md');
const INDEX_HTML_PATH = path.resolve(rootDir, 'index.html');

const SITE_URL = 'https://md-muqtadir-fuad.github.io/';
const OWNER_NAME = 'Md. Muqtadir Fuad';

const LIST_MARKERS = ['<!-- AUTO_GENERATED_PUBLICATIONS_START -->', '<!-- AUTO_GENERATED_PUBLICATIONS_END -->'];
const JSONLD_MARKERS = ['<!-- AUTO_GENERATED_PUBLICATIONS_JSONLD_START -->', '<!-- AUTO_GENERATED_PUBLICATIONS_JSONLD_END -->'];

const escapeHtml = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const plainText = s => s.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[*_`]/g, '').replace(/\s+/g, ' ').trim();

// Parse "## Group" / "### Title" / "- key: value" / abstract paragraphs
function parsePublications(markdown) {
  const text = markdown.replace(/<!--[\s\S]*?-->/g, '');
  const groups = [];
  let group = null;
  let entry = null;

  for (const line of text.split(/\r?\n/)) {
    const groupMatch = line.match(/^##\s+(.+?)\s*$/);
    const titleMatch = line.match(/^###\s+(.+?)\s*$/);
    const fieldMatch = line.match(/^-\s+(authors|venue|date|links):\s*(.*?)\s*$/i);

    if (groupMatch) {
      group = { name: groupMatch[1], entries: [] };
      groups.push(group);
      entry = null;
    } else if (titleMatch) {
      if (!group) {
        group = { name: 'Publications', entries: [] };
        groups.push(group);
      }
      entry = { title: titleMatch[1], authors: '', venue: '', date: '', links: [], abstract: [] };
      group.entries.push(entry);
    } else if (fieldMatch && entry && entry.abstract.length === 0) {
      const key = fieldMatch[1].toLowerCase();
      if (key === 'links') {
        entry.links = [...fieldMatch[2].matchAll(/\[([^\]]+)\]\(([^)\s]+)\)/g)].map(m => ({ label: m[1], url: m[2] }));
      } else {
        entry[key] = fieldMatch[2];
      }
    } else if (entry && line.trim()) {
      // Blank lines separate abstract paragraphs
      if (entry._newParagraph || entry.abstract.length === 0) entry.abstract.push(line.trim());
      else entry.abstract[entry.abstract.length - 1] += ` ${line.trim()}`;
      entry._newParagraph = false;
    } else if (entry && !line.trim() && entry.abstract.length > 0) {
      entry._newParagraph = true;
    }
  }
  return groups;
}

function renderList(groups) {
  const usedIds = new Set();
  const abstractId = title => {
    const base = 'abs-' + plainText(title).toLowerCase().replace(/[^a-z0-9\s-]/g, '').split(/\s+/).slice(0, 5).join('-');
    let id = base;
    for (let n = 2; usedIds.has(id); n++) id = `${base}-${n}`;
    usedIds.add(id);
    return id;
  };

  return groups.map(g => {
    const items = g.entries.map(e => {
      const id = abstractId(e.title);
      const links = e.links.map(l => `              <a href="${escapeHtml(l.url)}">${escapeHtml(l.label)}</a>`);
      if (e.abstract.length) links.push(`              <button class="abstract-toggle" data-abstract-id="${id}">Abstract</button>`);
      const lines = [
        '          <li>',
        `            <p class="pub-title">${marked.parseInline(e.title)}</p>`,
        e.authors && `            <p class="pub-authors">${marked.parseInline(e.authors)}</p>`,
        e.venue && `            <p class="pub-venue">${marked.parseInline(e.venue)}</p>`,
        links.length && `            <div class="pub-links">\n${links.join('\n')}\n            </div>`,
        e.abstract.length && `            <p id="${id}" class="pub-abstract hidden">${e.abstract.map(p => marked.parseInline(p)).join('<br><br>')}</p>`,
        '          </li>',
      ];
      return lines.filter(Boolean).join('\n');
    });
    return `        <h3 class="subsection-title">${escapeHtml(g.name)}</h3>\n        <ol class="pub-list">\n${items.join('\n')}\n        </ol>`;
  }).join('\n\n');
}

// Papers with a DOI become ScholarlyArticle structured data for search engines
function renderJsonLd(groups) {
  const articles = [];
  for (const e of groups.flatMap(g => g.entries)) {
    const doi = e.links.find(l => /^https?:\/\/(dx\.)?doi\.org\//.test(l.url));
    if (!doi) continue;
    const authorNames = plainText(e.authors.split('·')[0]).split(/\s*,\s*/).filter(Boolean);
    const year = (e.venue.match(/\b(19|20)\d{2}\b(?!.*\b(19|20)\d{2}\b)/) || [])[0];
    const article = {
      '@type': 'ScholarlyArticle',
      headline: plainText(e.title),
      author: authorNames.map(name => (name === OWNER_NAME ? { '@type': 'Person', name, url: SITE_URL } : { '@type': 'Person', name })),
      sameAs: doi.url,
      url: doi.url,
    };
    if (e.date || year) article.datePublished = e.date || year;
    if (e.venue) article.isPartOf = { '@type': 'PublicationIssue', name: plainText(e.venue).replace(/,\s*(19|20)\d{2}\s*$/, '') };
    articles.push(article);
  }
  const json = JSON.stringify({ '@context': 'https://schema.org', '@graph': articles }, null, 2).replace(/^/gm, '  ');
  return `  <script type="application/ld+json">\n${json}\n  </script>`;
}

function replaceBetween(html, [start, end], content) {
  const regex = new RegExp(`${start}[\\s\\S]*?${end}`);
  if (!regex.test(html)) return null;
  return html.replace(regex, () => `${start}\n${content}\n        ${end}`);
}

export function buildPublications() {
  if (!fs.existsSync(PUBLICATIONS_MD_PATH)) {
    console.warn('[build-publications] content/publications.md not found, skipping.');
    return;
  }

  const groups = parsePublications(fs.readFileSync(PUBLICATIONS_MD_PATH, 'utf-8'));
  let html = fs.readFileSync(INDEX_HTML_PATH, 'utf-8');

  const withList = replaceBetween(html, LIST_MARKERS, renderList(groups));
  const withJsonLd = withList && replaceBetween(withList, JSONLD_MARKERS, renderJsonLd(groups));
  if (!withJsonLd) {
    console.warn('[build-publications] Publication markers not found in index.html, skipping.');
    return;
  }

  if (withJsonLd !== html) fs.writeFileSync(INDEX_HTML_PATH, withJsonLd, 'utf-8');
  const count = groups.reduce((n, g) => n + g.entries.length, 0);
  console.log(`[build-publications] Rendered ${count} publication(s) in ${groups.length} group(s) into index.html`);
}

// Run directly if executed as CLI
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildPublications();
}
