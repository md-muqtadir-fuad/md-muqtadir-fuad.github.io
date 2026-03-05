# My Personal Portfolio
under development

```
portfolio/
├── client/                  # React (Vite/Create React App)
│   ├── public/              # static files (index.html, favicon, robots.txt)
│   │   └── assets/          # ← optional: move images here
│   ├── src/
│   │   ├── assets/          # images, icons, resume.pdf (if you prefer src import)
│   │   ├── components/      # Navbar.jsx, ProjectCard.jsx, Footer.jsx, etc.
│   │   ├── pages/           # route-based pages
│   │   │   ├── Home.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Projects.jsx
│   │   │   ├── ProjectDetail.jsx
│   │   │   ├── Publications.jsx
│   │   │   ├── Experience.jsx
│   │   │   └── Contact.jsx
│   │   ├── data/            # temp JSON or constants (projects.js, publications.js)
│   │   ├── App.jsx
│   │   ├── main.jsx         # or index.jsx
│   │   └── index.css        # global styles (or App.css)
│   └── package.json
│
├── server/                  # Express + Node
│   ├── config/              # db.js (mongoose connection)
│   ├── controllers/         # ← recommended addition: projectController.js, etc.
│   ├── models/              # Project.js, Publication.js (Mongoose schemas)
│   ├── routes/              # api.js (or split: projects.js, publications.js)
│   ├── .env                 # (gitignore'd)
│   ├── server.js            # or index.js (entry point)
│   └── package.json
│
├── .gitignore
├── README.md
└── .env.example             # optional: template for env vars
```