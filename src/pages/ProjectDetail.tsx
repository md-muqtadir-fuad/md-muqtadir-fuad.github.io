import { motion } from "motion/react";
import { useParams, Link } from "react-router-dom";
import { projectsData } from "../data/projectsData";
import { ArrowLeft, ExternalLink, Github, CheckCircle2 } from "lucide-react";

export default function ProjectDetail() {
  const { slug } = useParams();
  const project = projectsData.find((p) => p.slug === slug);

  if (!project) {
    return (
      <div className="pt-32 pb-16 px-4 text-center space-y-8">
        <h1 className="text-4xl font-bold font-display">Project Not Found</h1>
        <Link to="/projects" className="text-emerald-600 font-bold hover:underline">
          Back to Projects
        </Link>
      </div>
    );
  }

  return (
    <div className="pt-32 pb-16 px-4 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="space-y-12"
      >
        <Link
          to="/projects"
          className="inline-flex items-center gap-2 text-zinc-500 hover:text-emerald-600 transition-colors font-medium"
        >
          <ArrowLeft size={18} /> Back to Projects
        </Link>

        <div className="space-y-6">
          <span className="px-4 py-1.5 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold uppercase tracking-wider">
            {project.category}
          </span>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-zinc-900 font-display">
            {project.title}
          </h1>
          <p className="text-xl text-zinc-600 leading-relaxed max-w-3xl">
            {project.overview}
          </p>
        </div>

        <div className="aspect-video rounded-[2.5rem] overflow-hidden border border-zinc-100 shadow-2xl">
          <img
            src={`https://picsum.photos/seed/${project.slug}/1200/675`}
            alt={project.title}
            className="w-full h-full object-cover"
            referrerPolicy="no-referrer"
          />
        </div>

        <div className="grid md:grid-cols-3 gap-12">
          <div className="md:col-span-2 space-y-12">
            <section className="space-y-6">
              <h2 className="text-2xl font-bold font-display">Key Highlights</h2>
              <div className="grid gap-4">
                {project.highlights.map((point, i) => (
                  <div key={i} className="flex gap-4 p-4 bg-zinc-50 rounded-2xl border border-zinc-100">
                    <CheckCircle2 className="text-emerald-500 shrink-0 mt-1" size={20} />
                    <p className="text-zinc-700">{point}</p>
                  </div>
                ))}
              </div>
            </section>
          </div>

          <div className="space-y-12">
            <section className="space-y-6">
              <h2 className="text-2xl font-bold font-display">Tools & Tech</h2>
              <div className="flex flex-wrap gap-2">
                {project.tools.map((tool) => (
                  <span key={tool} className="px-4 py-2 bg-white border border-zinc-100 rounded-xl text-sm font-medium text-zinc-600 shadow-sm">
                    {tool}
                  </span>
                ))}
              </div>
            </section>

            <section className="space-y-6">
              <h2 className="text-2xl font-bold font-display">Links</h2>
              <div className="flex flex-col gap-3">
                {project.links.map((link, i) => (
                  <a
                    key={i}
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center justify-between p-4 bg-zinc-900 text-white rounded-2xl hover:bg-emerald-600 transition-colors"
                  >
                    <span className="font-bold">{link.label}</span>
                    <ExternalLink size={18} />
                  </a>
                ))}
              </div>
            </section>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
