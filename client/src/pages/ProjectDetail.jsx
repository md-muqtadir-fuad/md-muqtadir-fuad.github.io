import { useParams, Link } from 'react-router-dom';

export default function ProjectDetail() {
  const { slug } = useParams();

  return (
    <section className="section">
      <div className="container">
        <h1>Project Detail</h1>
        <p className="lead">Selected project: {slug}</p>
        <Link to="/projects" className="btn btn-secondary">
          Back to Projects
        </Link>
      </div>
    </section>
  );
}