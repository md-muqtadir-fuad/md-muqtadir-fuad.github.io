import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { buildBlogs } from './build-blogs.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const CONTENT_DIR = path.resolve(rootDir, 'blogs-posts/content');

const titleArg = process.argv.slice(2).join(' ').trim();
const title = titleArg || 'New Blog Post';

// Generate slug: prepend 'blog-' if not already present
let rawSlug = title.toLowerCase().replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
if (!rawSlug.startsWith('blog-')) {
  rawSlug = `blog-${rawSlug}`;
}

const today = new Date().toISOString().split('T')[0];
const targetFilePath = path.join(CONTENT_DIR, `${rawSlug}.md`);

if (fs.existsSync(targetFilePath)) {
  console.error(`[new-post] Error: File already exists at: ${targetFilePath}`);
  process.exit(1);
}

const template = `---
title: "${title}"
date: "${today}"
description: "A concise overview of the problem, methodologies, and key findings."
readTime: "5 min read"
---

Write your opening paragraph here. Explain the real-world motivation, technical context, and who benefits from this work.

## Background & Architecture

Describe the system architecture, engineering constraints, or research methodology:

- **Core Concept 1:** Problem definition and data sources.
- **Core Concept 2:** Algorithmic architecture and design choices.

## Technical Implementation

You can insert code snippets with automatic syntax highlighting:

\`\`\`python
def evaluate_metrics(predictions, ground_truth):
    accuracy = (predictions == ground_truth).mean()
    return {"accuracy": accuracy}
\`\`\`

You can also create structured comparison tables:

| Metric | Baseline | Proposed Solution | Improvement |
| :--- | :--- | :--- | :--- |
| Latency | 240 ms | 18 ms | **13.3x faster** |
| Memory Footprint | 1.2 GB | 250 MB | **79% reduction** |
| Accuracy | 88.4% | 94.7% | **+6.3%** |

## Key Insights & Takeaways

> "Summarize a core insight, lesson learned, or key philosophy in an editorial quote."

## Conclusion & Future Work

Outline your next steps, open research questions, or invite readers to collaborate.
`;

fs.writeFileSync(targetFilePath, template, 'utf-8');
console.log(`[new-post] Successfully created new post:`);
console.log(`  Markdown: ${targetFilePath}`);

// Run build to generate HTML immediately
buildBlogs();

console.log(`\nYou can now open and edit: blogs-posts/content/${rawSlug}.md`);
console.log(`Live preview will be available at: /blogs-posts/posts/${rawSlug}.html`);
