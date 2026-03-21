import React, { useState, useEffect } from "react";
import { motion } from "motion/react";
import { auth, db } from "../firebase";
import { onAuthStateChanged, User } from "firebase/auth";
import { collection, addDoc, getDocs, doc, getDoc, setDoc, query, where } from "firebase/firestore";
import { publicationsData } from "../data/publicationsData";
import { projectsData } from "../data/projectsData";
import { Plus, RefreshCw, Check, AlertCircle, Trash2, LayoutDashboard, FileText, Briefcase } from "lucide-react";

export default function Admin() {
  const [user, setUser] = useState<User | null>(null);
  const [isAdmin, setIsAdmin] = useState(false);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (currentUser) => {
      setUser(currentUser);
      if (currentUser) {
        // Check if user is admin in Firestore
        const userDoc = await getDoc(doc(db, "users", currentUser.uid));
        if (userDoc.exists() && userDoc.data().role === "admin") {
          setIsAdmin(true);
        } else if (currentUser.email === "mmfuad01@gmail.com") {
          // Fallback for the main user if doc doesn't exist yet
          setIsAdmin(true);
        } else {
          setIsAdmin(false);
        }
      } else {
        setIsAdmin(false);
      }
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  const syncData = async () => {
    setSyncing(true);
    setMessage(null);
    try {
      // Sync Publications
      for (const pub of publicationsData) {
        const pubRef = doc(db, "publications", pub.id.toString());
        await setDoc(pubRef, { ...pub, createdAt: new Date().toISOString() }, { merge: true });
      }

      // Sync Projects
      for (const project of projectsData) {
        const projectRef = doc(db, "projects", project.id.toString());
        await setDoc(projectRef, { ...project, createdAt: new Date().toISOString() }, { merge: true });
      }

      setMessage({ text: "Data synced successfully to Firestore!", type: 'success' });
    } catch (error) {
      console.error("Sync error:", error);
      setMessage({ text: "Failed to sync data. Check console for details.", type: 'error' });
    } finally {
      setSyncing(false);
    }
  };

  if (loading) {
    return (
      <div className="pt-32 flex justify-center">
        <RefreshCw className="animate-spin text-emerald-600" size={32} />
      </div>
    );
  }

  if (!isAdmin) {
    return (
      <div className="pt-32 pb-16 px-4 text-center space-y-8">
        <AlertCircle className="mx-auto text-red-500" size={64} />
        <h1 className="text-4xl font-bold font-display">Access Denied</h1>
        <p className="text-zinc-600">You do not have permission to access the admin dashboard.</p>
      </div>
    );
  }

  return (
    <div className="pt-32 pb-16 px-4 max-w-5xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="space-y-12"
      >
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <h1 className="text-4xl font-bold font-display flex items-center gap-3">
              <LayoutDashboard className="text-emerald-600" /> Admin Dashboard
            </h1>
            <p className="text-zinc-600">Manage your portfolio content and sync data.</p>
          </div>
          
          <button
            onClick={syncData}
            disabled={syncing}
            className="flex items-center gap-2 px-6 py-3 bg-emerald-600 text-white rounded-none font-bold hover:bg-emerald-700 transition-colors disabled:opacity-50"
          >
            {syncing ? <RefreshCw className="animate-spin" size={18} /> : <Check size={18} />}
            {syncing ? "Syncing..." : "Sync Initial Data"}
          </button>
        </div>

        {message && (
          <div className={`p-4 rounded-none flex items-center gap-3 ${
            message.type === 'success' ? 'bg-emerald-50 text-emerald-700 border border-emerald-100' : 'bg-red-50 text-red-700 border border-red-100'
          }`}>
            {message.type === 'success' ? <Check size={20} /> : <AlertCircle size={20} />}
            <p className="font-medium">{message.text}</p>
          </div>
        )}

        <div className="grid md:grid-cols-2 gap-8">
          <AdminCard 
            title="Publications" 
            icon={<FileText />} 
            description="Add or edit research papers and posters."
            link="/publications"
          />
          <AdminCard 
            title="Projects" 
            icon={<Briefcase />} 
            description="Manage your engineering and AI projects."
            link="/projects"
          />
        </div>

        <section className="space-y-6 pt-12 border-t border-zinc-100">
          <h2 className="text-2xl font-bold font-display">Quick Add Publication</h2>
          <AddPublicationForm />
        </section>
      </motion.div>
    </div>
  );
}

function AdminCard({ title, icon, description, link }: { title: string; icon: React.ReactNode; description: string; link: string }) {
  return (
    <div className="p-8 bg-white border border-zinc-100 rounded-none shadow-sm space-y-4">
      <div className="w-12 h-12 bg-emerald-50 text-emerald-600 flex items-center justify-center rounded-none">
        {icon}
      </div>
      <h3 className="text-xl font-bold font-display">{title}</h3>
      <p className="text-zinc-600 text-sm">{description}</p>
      <a href={link} className="inline-block text-emerald-600 font-bold text-sm hover:underline">
        View Live {title}
      </a>
    </div>
  );
}

function AddPublicationForm() {
  const [form, setForm] = useState({
    title: "",
    authors: "",
    venue: "",
    year: new Date().getFullYear().toString(),
    status: "Published",
    type: "Conference Paper",
    link: "",
    abstract: ""
  });
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setSuccess(false);
    try {
      const id = Date.now();
      await setDoc(doc(db, "publications", id.toString()), {
        ...form,
        id,
        createdAt: new Date().toISOString()
      });
      setSuccess(true);
      setForm({
        title: "",
        authors: "",
        venue: "",
        year: new Date().getFullYear().toString(),
        status: "Published",
        type: "Conference Paper",
        link: "",
        abstract: ""
      });
    } catch (error) {
      console.error("Add publication error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="grid gap-6 p-8 bg-zinc-50 border border-zinc-100 rounded-none">
      <div className="grid md:grid-cols-2 gap-6">
        <div className="space-y-2">
          <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Title</label>
          <input 
            required
            value={form.title}
            onChange={e => setForm({...form, title: e.target.value})}
            className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
            placeholder="Paper Title"
          />
        </div>
        <div className="space-y-2">
          <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Authors</label>
          <input 
            required
            value={form.authors}
            onChange={e => setForm({...form, authors: e.target.value})}
            className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
            placeholder="Authors (comma separated)"
          />
        </div>
      </div>

      <div className="grid md:grid-cols-3 gap-6">
        <div className="space-y-2">
          <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Venue</label>
          <input 
            required
            value={form.venue}
            onChange={e => setForm({...form, venue: e.target.value})}
            className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
            placeholder="Conference/Journal"
          />
        </div>
        <div className="space-y-2">
          <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Year</label>
          <input 
            required
            value={form.year}
            onChange={e => setForm({...form, year: e.target.value})}
            className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
            placeholder="2025"
          />
        </div>
        <div className="space-y-2">
          <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Status</label>
          <select 
            value={form.status}
            onChange={e => setForm({...form, status: e.target.value})}
            className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
          >
            <option>Published</option>
            <option>Under Review</option>
            <option>Poster</option>
          </select>
        </div>
      </div>

      <div className="space-y-2">
        <label className="text-xs font-bold uppercase tracking-wider text-zinc-500">Abstract</label>
        <textarea 
          rows={4}
          value={form.abstract}
          onChange={e => setForm({...form, abstract: e.target.value})}
          className="w-full px-4 py-3 bg-white border border-zinc-200 rounded-none focus:ring-2 focus:ring-emerald-500 outline-none"
          placeholder="Brief summary of the research..."
        />
      </div>

      <div className="flex items-center justify-between">
        {success && <p className="text-emerald-600 font-bold text-sm">Publication added successfully!</p>}
        <button
          type="submit"
          disabled={loading}
          className="ml-auto px-8 py-3 bg-zinc-900 text-white rounded-none font-bold hover:bg-emerald-600 transition-colors flex items-center gap-2"
        >
          {loading ? <RefreshCw className="animate-spin" size={18} /> : <Plus size={18} />}
          Add Publication
        </button>
      </div>
    </form>
  );
}
