import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import matter from 'gray-matter';
import { marked } from 'marked';
import hljs from 'highlight.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const CONTENT_DIR = path.resolve(rootDir, 'blogs-posts/content');
const POSTS_DIR = path.resolve(rootDir, 'blogs-posts/posts');
const BLOGS_HTML_PATH = path.resolve(rootDir, 'blogs-posts/blogs.html');

// Configure marked with highlight.js and clean semantics
const customRenderer = {
  heading(token) {
    const text = this.parser.parseInline(token.tokens);
    const id = text.toLowerCase().replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
    return `<h${token.depth} id="${id}">${text}</h${token.depth}>\n`;
  },

  code(token) {
    const text = token.text;
    const lang = token.lang;
    let highlighted = text;
    let validLang = lang;
    if (lang && hljs.getLanguage(lang)) {
      try {
        highlighted = hljs.highlight(text, { language: lang }).value;
      } catch {
        highlighted = text;
      }
    } else {
      try {
        const auto = hljs.highlightAuto(text);
        highlighted = auto.value;
        validLang = auto.language;
      } catch {
        highlighted = text;
      }
    }

    const langBadge = validLang ? `<div class="text-xs font-mono uppercase text-gray-400 pb-2 border-b border-gray-700 mb-2">${validLang}</div>` : '';
    return `<pre><code class="hljs ${validLang ? 'language-' + validLang : ''}">${langBadge}${highlighted}</code></pre>\n`;
  },

  image(token) {
    const caption = token.text || token.title || '';
    return `<div class="my-8 border border-black bg-gray-50 overflow-hidden">
      <img src="${token.href}" alt="${caption}" class="w-full h-auto object-cover block" loading="lazy" />
      ${caption ? `<p class="font-mono text-xs text-gray-600 p-2 text-center border-t border-black bg-white mb-0">${caption}</p>` : ''}
    </div>\n`;
  },

  link(token) {
    const text = this.parser.parseInline(token.tokens);
    const isExternal = token.href.startsWith('http://') || token.href.startsWith('https://');
    const targetAttr = isExternal ? ' target="_blank" rel="noopener noreferrer"' : '';
    const titleAttr = token.title ? ` title="${token.title}"` : '';
    return `<a href="${token.href}"${targetAttr}${titleAttr}>${text}</a>`;
  }
};

marked.use({ renderer: customRenderer, gfm: true, breaks: false });

function calculateReadTime(text) {
  const wordCount = text.trim().split(/\s+/).length;
  const minutes = Math.max(1, Math.ceil(wordCount / 200));
  return `${minutes} min read`;
}

