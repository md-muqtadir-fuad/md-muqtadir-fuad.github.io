import fs from 'fs';
import path from 'path';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const SITE_URL = 'https://md-muqtadir-fuad.github.io';
const POSTS_DIR = path.resolve(rootDir, 'blogs-posts/posts');
const CONTENT_DIR = path.resolve(rootDir, 'blogs-posts/content');

// Top-level pages: [url path, source files whose changes affect the page].
// experience/projects/publications/achievements/contacts.html are redirects to the home page, so they are left out.
const PAGES = [
  ['/', ['index.html', 'content/updates.md', 'content/publications.md', 'content/projects.md', 'content/experience.md', 'content/honors.md']],
  ['/blogs-posts/blogs.html', ['blogs-posts/blogs.html']],
];

// Last commit date of a file (YYYY-MM-DD), falling back to its modification time
function lastModified(relPath) {
  const absPath = path.resolve(rootDir, relPath);
  if (!fs.existsSync(absPath)) return null;
  try {
    const date = execFileSync('git', ['log', '-1', '--format=%cs', '--', relPath], {
      cwd: rootDir,
      encoding: 'utf-8',
      stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    if (date) return date;
  } catch {
    // Not a git checkout; use the file time below
  }
  return fs.statSync(absPath).mtime.toISOString().split('T')[0];
}

function latest(relPaths) {
  return relPaths.map(lastModified).filter(Boolean).sort().pop() || null;
}

export function buildSitemap() {
  const entries = PAGES.map(([urlPath, sources]) => ({ loc: SITE_URL + urlPath, lastmod: latest(sources) }));

  const posts = fs.existsSync(POSTS_DIR) ? fs.readdirSync(POSTS_DIR).filter(f => f.endsWith('.html')).sort() : [];
  for (const file of posts) {
    // Markdown-backed posts are regenerated on every build, so date them by their .md source
    const mdSource = path.join('blogs-posts/content', file.replace(/\.html$/, '.md'));
    const sources = fs.existsSync(path.resolve(CONTENT_DIR, path.basename(mdSource)))
      ? [mdSource]
      : [path.join('blogs-posts/posts', file)];
    entries.push({ loc: `${SITE_URL}/blogs-posts/posts/${file}`, lastmod: latest(sources.map(p => p.replace(/\\/g, '/'))) });
  }

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries
  .map(e => `  <url>\n    <loc>${e.loc}</loc>${e.lastmod ? `\n    <lastmod>${e.lastmod}</lastmod>` : ''}\n  </url>`)
  .join('\n')}
</urlset>
`;

  // public/ is what Vite publishes; the root copy is kept in sync for the dev server
  for (const target of ['public/sitemap.xml', 'sitemap.xml']) {
    fs.writeFileSync(path.resolve(rootDir, target), xml, 'utf-8');
  }
  console.log(`[build-sitemap] Wrote ${entries.length} URLs to sitemap.xml`);
}

// Run directly if executed as CLI
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildSitemap();
}
