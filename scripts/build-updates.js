import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { marked } from 'marked';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const UPDATES_MD_PATH = path.resolve(rootDir, 'content/updates.md');
const INDEX_HTML_PATH = path.resolve(rootDir, 'index.html');

const START_MARKER = '<!-- AUTO_GENERATED_UPDATES_START -->';
const END_MARKER = '<!-- AUTO_GENERATED_UPDATES_END -->';

// Parse "## Mon YYYY" headings followed by "- item" bullets (newest first)
function parseUpdates(markdown) {
  const text = markdown.replace(/<!--[\s\S]*?-->/g, '');
  const limitMatch = text.match(/^limit:\s*(\d+)\s*$/m);
  const limit = limitMatch ? parseInt(limitMatch[1], 10) : Infinity;

  const updates = [];
  let currentDate = '';
  for (const line of text.split(/\r?\n/)) {
    const heading = line.match(/^##\s+(.+?)\s*$/);
    if (heading) {
      currentDate = heading[1];
      continue;
    }
    const bullet = line.match(/^[-*]\s+(.+?)\s*$/);
    if (bullet) {
      updates.push({ date: currentDate, text: bullet[1] });
      continue;
    }
    // Indented lines continue the previous bullet
    const continuation = line.match(/^\s{2,}(\S.*?)\s*$/);
    if (continuation && updates.length > 0) {
      updates[updates.length - 1].text += ` ${continuation[1]}`;
    }
  }
  return updates.slice(0, limit);
}

function renderUpdates(updates) {
  return updates
    .map(u => {
      const body = marked.parseInline(u.text).replace(/<a href="/g, '<a class="underline" href="');
      return `          <li><span>${u.date}</span><p>${body}</p></li>`;
    })
    .join('\n');
}

export function buildUpdates() {
  if (!fs.existsSync(UPDATES_MD_PATH)) {
    console.warn('[build-updates] content/updates.md not found, skipping.');
    return;
  }

  const updates = parseUpdates(fs.readFileSync(UPDATES_MD_PATH, 'utf-8'));
  const indexHtml = fs.readFileSync(INDEX_HTML_PATH, 'utf-8');
  const markerRegex = new RegExp(`${START_MARKER}[\\s\\S]*?${END_MARKER}`);

  if (!markerRegex.test(indexHtml)) {
    console.warn('[build-updates] Update markers not found in index.html, skipping.');
    return;
  }

  const replacement = `${START_MARKER}\n${renderUpdates(updates)}\n          ${END_MARKER}`;
  const nextHtml = indexHtml.replace(markerRegex, () => replacement);
  if (nextHtml !== indexHtml) {
    fs.writeFileSync(INDEX_HTML_PATH, nextHtml, 'utf-8');
  }
  console.log(`[build-updates] Rendered ${updates.length} update(s) into index.html`);
}

// Run directly if executed as CLI
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildUpdates();
}
