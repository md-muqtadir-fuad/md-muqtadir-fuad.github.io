import { motion } from "motion/react";
import { projectsData as staticProjects } from "../data/projectsData";
import { ArrowRight, Github, ExternalLink, Code, Layers, RefreshCw } from "lucide-react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { db } from "../firebase";
import { collection, getDocs, query, orderBy } from "firebase/firestore";

export default function Projects() {
  const [projects, setProjects] = useState<any[]>(staticProjects);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const q = query(collection(db, "projects"), orderBy("id", "asc"));
        const querySnapshot = await getDocs(q);
        if (!querySnapshot.empty) {
          const fetched = querySnapshot.docs.map(doc => doc.data());
          setProjects(fetched);
        }
      } catch (error) {
        console.error("Error fetching projects:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div className="pt-32 pb-16 px-4 max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="space-y-16"
      >
        <div className="space-y-4">
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-zinc-900 font-display">
            Selected <span className="text-emerald-600 italic">Work</span>
          </h1>
          <p className="text-xl text-zinc-600 max-w-2xl">
            A showcase of engineering design, machine learning, and IoT projects.
          </p>
        </div>

        {loading ? (
          <div className="flex justify-center py-20">
            <RefreshCw className="animate-spin text-emerald-600" size={32} />
          </div>
        ) : (
          <div className="grid md:grid-cols-2 gap-8">
            {projects.map((project, i) => (
              <motion.div
                key={project.slug}
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                className="group flex flex-col bg-white border border-zinc-100 rounded-none overflow-hidden shadow-sm hover:shadow-xl transition-all"
              >
                <div className="aspect-video bg-zinc-100 relative overflow-hidden">
                  <img
                    src={`https://picsum.photos/seed/${project.slug}/800/450`}
                    alt={project.title}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                    referrerPolicy="no-referrer"
                  />
                  <div className="absolute top-4 left-4">
                    <span className="px-4 py-1.5 bg-white/90 backdrop-blur-sm text-zinc-900 rounded-none text-xs font-bold uppercase tracking-wider shadow-sm">
                      {project.category}
                    </span>
                  </div>
                </div>

                <div className="p-8 flex-1 flex flex-col space-y-6">
                  <div className="space-y-2">
                    <h3 className="text-2xl font-bold text-zinc-900 group-hover:text-emerald-600 transition-colors">
                      {project.title}
                    </h3>
                    <p className="text-zinc-600 line-clamp-2">
                      {project.overview || project.shortDescription}
                    </p>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    {project.tools.slice(0, 4).map((tool: string) => (
                      <span key={tool} className="px-3 py-1 bg-emerald-50 text-emerald-700 rounded-none text-xs font-medium">
                        {tool}
                      </span>
                    ))}
                  </div>

                  <div className="pt-4 mt-auto flex items-center justify-between">
                    <Link
                      to={`/projects/${project.slug}`}
                      className="inline-flex items-center gap-2 text-zinc-900 font-bold hover:text-emerald-600 transition-colors"
                    >
                      View Details <ArrowRight size={18} />
                    </Link>
                    <div className="flex gap-4">
                      {project.links.map((link: any, j: number) => (
                        <a
                          key={j}
                          href={link.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-zinc-400 hover:text-emerald-600 transition-colors"
                          title={link.label}
                        >
                          {link.label.toLowerCase().includes('github') ? <Github size={20} /> : <ExternalLink size={20} />}
                        </a>
                      ))}
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </motion.div>
    </div>
  );
}
