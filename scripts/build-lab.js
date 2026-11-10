import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const LAB_HTML_PATH = path.resolve(rootDir, 'lab/lab.html');
const LAB_MD_PATH = path.resolve(rootDir, 'lab/lab.md');

const escapeHtml = (s = '') =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const inline = (s = '') => marked.parseInline(s);
const parseLinks = (s = '') =>
  [...s.matchAll(/\[([^\]]+)\]\(([^)\s]+)\)/g)].map((m) => ({ label: m[1], url: m[2] }));

// Split markdown into top-level sections by "# Heading"
function parseSections(markdown) {
  const clean = markdown.replace(/<!--[\s\S]*?-->/g, '');
  const sections = {};
  let currentTitle = '';
  let currentLines = [];

  for (const line of clean.split(/\r?\n/)) {
    const heading = line.match(/^#\s+(.+?)\s*$/);
    if (heading) {
      if (currentTitle) {
        sections[currentTitle.toLowerCase()] = currentLines;
      }
      currentTitle = heading[1].trim();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }
  if (currentTitle) {
    sections[currentTitle.toLowerCase()] = currentLines;
  }
  return sections;
}

// Parse "### Title" with optional "- key: val" fields and free-text body
function parseEntries(lines) {
  const entries = [];
  let entry = null;

  for (const line of lines) {
    const title = line.match(/^###\s+(.+?)\s*$/);
    const field = line.match(/^-\s+([a-zA-Z0-9_-]+):\s*(.*?)\s*$/);

    if (title) {
      entry = { title: title[1].trim(), fields: {}, description: '' };
      entries.push(entry);
    } else if (entry && field && !entry.description) {
      entry.fields[field[1].toLowerCase()] = field[2].trim();
    } else if (entry && line.trim()) {
      entry.description += (entry.description ? ' ' : '') + line.trim();
    }
  }
  return entries;
}

function renderManifesto(lines) {
  const rawText = lines.join('\n').trim();
  const paragraphs = rawText
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean);

  if (paragraphs.length === 0) return '';

  const [first, ...rest] = paragraphs;
  const parts = [`        <p>\n          ${inline(first)}\n        </p>`];

  for (const p of rest) {
    parts.push(
      `        <p style="margin-top: 1rem; color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">\n          ${inline(p)}\n        </p>`
    );
  }
  return parts.join('\n');
}

function renderProjects(lines) {
  const entries = parseEntries(lines);
  return entries
    .map((e, idx) => {
      const numStr = String(idx + 1).padStart(2, '0');
      let linkLabel = 'Project Notes';
      let linkUrl = '#';

      if (e.fields.link) {
        // e.g. "Project Notes (#)" or "[Project Notes](url)" or "Project Notes"
        const mdLink = e.fields.link.match(/\[([^\]]+)\]\(([^)]+)\)/);
        const parenLink = e.fields.link.match(/^(.+?)\s*\(([^)]+)\)$/);
        if (mdLink) {
          linkLabel = mdLink[1];
          linkUrl = mdLink[2];
        } else if (parenLink) {
          linkLabel = parenLink[1];
          linkUrl = parenLink[2];
        } else {
          linkLabel = e.fields.link;
        }
      }

      const isHash = !linkUrl || linkUrl === '#';
      const linkAttr = isHash ? ' onclick="event.preventDefault();"' : '';

      return [
        `            <!-- Item ${numStr} -->`,
        '            <article class="single-project-item">',
        `              <h3 class="editorial-title">${inline(e.title)}</h3>`,
        e.description && `              <p class="editorial-desc">\n                ${inline(e.description)}\n              </p>`,
        `              <a href="${escapeHtml(linkUrl)}" class="editorial-link"${linkAttr}>${escapeHtml(linkLabel)}</a>`,
        '            </article>',
      ]
        .filter(Boolean)
        .join('\n');
    })
    .join('\n\n');
}

// Papers share the project layout: title, one line of text (venue and year), then links.
function renderPapers(lines) {
  return parseEntries(lines)
    .map((e) => {
      const links = parseLinks(e.fields.links || '')
        .map((l) => {
          const external = l.url.startsWith('http') ? ' target="_blank" rel="noopener noreferrer"' : '';
          return `                <a href="${escapeHtml(l.url)}" class="editorial-link"${external}>${escapeHtml(l.label)}</a>`;
        })
        .join('\n');

      return [
        '            <article class="single-project-item">',
        `              <h3 class="editorial-title">${inline(e.title)}</h3>`,
        e.description && `              <p class="editorial-desc">${inline(e.description)}</p>`,
        links && `              <div class="editorial-links">\n${links}\n              </div>`,
        '            </article>',
      ]
        .filter(Boolean)
        .join('\n');
    })
    .join('\n\n');
}

function replaceRegion(html, marker, newContent) {
  const start = `<!-- AUTO_GENERATED_LAB_${marker}_START -->`;
  const end = `<!-- AUTO_GENERATED_LAB_${marker}_END -->`;
  const regex = new RegExp(`${start}[\\s\\S]*?${end}`);

  if (!regex.test(html)) {
    console.warn(`[build-lab] Marker ${marker} not found in lab/lab.html, skipping.`);
    return html;
  }
  return html.replace(regex, `${start}\n${newContent}\n${end}`);
}

export function buildLab() {
  const mdPath = LAB_MD_PATH;
  if (!fs.existsSync(mdPath)) {
    console.warn('[build-lab] lab/lab.md not found, skipping.');
    return;
  }
  if (!fs.existsSync(LAB_HTML_PATH)) {
    console.warn(`[build-lab] ${LAB_HTML_PATH} not found, skipping.`);
    return;
  }

  const rawMd = fs.readFileSync(mdPath, 'utf-8');
  const sections = parseSections(rawMd);

  let html = fs.readFileSync(LAB_HTML_PATH, 'utf-8');

  if (sections['manifesto']) {
    const rendered = renderManifesto(sections['manifesto']);
    html = replaceRegion(html, 'MANIFESTO', rendered);
  }

  if (sections['ongoing projects']) {
    const rendered = renderProjects(sections['ongoing projects']);
    html = replaceRegion(html, 'ONGOING', rendered);
  }

  if (sections['completed projects']) {
    const rendered = renderProjects(sections['completed projects']);
    html = replaceRegion(html, 'COMPLETED', rendered);
  }

  if (sections['papers']) {
    const rendered = renderPapers(sections['papers']);
    html = replaceRegion(html, 'PAPERS', rendered);
  }

  fs.writeFileSync(LAB_HTML_PATH, html, 'utf-8');
  console.log(`[build-lab] Rendered ${path.relative(rootDir, mdPath)} into lab/lab.html`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildLab();
}
