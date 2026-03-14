import { Link } from 'react-router-dom';
import TagList from './TagList.jsx';

export default function ProjectCard({ project }) {
  return (
    <article className="card project-card">
      <div className="project-top">
        <span className="badge">{project.category}</span>
        <span className="meta-text">{project.period}</span>
      </div>

      <h2 className="project-title">{project.title}</h2>

      {project.course ? (
        <p className="meta-text">{project.course}</p>
      ) : null}

      <p className="muted">{project.shortDescription}</p>

      <TagList items={project.tools} />

      <div className="card-actions">
        <Link to={`/projects/${project.slug}`} className="btn btn-secondary">
          View Details
        </Link>
      </div>
    </article>
  );
}