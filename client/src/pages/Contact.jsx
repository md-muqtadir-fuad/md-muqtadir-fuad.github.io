import { siteContent } from '../data/siteContent.js';

export default function Contact() {
  return (
    <section className="section">
      <div className="container">
        <h1>Contact</h1>
        <p className="lead">
          You can send me a message using the form below or reach me by email.
        </p>

        <div className="contact-grid">
          <div className="card">
            <h2>Reach out</h2>
            <p className="muted">
              Best for project inquiries, research collaboration, speaking, or
              academic discussions.
            </p>

            <div className="contact-links-stack">
              <a href={`mailto:${siteContent.email}`} className="btn btn-secondary">
                Email Me
              </a>
              <a
                href="https://docs.google.com/forms/d/e/1FAIpQLSeMIhRynCuPofFD3-wmOWDBXTQWywxzAPZYck79DxCYXjMGow/viewform?usp=send_form"
                target="_blank"
                rel="noreferrer"
                className="btn btn-primary"
              >
                Open Form in New Tab
              </a>
            </div>
          </div>

          <div className="form-embed-wrap">
            <iframe
              title="Contact Form"
              src={siteContent.contactFormUrl}
              className="contact-iframe"
              loading="lazy"
            >
              Loading…
            </iframe>
          </div>
        </div>
      </div>
    </section>
  );
}