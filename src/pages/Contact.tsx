import { motion } from "motion/react";
import { Mail, MapPin, Send, Github, Linkedin, Globe } from "lucide-react";
import { siteContent } from "../constants";

export default function Contact() {
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
            Let's <span className="text-emerald-600 italic">Connect</span>
          </h1>
          <p className="text-xl text-zinc-600 max-w-2xl">
            Have a question or want to collaborate? Feel free to reach out.
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-16">
          <div className="space-y-12">
            <div className="space-y-8">
              <div className="flex gap-6">
                <div className="w-14 h-14 rounded-2xl bg-emerald-100 flex items-center justify-center shrink-0">
                  <Mail className="text-emerald-600" size={28} />
                </div>
                <div className="space-y-1">
                  <h3 className="text-sm font-bold text-zinc-400 uppercase tracking-widest">Email</h3>
                  <a href={`mailto:${siteContent.email}`} className="text-2xl font-bold text-zinc-900 hover:text-emerald-600 transition-colors">
                    {siteContent.email}
                  </a>
                </div>
              </div>

              <div className="flex gap-6">
                <div className="w-14 h-14 rounded-2xl bg-emerald-100 flex items-center justify-center shrink-0">
                  <MapPin className="text-emerald-600" size={28} />
                </div>
                <div className="space-y-1">
                  <h3 className="text-sm font-bold text-zinc-400 uppercase tracking-widest">Location</h3>
                  <p className="text-2xl font-bold text-zinc-900">{siteContent.location}</p>
                </div>
              </div>
            </div>

            <div className="space-y-6">
              <h3 className="text-sm font-bold text-zinc-400 uppercase tracking-widest">Socials</h3>
              <div className="flex gap-4">
                {[
                  { icon: <Github />, url: siteContent.links.github, label: "GitHub" },
                  { icon: <Linkedin />, url: siteContent.links.linkedin, label: "LinkedIn" },
                  { icon: <Globe />, url: siteContent.links.orcid, label: "ORCID" },
                ].map((social) => (
                  <a
                    key={social.label}
                    href={social.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-12 h-12 rounded-xl border border-zinc-200 flex items-center justify-center text-zinc-600 hover:bg-emerald-600 hover:text-white hover:border-emerald-600 transition-all"
                  >
                    {social.icon}
                  </a>
                ))}
              </div>
            </div>
          </div>

          <form className="p-8 bg-zinc-50 rounded-[2.5rem] border border-zinc-100 space-y-6">
            <div className="space-y-2">
              <label className="text-sm font-bold text-zinc-500 ml-2">Name</label>
              <input
                type="text"
                placeholder="Your Name"
                className="w-full px-6 py-4 bg-white border border-zinc-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-bold text-zinc-500 ml-2">Email</label>
              <input
                type="email"
                placeholder="your@email.com"
                className="w-full px-6 py-4 bg-white border border-zinc-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-bold text-zinc-500 ml-2">Message</label>
              <textarea
                rows={4}
                placeholder="How can I help you?"
                className="w-full px-6 py-4 bg-white border border-zinc-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all resize-none"
              />
            </div>
            <button
              type="submit"
              className="w-full py-4 bg-emerald-600 text-white rounded-2xl font-bold hover:bg-emerald-700 transition-all flex items-center justify-center gap-2"
            >
              Send Message <Send size={18} />
            </button>
          </form>
        </div>
      </motion.div>
    </div>
  );
}
