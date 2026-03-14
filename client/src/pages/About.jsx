import SectionHeader from '../components/SectionHeader.jsx';
import TagList from '../components/TagList.jsx';
import { aboutData } from '../data/aboutData.js';
import { siteContent } from '../data/siteContent.js';

export default function About() {
  return (
    <section className="section">
      <div className="container">
        <SectionHeader
          eyebrow="Profile"
          title="About"
          description={aboutData.summary[0]}
        />

        <div className="about-top-grid">
          <div className="card soft-card">
            <h2>Overview</h2>
            {aboutData.summary.map((paragraph) => (
              <p key={paragraph} className="muted">
                {paragraph}
              </p>
            ))}
          </div>

          <div className="card about-side-card">
            <h2>Quick Info</h2>
            <div className="quick-info-list">
              <div className="quick-info-item">
                <span className="quick-info-label">Location</span>
                <strong>{siteContent.location}</strong>
              </div>
              <div className="quick-info-item">
                <span className="quick-info-label">Email</span>
                <strong>{siteContent.email}</strong>
              </div>
              <div className="quick-info-item">
                <span className="quick-info-label">Institution</span>
                <strong>BUET</strong>
              </div>
            </div>

            <div className="profile-link-column">
              <a
                href={siteContent.links.resume}
                target="_blank"
                rel="noreferrer"
                className="btn btn-primary"
              >
                View Resume
              </a>
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
              <a
                href={siteContent.links.orcid}
                target="_blank"
                rel="noreferrer"
                className="btn btn-secondary"
              >
                ORCID
              </a>
            </div>
          </div>
        </div>

        <div className="content-stack">
          <div className="grid-two">
            <div className="card">
              <h2>Research Interests</h2>
              <ul className="feature-list">
                {aboutData.researchInterests.map((interest) => (
                  <li key={interest}>{interest}</li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h2>Education</h2>
              {aboutData.education.map((item) => (
                <div key={item.degree}>
                  <h3>{item.degree}</h3>
                  <p className="meta-text">
                    {item.institution} • {item.location}
                  </p>
                  <p className="meta-text">{item.period}</p>
                  <p className="muted">
                    <strong>Coursework:</strong> {item.coursework.join(', ')}
                  </p>
                </div>
              ))}
            </div>
          </div>

          <div>
            <h2>Skills</h2>
            <div className="skills-grid">
              {aboutData.skills.map((group) => (
                <div key={group.title} className="card">
                  <h3>{group.title}</h3>
                  <TagList items={group.items} />
                </div>
              ))}
            </div>
          </div>

          <div className="grid-two">
            <div className="card">
              <h2>Leadership & Service</h2>
              <div className="mini-stack">
                {aboutData.extracurriculars.map((item) => (
                  <div key={`${item.title}-${item.organization}`} className="list-block">
                    <h3>{item.title}</h3>
                    <p className="meta-text">
                      {item.organization} • {item.period}
                    </p>
                    <ul className="feature-list compact-list">
                      {item.points.map((point) => (
                        <li key={point}>{point}</li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </div>

            <div className="mini-stack">
              <div className="card">
                <h2>Honors & Awards</h2>
                <ul className="feature-list">
                  {aboutData.awards.map((award) => (
                    <li key={award}>{award}</li>
                  ))}
                </ul>
              </div>

              <div className="card">
                <h2>Training & Workshops</h2>
                <ul className="feature-list">
                  {aboutData.trainings.map((training) => (
                    <li key={training}>{training}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}