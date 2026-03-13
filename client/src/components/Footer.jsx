import { siteContent } from '../data/siteContent.js';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-inner">
        <p>
          © {new Date().getFullYear()} {siteContent.name}
        </p>

        <div className="footer-links">
          <a href={siteContent.links.github} target="_blank" rel="noreferrer">
            GitHub
          </a>
          <a href={siteContent.links.linkedin} target="_blank" rel="noreferrer">
            LinkedIn
          </a>
          <a href={siteContent.links.orcid} target="_blank" rel="noreferrer">
            ORCID
          </a>
          <a href={`mailto:${siteContent.email}`}>Email</a>
        </div>
      </div>
    </footer>
  );
}