import SectionHeader from '../components/SectionHeader.jsx';
import PublicationCard from '../components/PublicationCard.jsx';
import { publicationsData } from '../data/publicationsData.js';

export default function Publications() {
  return (
    <section className="section">
      <div className="container">
        <SectionHeader
          eyebrow="Research Output"
          title="Publications"
          description="Conference papers, research outputs, and manuscripts across AI, Bengali NLP, forecasting, smart manufacturing, and engineering analysis."
        />

        <div className="content-stack">
          {publicationsData.map((publication) => (
            <PublicationCard key={publication.id} publication={publication} />
          ))}
        </div>
      </div>
    </section>
  );
}