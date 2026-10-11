import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const INDEX_HTML_PATH = path.resolve(rootDir, 'index.html');

const escapeHtml = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const plainText = s => s.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[*_`]/g, '').replace(/\s+/g, ' ').trim();
const inline = s => marked.parseInline(s);
const inlineUnderlined = s => inline(s).replace(/<a href="/g, '<a class="underline" href="');
const parseLinks = s => [...s.matchAll(/\[([^\]]+)\]\(([^)\s]+)\)/g)].map(m => ({ label: m[1], url: m[2] }));

// "## Group" headings split entries into groups; entries before the first heading form an untitled group
function splitGroups(markdown) {
  const text = markdown.replace(/<!--[\s\S]*?-->/g, '');
  const groups = [{ name: '', lines: [] }];
  for (const line of text.split(/\r?\n/)) {
    const heading = line.match(/^##\s+(.+?)\s*$/);
    if (heading) groups.push({ name: heading[1], lines: [] });
    else groups[groups.length - 1].lines.push(line);
  }
  return groups;
}

// "### Title" blocks with "- key: value" fields followed by a free-text description
function parseEntries(lines) {
  const entries = [];
  let entry = null;
  for (const line of lines) {
    const title = line.match(/^###\s+(.+?)\s*$/);
    const field = line.match(/^-\s+([a-z]+):\s*(.*?)\s*$/i);
    if (title) {
      entry = { title: title[1], fields: {}, description: '' };
      entries.push(entry);
    } else if (entry && field && !entry.description) {
      entry.fields[field[1].toLowerCase()] = field[2];
    } else if (entry && line.trim()) {
      entry.description += (entry.description ? ' ' : '') + line.trim();
    }
  }
  return entries;
}

function renderGroups(groups, renderGroup) {
  const nonEmpty = groups.filter(g => g.html);
  return nonEmpty
    .map((g, i) => {
      const isLast = i === nonEmpty.length - 1;
      const heading = g.name ? `        <h3 class="subsection-title">${escapeHtml(g.name)}</h3>\n` : '';
      return heading + renderGroup(g, isLast);
    })
    .join('\n\n');
}

const SECTIONS = {
  projects: {
    file: 'content/projects.md',
    render(markdown) {
      const groups = splitGroups(markdown).map(g => {
        const rows = parseEntries(g.lines).map(e => {
          const { image = '', fit = '', links = '' } = e.fields;
          const imgClass = fit.toLowerCase() === 'contain' ? ' class="object-contain p-1"' : '';
          const linkHtml = parseLinks(links).map(l => `<a href="${escapeHtml(l.url)}">${escapeHtml(l.label)}</a>`).join('');
          return [
            '          <div class="project-row">',
            `            <img src="${escapeHtml(image)}" alt="${escapeHtml(plainText(e.title))}"${imgClass} loading="lazy">`,
            '            <div>',
            `              <p class="font-bold">${inline(e.title)}</p>`,
            e.description && `              <p class="text-sm text-gray-800 mt-1">${inline(e.description)}</p>`,
            linkHtml && `              <div class="pub-links">${linkHtml}</div>`,
            '            </div>',
            '          </div>',
          ].filter(Boolean).join('\n');
        });
        return { ...g, html: rows.join('\n') };
      });
      return renderGroups(groups, (g, isLast) => `        <div class="space-y-6${isLast ? '' : ' mb-8'}">\n${g.html}\n        </div>`);
    },
  },

  experience: {
    file: 'content/experience.md',
    render(markdown) {
      const groups = splitGroups(markdown).map(g => {
        const items = parseEntries(g.lines).map(e => {
          const { org = '', dates = '' } = e.fields;
          // With an organisation line the description is a lighter third line; without one it takes the org's place
          const lines = [`<p class="font-bold">${inline(e.title)}</p>`];
          if (org) lines.push(`<p class="text-sm text-gray-800">${inlineUnderlined(org)}</p>`);
          if (e.description) {
            lines.push(org
              ? `<p class="text-sm text-gray-700 mt-1">${inlineUnderlined(e.description)}</p>`
              : `<p class="text-sm text-gray-800">${inlineUnderlined(e.description)}</p>`);
          }
          return `          <li>\n            <div>${lines.join('')}</div>\n            <span>${escapeHtml(dates)}</span>\n          </li>`;
        });
        return { ...g, html: items.join('\n') };
      });
      return renderGroups(groups, (g, isLast) => `        <ul class="cv-list${isLast ? '' : ' mb-8'}">\n${g.html}\n        </ul>`);
    },
  },

  honors: {
    file: 'content/honors.md',
    render(markdown) {
      const groups = splitGroups(markdown).map(g => {
        const items = g.lines
          .map(line => line.match(/^-\s+(.+?)\s*\|\s*(.+?)\s*$/))
          .filter(Boolean)
          .map(([, date, text]) => `          <li><span>${escapeHtml(date)}</span><p>${inlineUnderlined(text)}</p></li>`);
        return { ...g, html: items.join('\n') };
      });
      return renderGroups(groups, (g, isLast) => `        <ul class="news-list${isLast ? '' : ' mb-8'}">\n${g.html}\n        </ul>`);
    },
  },
};

function buildSection(id) {
  const { file, render } = SECTIONS[id];
  const mdPath = path.resolve(rootDir, file);
  if (!fs.existsSync(mdPath)) {
    console.warn(`[build-sections] ${file} not found, skipping.`);
    return;
  }

  const marker = id.toUpperCase();
  const start = `<!-- AUTO_GENERATED_${marker}_START -->`;
  const end = `<!-- AUTO_GENERATED_${marker}_END -->`;
  const regex = new RegExp(`${start}[\\s\\S]*?${end}`);

  const html = fs.readFileSync(INDEX_HTML_PATH, 'utf-8');
  if (!regex.test(html)) {
    console.warn(`[build-sections] ${id} markers not found in index.html, skipping.`);
    return;
  }

  const content = render(fs.readFileSync(mdPath, 'utf-8'));
  const next = html.replace(regex, () => `${start}\n${content}\n        ${end}`);
  if (next !== html) fs.writeFileSync(INDEX_HTML_PATH, next, 'utf-8');
  console.log(`[build-sections] Rendered ${file} into index.html`);
}

export const buildProjects = () => buildSection('projects');
export const buildExperience = () => buildSection('experience');
export const buildHonors = () => buildSection('honors');

export function buildSections() {
  for (const id of Object.keys(SECTIONS)) buildSection(id);
}

// Run directly if executed as CLI
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildSections();
}
