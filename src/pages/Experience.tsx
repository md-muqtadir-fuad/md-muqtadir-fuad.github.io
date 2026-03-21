import { motion } from "motion/react";
import { experienceData } from "../data/experienceData";
import { Briefcase, Users, Trophy, ExternalLink, MapPin, Calendar } from "lucide-react";

export default function Experience() {
  return (
    <div className="pt-32 pb-16 px-4 max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="space-y-24"
      >
        {/* Work Experience */}
        <section className="space-y-12">
          <div className="space-y-4">
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-zinc-900 font-display">
              Professional <span className="text-emerald-600 italic">Journey</span>
            </h1>
            <p className="text-xl text-zinc-600 max-w-2xl">
              Gaining hands-on experience in industrial engineering and academic research.
            </p>
          </div>

          <div className="space-y-12">
            {experienceData.work.map((item, i) => (
              <div key={i} className="group relative grid md:grid-cols-4 gap-8 p-8 bg-white border border-zinc-100 rounded-3xl shadow-sm hover:shadow-md transition-all">
                <div className="md:col-span-1 space-y-2">
                  <div className="text-emerald-600 font-bold flex items-center gap-2">
                    <Calendar size={16} /> {item.period}
                  </div>
                  <div className="text-zinc-400 text-sm flex items-center gap-2">
                    <MapPin size={16} /> {item.location}
                  </div>
                </div>
                <div className="md:col-span-3 space-y-4">
                  <h3 className="text-2xl font-bold text-zinc-900 group-hover:text-emerald-600 transition-colors">
                    {item.title}
                  </h3>
                  <p className="text-lg font-medium text-zinc-700">{item.organization}</p>
                  <ul className="space-y-3">
                    {item.bullets.map((bullet, j) => (
                      <li key={j} className="text-zinc-600 flex gap-3">
                        <div className="w-1.5 h-1.5 rounded-full bg-emerald-500 mt-2.5 shrink-0" />
                        {bullet}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Leadership & Service */}
        <section className="space-y-12">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <Users className="text-emerald-600" /> Leadership & Service
          </h2>
          <div className="grid md:grid-cols-2 gap-6">
            {experienceData.leadership.map((item, i) => (
              <div key={i} className="p-6 bg-zinc-50 rounded-3xl border border-zinc-100 space-y-4">
                <div className="space-y-1">
                  <h3 className="text-xl font-bold text-zinc-900">{item.title}</h3>
                  <p className="text-emerald-600 font-medium">{item.organization}</p>
                </div>
                <div className="flex items-center justify-between text-sm text-zinc-500">
                  <span>{item.period}</span>
                  <span>{item.location}</span>
                </div>
                <ul className="space-y-2">
                  {item.bullets.map((bullet, j) => (
                    <li key={j} className="text-sm text-zinc-600 flex gap-2">
                      <div className="w-1 h-1 rounded-full bg-emerald-400 mt-2 shrink-0" />
                      {bullet}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>

        {/* Competitions */}
        <section className="space-y-12">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <Trophy className="text-emerald-600" /> Competitions & Hackathons
          </h2>
          <div className="space-y-6">
            {experienceData.competitions.map((item, i) => (
              <div key={i} className="p-8 bg-emerald-900 text-white rounded-3xl space-y-6">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                  <div className="space-y-1">
                    <h3 className="text-2xl font-bold">{item.title}</h3>
                    <p className="text-emerald-300 font-medium">{item.organization}</p>
                  </div>
                  {item.link && (
                    <a
                      href={item.link.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-2 px-4 py-2 bg-white/10 rounded-full text-sm hover:bg-white/20 transition-colors"
                    >
                      {item.link.label} <ExternalLink size={14} />
                    </a>
                  )}
                </div>
                <ul className="grid md:grid-cols-2 gap-4">
                  {item.bullets.map((bullet, j) => (
                    <li key={j} className="text-emerald-100/80 flex gap-3 text-sm">
                      <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 shrink-0" />
                      {bullet}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>
      </motion.div>
    </div>
  );
}
