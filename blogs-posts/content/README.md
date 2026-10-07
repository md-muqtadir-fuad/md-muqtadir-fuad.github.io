# Blog Writing & Publishing Guide

Welcome to your Markdown-powered blogging system! You no longer need to write or edit 600+ lines of raw HTML, meta tags, and boilerplate classes.

---

## ⚡ Quick Start: 3 Steps to Publish

### 1. Create a Post
Run the following command in your terminal:
```bash
npm run new:post "Your Post Title"
```
This automatically scaffolds a new `.md` file in `blogs-posts/content/blog-your-post-title.md` with today's date and a starter template.

### 2. Write & Edit
Open the newly created `.md` file in your editor (VS Code, Antigravity IDE, Obsidian, Typora, etc.) and write your post in clean Markdown.

### 3. Live Preview & Save
Make sure your development server is running:
```bash
npm run dev
```
Whenever you press **Ctrl+S** to save your `.md` file, the system instantly:
- Recompiles the Markdown into `blogs-posts/posts/blog-your-post-title.html`
- Injects full SEO metadata, Open Graph cards, schema markup, header, and footer
- Updates the blog card in `blogs-posts/blogs.html`
- Triggers a hot-reload in your browser at `http://localhost:3000`

---

## 📋 Available Commands

| Command | What it does |
|---|---|
| `npm run new:post "Title"` | Creates a new post in `blogs-posts/content/` and compiles it immediately |
| `npm run dev` | Starts local dev server with auto-compilation & live hot-reload on `.md` changes |
| `npm run build` | Compiles all Markdown blogs, optimizes assets, and generates `./dist` for production |
| `npm run blogs:build` | Manually recompiles all `.md` files without starting Vite |

---

## 🏷️ Frontmatter Reference

Every blog post starts with a YAML frontmatter block between `---` lines.

```yaml
---
title: "Your Article Title"
date: "2026-10-08"
category: "Engineering & Research"
readTime: "5 min read"
description: "A short 1-2 sentence overview of the article."
keywords: ["Machine Learning", "Optimization"]
coverImage: "https://i.postimg.cc/6qHXXqjm/1772567890101.jpg"
coverCaption: "System architecture and deployment pipeline."
coverAlt: "Descriptive alt text"
author: "Md. Muqtadir Fuad"
metrics:
  - value: "1,279"
    label: "Total Blood Bags"
  - value: "99.2%"
    label: "Efficiency"
authorBio: true
---
```

### Frontmatter Fields

| Field | Type | Required? | Description |
|---|---|---|---|
| `title` | string | **Yes** | Post title (displayed as H1, page title, and SEO title) |
| `date` | string | **Yes** | Publication date in `YYYY-MM-DD` format |
| `description` | string | **Yes** | Subtitle, meta description, and card description |
| `category` | string | Optional | Category badge (e.g. `Engineering`, `Community & Leadership`) |
| `readTime` | string | Optional | Read time (e.g. `6 min read`). If omitted, auto-calculated from word count |
| `keywords` | array / string | Optional | SEO keywords list |
| `coverImage` | string (URL / path) | Optional | Hero banner image shown below the header |
| `coverCaption` | string | Optional | Caption displayed underneath the cover image |
| `coverAlt` | string | Optional | Image alt text for accessibility |
| `author` | string | Optional | Defaults to `"Md. Muqtadir Fuad"` |
| `metrics` | array of objects | Optional | List of `{ value, label }` shown as a highlight stat bar |
| `authorBio` | boolean | Optional | Whether to display the author bio box (default: `true`) |
| `authorBioTitle`| string | Optional | Title of the bio box |
| `authorBioText` | string (HTML) | Optional | Custom author bio text |
| `authorLinks` | array of `{ label, url }` | Optional | Custom reference links in the bio box |

---

## 🎨 Markdown Formatting Cheatsheet

### 1. Headings
Use `##` for main sections and `###` for sub-sections. Clean IDs are automatically generated for each heading.
```markdown
## Section Title
### Sub-section Title
```

### 2. Code Snippets (Syntax Highlighted)
Code blocks are automatically highlighted with `highlight.js` using the site's dark monochrome theme:
````markdown
```python
def optimize_schedule(tasks):
    return sorted(tasks, key=lambda t: t.deadline)
```
````

### 3. Tables
Tables automatically receive clean monochrome styling with subtle hover states:
```markdown
| Parameter | Baseline | New Model | Delta |
| :--- | :--- | :--- | :--- |
| Latency | 120 ms | 15 ms | **8x faster** |
| Accuracy | 91.2% | 96.8% | **+5.6%** |
```

### 4. Images with Captions
Images in Markdown are automatically wrapped in a bordered container with a centered caption:
```markdown
![System architecture diagram](https://example.com/diagram.png)
```

### 5. Pull Quotes / Editorial Quotes
```markdown
> "A core philosophy or takeaway from your research or project."
```

### 6. Embedded Custom HTML
Because Markdown supports raw HTML, you can insert custom HTML elements whenever you need special styling or interactive components:
```html
<div class="p-4 border border-black bg-gray-100 font-mono text-sm">
  Custom highlighted note or alert box.
</div>
```

---

## 📁 Directory Architecture

```
blogs-posts/
├── content/              <-- WRITE HERE!
│   ├── README.md         <-- This guide
│   ├── template.md       <-- Copy-paste starter template
│   └── blog-badhan.md    <-- Your active markdown post
├── posts/                <-- AUTO-GENERATED HTML (Do not edit manually)
│   ├── blog-badhan.html
│   └── ...
└── blogs.html            <-- Main blog listing page (auto-updated with new post cards)
```

---

## 🚀 Deployment to GitHub Pages

You don't need to do any extra build steps before pushing to GitHub:
1. Commit your changes:
   ```bash
   git add .
   git commit -m "Add new blog post"
   git push origin master
   ```
2. Your GitHub Actions workflow runs `npm run build`, which automatically compiles all Markdown files in `blogs-posts/content/` into HTML and publishes the site to GitHub Pages!
