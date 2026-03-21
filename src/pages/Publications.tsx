import { motion, AnimatePresence } from "motion/react";
import { publicationsData as staticPublications } from "../data/publicationsData";
import { FileText, ExternalLink, Calendar, User, MapPin, Tag, ChevronDown, ChevronUp, RefreshCw } from "lucide-react";
import { useState, useEffect } from "react";
import { db } from "../firebase";
import { collection, getDocs, query, orderBy } from "firebase/firestore";

export default function Publications() {
  const [expandedId, setExpandedId] = useState<number | null>(null);
  const [publications, setPublications] = useState<any[]>(staticPublications);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPublications = async () => {
      try {
        const q = query(collection(db, "publications"), orderBy("year", "desc"));
        const querySnapshot = await getDocs(q);
        if (!querySnapshot.empty) {
          const fetched = querySnapshot.docs.map(doc => doc.data());
          // Sort by year descending, then by id descending (assuming newer IDs are more recent)
          fetched.sort((a, b) => {
            if (b.year !== a.year) return b.year.localeCompare(a.year);
            return b.id - a.id;
          });
          setPublications(fetched);
        }
      } catch (error) {
        console.error("Error fetching publications:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPublications();
  }, []);

  const toggleAbstract = (id: number) => {
    setExpandedId(expandedId === id ? null : id);
  };

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
            Research <span className="text-emerald-600 italic">Output</span>
          </h1>
          <p className="text-xl text-zinc-600 max-w-2xl">
            Selected publications, conference papers, and research manuscripts.
          </p>
        </div>

        {loading ? (
          <div className="flex justify-center py-20">
            <RefreshCw className="animate-spin text-emerald-600" size={32} />
          </div>
        ) : (
          <div className="space-y-8">
            {publications.map((pub, i) => (
              <motion.div
                key={pub.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5, delay: i * 0.1 }}
                className="group relative p-8 bg-white border border-zinc-100 rounded-none shadow-sm hover:shadow-md transition-all border-l-4 border-l-emerald-500"
              >
                <div className="flex flex-wrap items-center gap-3 mb-4">
                  <span className={`px-3 py-1 rounded-none text-xs font-bold uppercase tracking-wider ${
                    pub.status === 'Published' ? 'bg-emerald-100 text-emerald-700' : 'bg-amber-100 text-amber-700'
                  }`}>
                    {pub.status}
                  </span>
                  <span className="px-3 py-1 bg-zinc-100 text-zinc-600 rounded-none text-xs font-bold uppercase tracking-wider">
                    {pub.type}
                  </span>
                  <span className="flex items-center gap-1 text-zinc-400 text-xs font-medium ml-auto">
                    <Calendar size={14} /> {pub.year}
                  </span>
                </div>

                <h3 className="text-2xl font-bold text-zinc-900 mb-4 group-hover:text-emerald-600 transition-colors leading-tight">
                  {pub.title}
                </h3>

                <div className="space-y-4">
                  <div className="flex gap-2 text-zinc-600">
                    <User size={18} className="shrink-0 text-emerald-500 mt-1" />
                    <p className="text-sm italic">{pub.authors}</p>
                  </div>

                  <div className="flex gap-2 text-zinc-500">
                    <MapPin size={18} className="shrink-0 text-emerald-500 mt-1" />
                    <p className="text-sm">{pub.venue}</p>
                  </div>
                </div>

                <div className="mt-6 flex flex-wrap gap-4 pt-6 border-t border-zinc-50">
                  <button
                    onClick={() => toggleAbstract(pub.id)}
                    className="inline-flex items-center gap-2 text-zinc-600 font-bold hover:text-emerald-600 transition-colors text-sm"
                  >
                    {expandedId === pub.id ? (
                      <>Hide Abstract <ChevronUp size={16} /></>
                    ) : (
                      <>See Abstract <ChevronDown size={16} /></>
                    )}
                  </button>

                  {pub.link && (
                    <a
                      href={pub.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-2 text-emerald-600 font-bold hover:text-emerald-700 transition-colors text-sm"
                    >
                      View Publication <ExternalLink size={16} />
                    </a>
                  )}
                </div>

                <AnimatePresence>
                  {expandedId === pub.id && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3 }}
                      className="overflow-hidden"
                    >
                      <div className="mt-4 p-6 bg-zinc-50 border-l-2 border-emerald-200 text-zinc-600 text-sm leading-relaxed">
                        <p className="font-bold text-zinc-900 mb-2 uppercase tracking-wider text-xs">Abstract</p>
                        {pub.abstract || "Abstract not available for this publication."}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            ))}
          </div>
        )}
      </motion.div>
    </div>
  );
}
