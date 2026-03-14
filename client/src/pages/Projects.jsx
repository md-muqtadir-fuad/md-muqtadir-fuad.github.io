import SectionHeader from '../components/SectionHeader.jsx';
import ProjectCard from '../components/ProjectCard.jsx';
import { projectsData } from '../data/projectsData.js';

export default function Projects() {
  return (
    <section className="section">
      <div className="container">
        <SectionHeader
          eyebrow="Selected Work"
          title="Projects"
          description="A mix of academic, design, IoT, and hackathon projects built around engineering, intelligent systems, and practical problem solving."
        />

        <div className="project-grid">
          {projectsData.map((project) => (
            <ProjectCard key={project.slug} project={project} />
          ))}
        </div>
      </div>
    </section>
  );
}