export default function TimelineItem({ item }) {
  return (
    <article className="timeline-item">
      <div className="timeline-marker" />

      <div className="card timeline-card">
        <div className="timeline-top">
          <div>
            <h3 className="timeline-title">{item.title}</h3>
            <p className="meta-text">
              {item.organization}
              {item.location ? ` • ${item.location}` : ''}
            </p>
          </div>

          <span className="badge">{item.period}</span>
        </div>

        {item.bullets?.length ? (
          <ul className="feature-list">
            {item.bullets.map((point) => (
              <li key={point}>{point}</li>
            ))}
          </ul>
        ) : null}

        {item.link ? (
          <a
            href={item.link.url}
            target="_blank"
            rel="noreferrer"
            className="inline-link"
          >
            {item.link.label}
          </a>
        ) : null}
      </div>
    </article>
  );
}