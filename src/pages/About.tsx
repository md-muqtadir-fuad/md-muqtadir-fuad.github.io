import { motion } from "motion/react";
import { aboutData } from "../data/aboutData";
import { siteContent } from "../constants";
import { GraduationCap, Briefcase, Award, Code, Globe, FileText, Github, Linkedin } from "lucide-react";

export default function About() {
  return (
    <div className="pt-32 pb-16 px-4 max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="space-y-16"
      >
        {/* Header Section */}
        <section className="space-y-8">
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-zinc-900 font-display">
            About <span className="text-emerald-600 italic">Me</span>
          </h1>
          <div className="grid md:grid-cols-3 gap-12">
            <div className="md:col-span-2 space-y-6 text-lg text-zinc-600 leading-relaxed">
              {aboutData.summary.map((para, i) => (
                <p key={i}>{para}</p>
              ))}
              <div className="flex flex-wrap gap-4 pt-4">
                <a
                  href={siteContent.links.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 px-4 py-2 bg-zinc-100 rounded-full text-sm font-medium hover:bg-zinc-200 transition-colors"
                >
                  <Github size={16} /> GitHub
                </a>
                <a
                  href={siteContent.links.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 px-4 py-2 bg-zinc-100 rounded-full text-sm font-medium hover:bg-zinc-200 transition-colors"
                >
                  <Linkedin size={16} /> LinkedIn
                </a>
                <a
                  href={siteContent.links.orcid}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 px-4 py-2 bg-zinc-100 rounded-full text-sm font-medium hover:bg-zinc-200 transition-colors"
                >
                  <Globe size={16} /> ORCID
                </a>
              </div>
            </div>
            <div className="space-y-8">
              <div className="p-6 bg-emerald-50 rounded-3xl border border-emerald-100">
                <h3 className="text-emerald-900 font-bold mb-4 flex items-center gap-2">
                  <FileText size={20} /> Quick Info
                </h3>
                <ul className="space-y-3 text-sm text-emerald-800">
                  <li><span className="font-semibold">Location:</span> {siteContent.location}</li>
                  <li><span className="font-semibold">Email:</span> {siteContent.email}</li>
                  <li><span className="font-semibold">Status:</span> {siteContent.shortTitle}</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* Research Interests */}
        <section className="space-y-8">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <Globe className="text-emerald-600" /> Research Interests
          </h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {aboutData.researchInterests.map((interest, i) => (
              <div key={i} className="p-4 bg-white border border-zinc-100 rounded-2xl shadow-sm hover:border-emerald-200 transition-colors">
                <p className="text-zinc-700 text-sm">{interest}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Education */}
        <section className="space-y-8">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <GraduationCap className="text-emerald-600" /> Education
          </h2>
          <div className="space-y-8">
            {aboutData.education.map((edu, i) => (
              <div key={i} className="relative pl-8 border-l-2 border-emerald-100 space-y-2">
                <div className="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-emerald-500 border-4 border-white shadow-sm" />
                <h3 className="text-xl font-bold text-zinc-900">{edu.degree}</h3>
                <p className="text-emerald-600 font-medium">{edu.institution}</p>
                <div className="flex items-center gap-4 text-sm text-zinc-500">
                  <span>{edu.location}</span>
                  <span>•</span>
                  <span>{edu.period}</span>
                </div>
                <p className="text-sm text-zinc-600 pt-2">
                  <span className="font-semibold">Coursework:</span> {edu.coursework.join(', ')}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* Skills */}
        <section className="space-y-8">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <Code className="text-emerald-600" /> Skills
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {aboutData.skills.map((group, i) => (
              <div key={i} className="space-y-3">
                <h3 className="font-bold text-zinc-900 text-sm uppercase tracking-wider">{group.title}</h3>
                <div className="flex flex-wrap gap-2">
                  {group.items.map((skill, j) => (
                    <span key={j} className="px-3 py-1 bg-zinc-50 text-zinc-600 rounded-lg text-xs border border-zinc-100">
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Awards */}
        <section className="space-y-8">
          <h2 className="text-3xl font-bold font-display flex items-center gap-3">
            <Award className="text-emerald-600" /> Honors & Awards
          </h2>
          <div className="space-y-4">
            {aboutData.awards.map((award, i) => (
              <div key={i} className="flex gap-4 p-4 bg-zinc-50 rounded-2xl border border-zinc-100">
                <div className="w-10 h-10 rounded-full bg-emerald-100 flex items-center justify-center shrink-0">
                  <Award className="text-emerald-600" size={20} />
                </div>
                <p className="text-zinc-700">{award}</p>
              </div>
            ))}
          </div>
        </section>
      </motion.div>
    </div>
  );
}
