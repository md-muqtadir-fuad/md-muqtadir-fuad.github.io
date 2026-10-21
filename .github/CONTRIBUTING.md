# Contributing

This is my personal portfolio, so I don't accept feature or design changes. Fixes are welcome:

- typos and broken links
- pages that display incorrectly in some browser or screen size
- wrong or outdated details in a publication, project, or blog post

For anything bigger, open an issue first.

## Making a change

```bash
npm install
npm run dev    # http://localhost:3000
```

Most sections of the site are generated from Markdown. Edit the source file, not the HTML; the generated parts are overwritten on every build.

| Section | Source |
| --- | --- |
| Updates | `content/updates.md` |
| Publications | `content/publications.md` |
| Projects, Experience, Honors | `content/projects.md`, `content/experience.md`, `content/honors.md` |
| Blog posts | `blogs-posts/content/` (see its README) |

Run `npm run build` before opening a pull request to make sure the site still builds.

Code you contribute is licensed under the [MIT License](../LICENSE).
