import { siteContent } from '../data/siteContent.js';

export default function About() {
  return (
    <section className="section">
      <div className="container">
        <h1>About</h1>
        <p className="lead">{siteContent.aboutSummary}</p>

        <div className="card">
          <h2>Current direction</h2>
          <p>
            This page will later include your full bio, education, research
            interests, skills, and selected achievements.
          </p>
        </div>
      </div>
    </section>
  );
}