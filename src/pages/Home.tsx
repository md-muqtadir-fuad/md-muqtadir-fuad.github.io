import { motion } from "motion/react";
import { ArrowRight, BookOpen, ExternalLink } from "lucide-react";
import { Link } from "react-router-dom";
import { siteContent } from "../constants";
import { projectsData } from "../data/projectsData";
import { publicationsData } from "../data/publicationsData";

export default function Home() {
  const selectedProjects = projectsData.slice(0, 2);
  const featuredPublications = publicationsData.slice(0, 2);

  return (
    <div className="pt-24 pb-16 space-y-32">
      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 min-h-[70vh] flex flex-col md:flex-row items-center justify-between gap-12">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          className="flex-1 space-y-8 text-center md:text-left"
        >
          <div className="space-y-4">
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight font-display leading-tight">
              <span className="text-zinc-900">Md. Muqtadir</span>{" "}
              <span className="text-emerald-600">Fuad</span>
            </h1>
            <p className="text-xl md:text-2xl text-zinc-500 max-w-2xl leading-relaxed font-light">
              {siteContent.tagline}
            </p>
          </div>

          <div className="pt-4">
            <Link
              to="/about"
              className="inline-flex items-center justify-center px-8 py-4 bg-zinc-900 text-white font-medium rounded-none hover:bg-emerald-600 transition-all group"
            >
              Learn More <ArrowRight size={20} className="ml-2 group-hover:translate-x-1 transition-transform" />
            </Link>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
          className="flex-1 flex justify-center md:justify-end"
        >
          <div className="relative w-64 h-64 md:w-96 md:h-96">
            <div className="absolute inset-0 border-2 border-emerald-600 translate-x-4 translate-y-4 -z-10" />
            <div className="w-full h-full overflow-hidden border border-zinc-200 bg-zinc-100 shadow-2xl">
              <img 
                src={siteContent.photoUrl} 
                alt={siteContent.name}
                className="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-700"
                referrerPolicy="no-referrer"
              />
            </div>
          </div>
        </motion.div>
      </section>

      {/* Selected Work Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div className="flex items-end justify-between border-b border-zinc-100 pb-8">
          <div className="space-y-2">
            <h2 className="text-sm font-bold uppercase tracking-[0.2em] text-emerald-600">
              Selected Work
            </h2>
            <p className="text-3xl font-light text-zinc-900">
              Featured Projects
            </p>
          </div>
          <Link 
            to="/projects" 
            className="text-sm font-medium text-zinc-400 hover:text-emerald-600 transition-colors flex items-center gap-2 mb-1"
          >
            View all <ArrowRight size={16} />
          </Link>
        </div>

        <div className="grid md:grid-cols-2 gap-12">
          {selectedProjects.map((project, i) => (
            <motion.div
              key={project.slug}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: i * 0.1 }}
              className="group space-y-6"
            >
              <Link to={`/projects/${project.slug}`} className="block aspect-video overflow-hidden bg-zinc-100 border border-zinc-100">
                <img
                  src={`https://picsum.photos/seed/${project.slug}/800/450`}
                  alt={project.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 grayscale hover:grayscale-0"
                  referrerPolicy="no-referrer"
                />
              </Link>
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <h3 className="text-xl font-medium text-zinc-900 group-hover:text-emerald-600 transition-colors">
                    {project.title}
                  </h3>
                  <span className="text-xs uppercase tracking-widest text-zinc-400">
                    {project.category.split(' / ')[0]}
                  </span>
                </div>
                <p className="text-zinc-500 text-sm line-clamp-1 font-light">
                  {project.shortDescription}
                </p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Featured Publications Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div className="flex items-end justify-between border-b border-zinc-100 pb-8">
          <div className="space-y-2">
            <h2 className="text-sm font-bold uppercase tracking-[0.2em] text-emerald-600">
              Research
            </h2>
            <p className="text-3xl font-light text-zinc-900">
              Featured Publications
            </p>
          </div>
          <Link 
            to="/publications" 
            className="text-sm font-medium text-zinc-400 hover:text-emerald-600 transition-colors flex items-center gap-2 mb-1"
          >
            All publications <ArrowRight size={16} />
          </Link>
        </div>

        <div className="grid gap-8">
          {featuredPublications.map((pub, i) => (
            <motion.div
              key={pub.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: i * 0.1 }}
              className="group p-8 border border-zinc-100 hover:border-emerald-600/20 hover:bg-emerald-50/30 transition-all"
            >
              <div className="flex flex-col md:flex-row md:items-start justify-between gap-6">
                <div className="space-y-4 flex-1">
                  <div className="flex items-center gap-3">
                    <span className="px-2 py-1 bg-zinc-100 text-zinc-500 text-[10px] font-bold uppercase tracking-wider">
                      {pub.year}
                    </span>
                    <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-600">
                      {pub.type}
                    </span>
                  </div>
                  <h3 className="text-xl font-medium text-zinc-900 group-hover:text-emerald-600 transition-colors leading-snug">
                    {pub.title}
                  </h3>
                  <p className="text-zinc-500 text-sm font-light italic">
                    {pub.authors}
                  </p>
                </div>
                {pub.link && (
                  <a 
                    href={pub.link} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="p-3 border border-zinc-100 text-zinc-400 hover:text-emerald-600 hover:border-emerald-600 transition-all self-start"
                  >
                    <ExternalLink size={20} />
                  </a>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </section>
    </div>
  );
}
