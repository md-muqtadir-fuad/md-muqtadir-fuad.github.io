import { Link, useParams } from 'react-router-dom';
import TagList from '../components/TagList.jsx';
import { projectsData } from '../data/projectsData.js';

export default function ProjectDetail() {
  const { slug } = useParams();
  const project = projectsData.find((item) => item.slug === slug);

  if (!project) {
    return (
      <section className="section">
        <div className="container">
          <h1>Project not found</h1>
          <p className="lead">The project you are looking for does not exist.</p>
          <Link to="/projects" className="btn btn-secondary">
            Back to Projects
          </Link>
        </div>
      </section>
    );
  }

  return (
    <section className="section">
      <div className="container">
        <p className="eyebrow">{project.category}</p>
        <h1>{project.title}</h1>
        <p className="lead">{project.overview}</p>

        <div className="detail-meta-row">
          <span className="badge">{project.period}</span>
          {project.course ? <span className="badge badge-muted">{project.course}</span> : null}
        </div>

        <div className="detail-actions">
          <Link to="/projects" className="btn btn-secondary">
            Back to Projects
          </Link>

          {project.links?.map((link) => (
            <a
              key={link.url}
              href={link.url}
              target="_blank"
              rel="noreferrer"
              className="btn btn-primary"
            >
              {link.label}
            </a>
          ))}
        </div>

        <div className="grid-two detail-grid">
          <div className="card">
            <h2>Highlights</h2>
            <ul className="feature-list">
              {project.highlights.map((point) => (
                <li key={point}>{point}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h2>Tools & Topics</h2>
            <TagList items={project.tools} />
          </div>
        </div>
      </div>
    </section>
  );
}