function formatDate(dateStr) {
  if (!dateStr) return '';
  const date = new Date(dateStr);
  if (isNaN(date.getTime())) return dateStr;
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

function generateHtmlPage({ frontmatter, contentHtml, slug, rawMarkdown }) {
  const title = frontmatter.title || 'Blog Post';
  const description = frontmatter.description || '';
  const dateStr = frontmatter.date || '';
  const formattedDate = formatDate(dateStr);
  const readTime = frontmatter.readTime || calculateReadTime(rawMarkdown);
  const category = frontmatter.category || '';
  const coverImage = frontmatter.coverImage || '';
  const coverCaption = frontmatter.coverCaption || '';
  const coverAlt = frontmatter.coverAlt || title;
  const keywords = Array.isArray(frontmatter.keywords) ? frontmatter.keywords.join(', ') : (frontmatter.keywords || '');
  const author = frontmatter.author || 'Md. Muqtadir Fuad';
  const canonicalUrl = `https://md-muqtadir-fuad.github.io/blogs-posts/posts/${slug}.html`;

  // Hero Cover Image HTML
  let heroImageHtml = '';
  if (coverImage) {
    heroImageHtml = `
      <!-- Featured Image -->
      <div class="mb-12">
        <img src="${coverImage}"
          alt="${coverAlt}"
          class="w-full h-auto max-h-[550px] object-cover border border-black">
        ${coverCaption ? `<p class="font-mono text-xs text-gray-600 mt-2 text-center">${coverCaption}</p>` : ''}
      </div>`;
  }

  // Metrics Highlight Bar (optional)
  let metricsHtml = '';
  if (Array.isArray(frontmatter.metrics) && frontmatter.metrics.length > 0) {
    metricsHtml = `
      <!-- Quick Metrics Highlight Bar -->
      <div class="grid grid-cols-2 md:grid-cols-${Math.min(4, frontmatter.metrics.length)} gap-4 mb-12">
        ${frontmatter.metrics.map(m => `
        <div class="border border-black p-4 text-center bg-gray-50">
          <span class="block text-2xl md:text-3xl font-bold font-mono">${m.value}</span>
          <span class="font-mono text-xs uppercase tracking-wider text-gray-600">${m.label}</span>
        </div>`).join('\n')}
      </div>`;
  }

  // Author Bio / Reference Box
  let authorBioHtml = '';
  if (frontmatter.authorBio !== false) {
    const bioTitle = frontmatter.authorBioTitle || 'About the Author &amp; Organization';
    const bioText = frontmatter.authorBioText || '<strong>Md. Muqtadir Fuad</strong> is a graduate in Industrial and Production Engineering from BUET, conducting research at the intersection of Operations Research, Machine Learning, and Social Impact.';
    
    let linksHtml = '';
    if (Array.isArray(frontmatter.authorLinks) && frontmatter.authorLinks.length > 0) {
      linksHtml = `
        <div class="flex flex-wrap gap-4 text-xs mt-3">
          ${frontmatter.authorLinks.map(l => `<a href="${l.url}" target="_blank" rel="noopener noreferrer" class="hover:underline font-bold">${l.label} &rarr;</a>`).join('\n')}
        </div>`;
    }

    authorBioHtml = `
      <!-- Author Bio / Reference Box -->
      <div class="mt-12 p-6 border border-black bg-gray-50 font-mono text-sm">
        <div class="font-bold uppercase tracking-wider mb-2 text-black">${bioTitle}</div>
        <p class="text-gray-800 mb-3 font-sans text-sm leading-relaxed">
          ${bioText}
        </p>
        ${linksHtml}
      </div>`;
  }

  return `<!DOCTYPE html>
<html lang="en">

<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-BJBJDYRXEB"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-BJBJDYRXEB');
  </script>

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  
  <!-- SEO Primary Meta Tags -->
  <title>${title} | Md. Muqtadir Fuad</title>
  <meta name="title" content="${title} | Md. Muqtadir Fuad" />
  <meta name="description" content="${description.replace(/"/g, '&quot;')}" />
  ${keywords ? `<meta name="keywords" content="${keywords.replace(/"/g, '&quot;')}" />` : ''}
  <meta name="author" content="${author}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="theme-color" content="#000000" />
  <link rel="canonical" href="${canonicalUrl}" />

  <!-- Favicon -->
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article" />
  <meta property="og:url" content="${canonicalUrl}" />
  <meta property="og:title" content="${title} | Md. Muqtadir Fuad" />
  <meta property="og:description" content="${description.replace(/"/g, '&quot;')}" />
  ${coverImage ? `<meta property="og:image" content="${coverImage}" />` : '<meta property="og:image" content="https://md-muqtadir-fuad.github.io/apple-touch-icon.png" />'}
  <meta property="og:site_name" content="Md. Muqtadir Fuad" />
  <meta property="og:locale" content="en_US" />
  ${dateStr ? `<meta property="article:published_time" content="${dateStr}" />` : ''}
  <meta property="article:author" content="${author}" />
  ${category ? `<meta property="article:section" content="${category}" />` : ''}

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="${canonicalUrl}" />
  <meta name="twitter:title" content="${title} | Md. Muqtadir Fuad" />
  <meta name="twitter:description" content="${description.replace(/"/g, '&quot;')}" />
  ${coverImage ? `<meta name="twitter:image" content="${coverImage}" />` : '<meta name="twitter:image" content="https://md-muqtadir-fuad.github.io/apple-touch-icon.png" />'}

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "${title.replace(/"/g, '\\"')}",
    "description": "${description.replace(/"/g, '\\"')}",
    "image": "${coverImage || 'https://md-muqtadir-fuad.github.io/apple-touch-icon.png'}",
    "datePublished": "${dateStr}",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "${canonicalUrl}"
    },
    "author": {
      "@type": "Person",
      "name": "${author}",
      "url": "https://md-muqtadir-fuad.github.io"
    },
    "publisher": {
      "@type": "Person",
      "name": "Md. Muqtadir Fuad"
    },
    "inLanguage": "en-US"
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/style.css">
  <style>
    /* Clean highlight.js code styling */
    .hljs-keyword, .hljs-selector-tag { color: #f975e1; font-weight: bold; }
    .hljs-string, .hljs-attribute { color: #9ecbff; }
    .hljs-comment, .hljs-quote { color: #6a737d; font-style: italic; }
    .hljs-title, .hljs-section { color: #b392f0; font-weight: bold; }
    .hljs-number, .hljs-literal { color: #79b8ff; }
    .hljs-variable, .hljs-template-variable { color: #ffab70; }
  </style>
</head>

<body class="bg-white text-black min-h-screen flex flex-col selection:bg-black selection:text-white">

  <!-- Desktop Header -->
  <header class="fixed top-0 w-full bg-white border-b border-black z-50">
    <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
      <a href="/" class="font-bold text-lg font-mono tracking-tighter">MMF.</a>
      <nav class="hidden md:flex gap-8 font-mono text-sm uppercase">
        <a href="/" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Home</a>
        <a href="/experience.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Experience</a>
        <a href="/projects.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Projects</a>
        <a href="/publications.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Publications</a>
        <a href="/achievements.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Achievements</a>
      </nav>
      <button id="menu-btn"
        class="md:hidden font-mono text-sm border border-black px-3 py-1 uppercase hover:bg-black hover:text-white transition-colors">
        MENU
      </button>
    </div>
  </header>

  <!-- Mobile Nav -->
  <div id="mobile-nav"
    class="hidden fixed inset-0 top-16 bg-white z-40 border-b border-black p-6 flex flex-col gap-6 font-mono text-2xl uppercase">
    <a href="/" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Home</a>
    <a href="/experience.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Experience</a>
    <a href="/projects.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Projects</a>
    <a href="/publications.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Publications</a>
    <a href="/achievements.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Achievements</a>
  </div>

  <main class="flex-grow max-w-3xl mx-auto px-6 pt-32 pb-24 w-full">
    <article class="mb-16">
      <header class="mb-10">
        <div class="mb-4 font-mono text-sm flex flex-wrap items-center gap-3 text-gray-600">
          ${formattedDate ? `<time datetime="${dateStr}">${formattedDate}</time>` : ''}
          ${formattedDate && readTime ? '<span>•</span>' : ''}
          ${readTime ? `<span>${readTime}</span>` : ''}
          ${category ? `<span>•</span><span class="border border-black px-2 py-0.5 text-xs font-mono uppercase bg-gray-50">${category}</span>` : ''}
        </div>
        <h1 class="text-4xl md:text-5xl font-bold tracking-tight mb-6">${title}</h1>
        ${description ? `<p class="text-xl text-gray-700 leading-relaxed">${description}</p>` : ''}
      </header>

      ${heroImageHtml}

      ${metricsHtml}

      <div class="prose prose-lg max-w-none text-gray-800 space-y-6">
        ${contentHtml}
      </div>

      ${authorBioHtml}

      <div class="mt-16 pt-8 border-t border-black flex justify-between items-center">
        <a href="/blogs-posts/blogs.html" class="font-mono text-sm uppercase hover:underline flex items-center gap-2">
          &larr; Back to Blogs
        </a>
        <a href="/experience.html" class="font-mono text-sm uppercase hover:underline">
          View Experience &rarr;
        </a>
      </div>
    </article>
  </main>

  <footer class="border-t border-black bg-gray-50 text-black mt-auto">
    <div class="max-w-6xl mx-auto px-6 py-12">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
        <div>
          <h3 class="text-xl font-bold font-mono">Md. Muqtadir Fuad</h3>
          <p class="text-xs text-gray-600 font-mono">Open for research inquiries, collaboration, and technical exchange.</p>
        </div>
        <div class="flex flex-wrap gap-4 font-mono text-xs">
          <a href="/" class="hover:underline">Home</a>
          <a href="/experience.html" class="hover:underline">Experience</a>
          <a href="/projects.html" class="hover:underline">Projects</a>
          <a href="/publications.html" class="hover:underline">Publications</a>
          <a href="/blogs-posts/blogs.html" class="hover:underline">Blogs</a>
          <a href="/contacts.html" class="hover:underline">Contacts</a>
        </div>
      </div>

      <!-- Matrix of 8 Platforms (Borderless Clean Style) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-6 gap-y-4 mb-10">

        <!-- 1. Official Email -->
        <a href="mailto:muqtadir@iat.buet.ac.bd" class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 21h18M3 10h18M5 10v11M19 10v11M9 10v11M14 10v11M12 3L2 10h20L12 3z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">Official Email</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">muqtadir@iat.buet.ac.bd</div>
          </div>
        </a>

        <!-- 2. Personal Email -->
        <a href="mailto:mmfuad01@gmail.com" class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="4" width="20" height="16" rx="2" />
              <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">Personal Email</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">mmfuad01@gmail.com</div>
          </div>
        </a>

        <!-- 3. Google Scholar -->
        <a href="https://scholar.google.com/citations?user=KumeQCkAAAAJ&hl=en" target="_blank" rel="noopener noreferrer"
          class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path
                d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">Google Scholar</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">scholar/KumeQCkAAAAJ</div>
          </div>
        </a>

        <!-- 4. ORCID -->
        <a href="https://orcid.org/0009-0009-4362-0780" target="_blank" rel="noopener noreferrer"
          class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path
                d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.016-5.325 5.016h-3.919V7.416zm1.444 1.306v7.444h2.297c2.359 0 3.869-1.516 3.869-3.722 0-2.016-1.397-3.722-3.816-3.722h-2.35z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">ORCID</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">0009-0009-4362-0780</div>
          </div>
        </a>

        <!-- 5. ResearchGate -->
        <a href="https://www.researchgate.net/profile/Md-Muqtadir-Fuad?ev=hdr_xprf" target="_blank"
          rel="noopener noreferrer" class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path
                d="M19.586 0c-.818 0-1.508.19-2.073.565-.563.377-.97.936-1.213 1.68a3.193 3.193 0 0 0-.112.437 8.363 8.363 0 0 0-.078.53 9 9 0 0 0-.79-1.078c-.37-.417-.82-.74-1.35-.97C13.44.433 12.81.3 12.08.3c-.928 0-1.78.21-2.556.63-.775.42-1.42 1.01-1.933 1.77-.514.76-.894 1.66-1.14 2.7-.248 1.04-.372 2.18-.372 3.42 0 1.25.124 2.39.372 3.43.246 1.04.626 1.94 1.14 2.7.513.76 1.158 1.35 1.933 1.77.776.42 1.628.63 2.556.63.79 0 1.467-.14 2.03-.42.564-.28 1.04-.66 1.43-1.14v4.54h2.15V9.45c0-1.2-.1-2.2-.3-3-.2-.8-.5-1.4-.9-1.9-.4-.5-.9-.9-1.5-1.1-.6-.2-1.3-.3-2.1-.3-.6 0-1.2.1-1.7.3-.5.2-.9.5-1.2.9-.3.4-.6.9-.7 1.4-.1.5-.2 1.1-.2 1.8h-2.1c0-.9.1-1.7.4-2.4.3-.7.7-1.4 1.2-1.9.5-.5 1.2-.9 1.9-1.2.7-.3 1.6-.4 2.5-.4.8 0 1.5.1 2.1.3.6.2 1.1.5 1.5.9.4.4.7.9.9 1.5.2.6.3 1.3.3 2.1v.37c.36-.61.85-1.1 1.46-1.47.62-.37 1.36-.55 2.22-.55 1.17 0 2.1.38 2.78 1.14.68.76 1.02 1.83 1.02 3.21v7.62h-2.15v-7.2c0-.96-.2-1.68-.6-2.17-.4-.49-1-.73-1.8-.73-.55 0-1.04.14-1.47.43-.43.28-.77.7-.99 1.24v8.43h-2.15V6.7z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">ResearchGate</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">profile/Md-Muqtadir-Fuad</div>
          </div>
        </a>

        <!-- 6. GitHub -->
        <a href="https://github.com/md-muqtadir-fuad" target="_blank" rel="noopener noreferrer"
          class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path fill-rule="evenodd" clip-rule="evenodd"
                d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">GitHub</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">github.com/md-muqtadir-fuad</div>
          </div>
        </a>

        <!-- 7. LinkedIn -->
        <a href="https://www.linkedin.com/in/md-muqtadir-fuad/" target="_blank" rel="noopener noreferrer"
          class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path
                d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.45a1.64 1.64 0 1 0 0 3.28 1.64 1.64 0 0 0 0-3.28z" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">LinkedIn</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">in/md-muqtadir-fuad</div>
          </div>
        </a>

        <!-- 8. Curriculum Vitae -->
        <a href="https://drive.google.com/drive/folders/1JUhDSJzOHMZNoj8A99ni9DeYwGfImAQz?usp=sharing" target="_blank"
          rel="noopener noreferrer" class="group flex items-center gap-3 py-1.5 transition-colors">
          <div
            class="w-8 h-8 rounded border border-black/25 bg-white flex items-center justify-center shrink-0 group-hover:border-black group-hover:bg-black group-hover:text-white transition-colors">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
              <polyline points="14 2 14 8 20 8" />
            </svg>
          </div>
          <div class="overflow-hidden">
            <div class="font-bold text-xs uppercase tracking-wider group-hover:underline">Curriculum Vitae</div>
            <div class="font-mono text-[11px] text-gray-500 truncate">Google Drive [PDF] &rarr;</div>
          </div>
        </a>

      </div>

      <!-- Bottom Line -->
      <div
        class="border-t border-black/20 pt-6 flex flex-col sm:flex-row justify-between items-center gap-3 text-xs font-mono text-gray-600">
        <div>&copy; 2026 Md. Muqtadir Fuad. All rights reserved.</div>
      </div>
    </div>
  </footer>

  <script type="module" src="/main.js"></script>
</body>

</html>`;
}

function updateBlogsListing(postsMeta) {
  if (!fs.existsSync(BLOGS_HTML_PATH)) return;

  let blogsHtml = fs.readFileSync(BLOGS_HTML_PATH, 'utf-8');

  const START_MARKER = '<!-- AUTO_GENERATED_POSTS_START -->';
  const END_MARKER = '<!-- AUTO_GENERATED_POSTS_END -->';

  // Ensure markers exist in blogs.html right after <div class="grid grid-cols-1 gap-8">
  if (!blogsHtml.includes(START_MARKER)) {
    const gridMatch = /<div class="grid grid-cols-1 gap-8">/;
    if (gridMatch.test(blogsHtml)) {
      blogsHtml = blogsHtml.replace(
        gridMatch,
        `<div class="grid grid-cols-1 gap-8">\n        ${START_MARKER}\n        ${END_MARKER}`
      );
    }
  }

  // Filter posts that are not already listed as legacy manual posts
  const outsideContent = blogsHtml.replace(new RegExp(`${START_MARKER}[\\s\\S]*?${END_MARKER}`), '');

  const cardsToInsert = [];
  for (const post of postsMeta) {
    const postUrl = `/blogs-posts/posts/${post.slug}.html`;
    // If the legacy HTML already has an article linking to this post, don't duplicate it in the auto-grid
    if (outsideContent.includes(postUrl)) {
      continue;
    }

    const formattedDate = formatDate(post.date);
    const categoryBadge = post.category
      ? `<span class="border border-black px-1.5 py-0.5 bg-black text-white">${post.category}</span>`
      : '';

    const card = `
        <!-- Auto Generated Blog Card: ${post.title} -->
        <article class="border-b border-black p-6 hover:bg-gray-50 transition-colors flex flex-col h-full group">
          <div class="mb-4">
            ${formattedDate ? `<time class="font-mono text-sm block mb-2">${formattedDate}</time>` : ''}
            <h3 class="text-xl font-bold font-mono tracking-tight group-hover:underline">
              <a href="${postUrl}">
                ${post.title}
              </a>
            </h3>
          </div>
          ${post.description ? `<p class="text-sm mb-6 flex-grow">${post.description}</p>` : ''}
          <a href="${postUrl}" class="font-mono text-sm border border-black px-4 py-2 uppercase hover:bg-black hover:text-white transition-colors text-center inline-block w-fit">Read Post</a>
        </article>`;
    cardsToInsert.push(card);
  }

  const replacement = `${START_MARKER}${cardsToInsert.join('\n')}\n        ${END_MARKER}`;
  const markerRegex = new RegExp(`${START_MARKER}[\\s\\S]*?${END_MARKER}`);
  if (markerRegex.test(blogsHtml)) {
    blogsHtml = blogsHtml.replace(markerRegex, replacement);
    fs.writeFileSync(BLOGS_HTML_PATH, blogsHtml, 'utf-8');
    console.log(`[build-blogs] Updated blogs.html with ${cardsToInsert.length} auto-generated posts.`);
  }
}

export function buildBlogs() {
  if (!fs.existsSync(CONTENT_DIR)) {
    fs.mkdirSync(CONTENT_DIR, { recursive: true });
  }
  if (!fs.existsSync(POSTS_DIR)) {
    fs.mkdirSync(POSTS_DIR, { recursive: true });
  }

  const files = fs.readdirSync(CONTENT_DIR).filter(f => {
    if (!f.endsWith('.md')) return false;
    const lower = f.toLowerCase();
    return !lower.startsWith('_') && lower !== 'readme.md' && lower !== 'template.md';
  });
  console.log(`[build-blogs] Found ${files.length} markdown file(s) in blogs-posts/content/`);

  const postsMeta = [];

  for (const file of files) {
    const slug = file.replace(/\.md$/, '');
    const filePath = path.join(CONTENT_DIR, file);
    const rawContent = fs.readFileSync(filePath, 'utf-8');

    const { data: frontmatter, content: rawMarkdown } = matter(rawContent);
    const contentHtml = marked.parse(rawMarkdown);

    const fullHtml = generateHtmlPage({
      frontmatter,
      contentHtml,
      slug,
      rawMarkdown
    });

    const outputPath = path.join(POSTS_DIR, `${slug}.html`);
    fs.writeFileSync(outputPath, fullHtml, 'utf-8');
    console.log(`[build-blogs] Generated ${slug}.html`);

    postsMeta.push({
      slug,
      title: frontmatter.title || slug,
      date: frontmatter.date || '',
      description: frontmatter.description || '',
      category: frontmatter.category || '',
    });
  }

  // Sort by date descending
  postsMeta.sort((a, b) => new Date(b.date || 0) - new Date(a.date || 0));

  updateBlogsListing(postsMeta);

  return postsMeta;
}

// Run directly if executed as CLI
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  buildBlogs();
}
