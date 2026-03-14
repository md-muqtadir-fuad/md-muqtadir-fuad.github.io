export default function PublicationCard({ publication }) {
  return (
    <article className="card publication-card">
      <div className="publication-top">
        <div className="publication-badges">
          <span className="badge">{publication.year}</span>
          <span className="badge badge-muted">{publication.status}</span>
          <span className="badge badge-muted">{publication.type}</span>
        </div>
      </div>

      <h2 className="publication-title">{publication.title}</h2>
      <p className="muted">{publication.authors}</p>
      <p>{publication.venue}</p>

      {publication.link ? (
        <a
          href={publication.link}
          target="_blank"
          rel="noreferrer"
          className="inline-link"
        >
          Open record
        </a>
      ) : null}
    </article>
  );
}