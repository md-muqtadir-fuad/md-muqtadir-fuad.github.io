# Md. Muqtadir Fuad - Portfolio

A modern, responsive portfolio website showcasing engineering projects, research work, publications, and professional achievements. Built with Vite and Tailwind CSS for fast performance and beautiful design.

## Overview

This is the personal portfolio of **Md. Muqtadir Fuad**, an engineer, researcher, and data science enthusiast from Bangladesh. A graduate of Industrial and Production Engineering (IPE) from the Bangladesh University of Engineering and Technology (BUET), this portfolio demonstrates diverse technical expertise through completed projects, academic publications, and professional accomplishments.

## Features

- **Responsive Design** - Mobile-first approach with Tailwind CSS
- **Fast Performance** - Built with Vite for optimized development and production builds
- **Multiple Sections**:
  - **Home** - Introduction and quick overview
  - **Experience** - Professional work history and roles
  - **Projects** - Detailed project showcases and case studies
  - **Publications** - Research papers and technical writings
  - **Achievements** - Awards, certifications, and recognitions
  - **Blogs** - Technical blog posts and insights
  - **Contact** - Get in touch information

## Tech Stack

- **Build Tool**: [Vite 6.2.3](https://vitejs.dev/)
- **Styling**: [Tailwind CSS 4.1.14](https://tailwindcss.com/)
- **Markup**: HTML5
- **Scripting**: Vanilla JavaScript
- **Configuration**: TypeScript config

## Project Structure

```
portfolio-static/
├── index.html              # Home page
├── experience.html         # Experience/career page
├── projects.html           # Projects showcase
├── publications.html       # Research publications
├── achievements.html       # Awards and recognition
├── blogs.html              # Blog listing
├── blog-*.html             # Individual blog posts
├── contacts.html           # Contact page
├── 404.html                # Not found page
├── style.css               # Global styles with Tailwind
├── main.js                 # Main JavaScript
├── metadata.json           # Project metadata
├── package.json            # Project dependencies
├── vite.config.ts          # Vite configuration
├── tsconfig.json           # TypeScript configuration
└── assets/                 # Static assets (images, etc.)
```

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn package manager

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd portfolio-static
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

### Development

Start the development server with hot reload:

```bash
npm run dev
```

The site will be available at `http://localhost:3000` (or `http://0.0.0.0:3000` for network access)

### Build

Create an optimized production build:

```bash
npm run build
```

Output files will be in the `dist/` directory.

### Preview

Preview the production build locally:

```bash
npm run preview
```

## Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server on port 3000 |
| `npm run build` | Create optimized production build |
| `npm run preview` | Preview production build locally |

## Configuration Files

- **vite.config.ts** - Vite build and dev server configuration
- **tsconfig.json** - TypeScript configuration for type safety
- **package.json** - Project metadata and dependencies

## Blog Posts

The portfolio includes multiple technical blog posts covering various topics:

- **Blog Badhan** - IoT and embedded systems
- **Blog Bezier Lab** - Mathematical visualization
- **Blog BNWP** - Water and environmental projects
- **Blog Dengue** - Public health data analysis
- **Blog eGov Lens** - E-governance systems
- **Blog IoT Conveyor** - Industrial IoT applications
- **Blog IoT Platform** - IoT infrastructure
- **Blog QueryNest** - Database optimization
- **Blog Shoe Shiner** - Service industry technology
- **And more** - Various technical topics

## Projects Featured

The portfolio showcases multiple engineering and data science projects demonstrating skills in:

- Industrial engineering and optimization
- IoT and embedded systems
- Data analysis and visualization
- Web development
- E-governance and public technology
- Environmental and public health applications

## Utilities

- **generate_blogs.js** - Script for generating blog pages from metadata
- **fix_projects.js** - Utility for managing project data

## License

This portfolio is personal work. For inquiries regarding projects, research, or collaboration, please visit the contact page.

## Contact

For more information, inquiries, or collaboration opportunities, please visit the contact page on the website or refer to the contact information in the portfolio.

---

**Built with ❤️ using Vite + Tailwind CSS**
