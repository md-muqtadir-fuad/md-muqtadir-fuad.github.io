import { Link } from 'react-router-dom';
import { siteContent } from '../data/siteContent.js';
import { homeData } from '../data/homeData.js';
import { projectsData } from '../data/projectsData.js';
import { publicationsData } from '../data/publicationsData.js';

export default function Home() {
  const featuredProjects = projectsData.slice(0, 3);
  const featuredPublications = publicationsData.slice(0, 2);

  return (
    <>
      <section className="section hero hero-home">
        <div className="container">
          <div className="hero-grid">
            <div>
              <p className="eyebrow">{siteContent.shortTitle}</p>
              <h1>{siteContent.name}</h1>
              <p className="lead">{siteContent.tagline}</p>
              <p className="muted max-width">{siteContent.heroSummary}</p>

              <div className="hero-actions">
                <Link to="/projects" className="btn btn-primary">
                  View Projects
                </Link>
                <Link to="/publications" className="btn btn-secondary">
                  Publications
                </Link>
                <Link to="/contact" className="btn btn-secondary">
                  Contact
                </Link>
              </div>

              <div className="stats-grid">
                {homeData.stats.map((item) => (
                  <div key={item.label} className="stat-tile">
                    <span className="stat-label">{item.label}</span>
                    <strong className="stat-value">{item.value}</strong>
                  </div>
                ))}
              </div>
            </div>

            <aside className="hero-panel">
              <div className="hero-panel-inner">
                <h2>Research & Work Direction</h2>
                <p className="muted">
                  I work at the intersection of AI, industrial engineering,
                  optimization, manufacturing systems, and engineering design.
                </p>

                <ul className="feature-list compact-list">
                  {homeData.focusAreas.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>

                <div className="hero-panel-links">
                  <a
                    href={siteContent.links.github}
                    target="_blank"
                    rel="noreferrer"
                    className="btn btn-secondary"
                  >
                    GitHub
                  </a>
                  <a
                    href={siteContent.links.linkedin}
                    target="_blank"
                    rel="noreferrer"
                    className="btn btn-secondary"
                  >
                    LinkedIn
                  </a>
                </div>
              </div>
            </aside>
          </div>
        </div>
      </section>

      <section className="section section-tight-top">
        <div className="container">
          <div className="home-section-head">
            <div>
              <p className="eyebrow">Featured Projects</p>
              <h2>Selected engineering and AI work</h2>
            </div>

            <Link to="/projects" className="inline-link">
              See all projects
            </Link>
          </div>

          <div className="project-grid">
            {featuredProjects.map((project) => (
              <article key={project.slug} className="card project-card soft-card">
                <div className="project-top">
                  <span className="badge">{project.category}</span>
                  <span className="meta-text">{project.period}</span>
                </div>

                <h3 className="project-title">{project.title}</h3>
                <p className="muted">{project.shortDescription}</p>

                <div className="card-actions">
                  <Link
                    to={`/projects/${project.slug}`}
                    className="btn btn-secondary"
                  >
                    View Details
                  </Link>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="section section-tight-top">
        <div className="container">
          <div className="home-section-head">
            <div>
              <p className="eyebrow">Publications</p>
              <h2>Recent research output</h2>
            </div>

            <Link to="/publications" className="inline-link">
              See all publications
            </Link>
          </div>

          <div className="content-stack">
            {featuredPublications.map((publication) => (
              <article
                key={publication.id}
                className="card publication-card soft-card"
              >
                <div className="publication-top">
                  <div className="publication-badges">
                    <span className="badge">{publication.year}</span>
                    <span className="badge badge-muted">
                      {publication.status}
                    </span>
                  </div>
                </div>

                <h3 className="publication-title">{publication.title}</h3>
                <p className="muted">{publication.authors}</p>
                <p>{publication.venue}</p>
              </article>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}