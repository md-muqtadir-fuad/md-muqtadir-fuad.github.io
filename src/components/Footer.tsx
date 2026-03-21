import { Github, Linkedin, Twitter, Mail } from "lucide-react";

export default function Footer() {
  const socialLinks = [
    { name: "GitHub", icon: <Github size={20} />, url: "https://github.com/md-muqtadir-fuad" },
    { name: "LinkedIn", icon: <Linkedin size={20} />, url: "https://linkedin.com/in/md-muqtadir-fuad" },
    { name: "Twitter", icon: <Twitter size={20} />, url: "https://twitter.com/muqtadir_fuad" },
    { name: "Email", icon: <Mail size={20} />, url: "mailto:mmfuad01@gmail.com" },
  ];

  return (
    <footer className="bg-zinc-50 border-t border-black/5 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center space-y-6 md:space-y-0">
          <div className="text-center md:text-left">
            <h3 className="text-lg font-bold tracking-tight">
              MUQTADIR <span className="text-emerald-600">FUAD</span>
            </h3>
            <p className="text-sm text-zinc-500 mt-1">
              Building the future with code and creativity.
            </p>
          </div>

          <div className="flex space-x-6">
            {socialLinks.map((link) => (
              <a
                key={link.name}
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-zinc-400 hover:text-emerald-600 transition-colors"
                aria-label={link.name}
              >
                {link.icon}
              </a>
            ))}
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-black/5 text-center">
          <p className="text-xs text-zinc-400">
            &copy; {new Date().getFullYear()} Md. Muqtadir Fuad. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
