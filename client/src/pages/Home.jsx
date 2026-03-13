import { Link } from 'react-router-dom';
import { siteContent } from '../data/siteContent.js';

export default function Home() {
  return (
    <section className="section hero">
      <div className="container">
        <p className="eyebrow">{siteContent.shortTitle}</p>
        <h1>{siteContent.name}</h1>
        <p className="lead">{siteContent.tagline}</p>
        <p className="muted max-width">{siteContent.heroSummary}</p>

        <div className="hero-actions">
          <Link to="/projects" className="btn btn-primary">
            View Projects
          </Link>
          <Link to="/about" className="btn btn-secondary">
            About Me
          </Link>
        </div>
      </div>
    </section>
  );
}