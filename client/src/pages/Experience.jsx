import SectionHeader from '../components/SectionHeader.jsx';
import TimelineItem from '../components/TimelineItem.jsx';
import { experienceData } from '../data/experienceData.js';

export default function Experience() {
  return (
    <section className="section">
      <div className="container">
        <SectionHeader
          eyebrow="Journey"
          title="Experience"
          description="Work, leadership, and competition experience that reflects both research direction and practical engineering involvement."
        />

        <div className="experience-section">
          <h2>Work Experience</h2>
          <div className="timeline">
            {experienceData.work.map((item) => (
              <TimelineItem
                key={`${item.title}-${item.organization}`}
                item={item}
              />
            ))}
          </div>
        </div>

        <div className="experience-section">
          <h2>Leadership & Service</h2>
          <div className="timeline">
            {experienceData.leadership.map((item) => (
              <TimelineItem
                key={`${item.title}-${item.organization}`}
                item={item}
              />
            ))}
          </div>
        </div>

        <div className="experience-section">
          <h2>Competitions & Hackathons</h2>
          <div className="timeline">
            {experienceData.competitions.map((item) => (
              <TimelineItem
                key={`${item.title}-${item.organization}`}
                item={item}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}