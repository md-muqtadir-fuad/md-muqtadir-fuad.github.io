import { Link } from "react-router-dom";
import { motion } from "motion/react";
import { Menu, X, LogIn, LogOut, User as UserIcon } from "lucide-react";
import { useState, useEffect } from "react";
import { auth, db } from "../firebase";
import { signInWithPopup, GoogleAuthProvider, signOut, onAuthStateChanged, User } from "firebase/auth";
import { doc, getDoc } from "firebase/firestore";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [user, setUser] = useState<User | null>(null);
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (currentUser) => {
      setUser(currentUser);
      if (currentUser) {
        // Check if user is admin
        const userDoc = await getDoc(doc(db, "users", currentUser.uid));
        if (userDoc.exists() && userDoc.data().role === "admin") {
          setIsAdmin(true);
        } else if (currentUser.email === "mmfuad01@gmail.com") {
          setIsAdmin(true);
        } else {
          setIsAdmin(false);
        }
      } else {
        setIsAdmin(false);
      }
    });
    return () => unsubscribe();
  }, []);

  const handleLogin = async () => {
    const provider = new GoogleAuthProvider();
    try {
      await signInWithPopup(auth, provider);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const handleLogout = async () => {
    try {
      await signOut(auth);
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  const navLinks = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about" },
    { name: "Projects", path: "/projects" },
    { name: "Experience", path: "/experience" },
    { name: "Publications", path: "/publications" },
    { name: "Contact", path: "/contact" },
    ...(isAdmin ? [{ name: "Admin", path: "/admin" }] : []),
  ];

  return (
    <nav className="fixed w-full z-50 bg-white/80 backdrop-blur-md border-b border-black/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <Link to="/" className="text-xl font-bold tracking-tight font-display">
            MUQTADIR <span className="text-emerald-600">FUAD</span>
          </Link>

          {/* Desktop Nav */}
          <div className="hidden md:flex items-center space-x-8">
            {navLinks.map((link) => (
              <Link
                key={link.name}
                to={link.path}
                className="text-sm font-medium text-zinc-600 hover:text-emerald-600 transition-colors"
              >
                {link.name}
              </Link>
            ))}
            
            {user ? (
              <div className="flex items-center gap-4 pl-4 border-l border-black/5">
                <div className="flex items-center gap-2">
                  {user.photoURL ? (
                    <img src={user.photoURL} alt={user.displayName || ""} className="w-8 h-8 rounded-full border border-black/5" referrerPolicy="no-referrer" />
                  ) : (
                    <div className="w-8 h-8 rounded-full bg-zinc-100 flex items-center justify-center text-zinc-400">
                      <UserIcon size={16} />
                    </div>
                  )}
                </div>
                <button
                  onClick={handleLogout}
                  className="text-sm font-medium text-zinc-600 hover:text-red-600 transition-colors flex items-center gap-1"
                >
                  <LogOut size={16} /> Logout
                </button>
              </div>
            ) : (
              <button
                onClick={handleLogin}
                className="px-4 py-1.5 bg-zinc-900 text-white text-sm font-medium rounded-full hover:bg-zinc-800 transition-colors flex items-center gap-2"
              >
                <LogIn size={16} /> Login
              </button>
            )}
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center gap-4">
            {user && user.photoURL && (
              <img src={user.photoURL} alt={user.displayName || ""} className="w-8 h-8 rounded-full border border-black/5" referrerPolicy="no-referrer" />
            )}
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="p-2 text-zinc-600 hover:text-emerald-600"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Nav */}
      {isOpen && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="md:hidden bg-white border-b border-black/5 px-4 pt-2 pb-6 space-y-1"
        >
          {navLinks.map((link) => (
            <Link
              key={link.name}
              to={link.path}
              onClick={() => setIsOpen(false)}
              className="block px-3 py-2 text-base font-medium text-zinc-600 hover:text-emerald-600 hover:bg-zinc-50 rounded-md"
            >
              {link.name}
            </Link>
          ))}
          <div className="pt-4 mt-4 border-t border-black/5">
            {user ? (
              <button
                onClick={() => { handleLogout(); setIsOpen(false); }}
                className="w-full text-left px-3 py-2 text-base font-medium text-red-600 hover:bg-red-50 rounded-md flex items-center gap-2"
              >
                <LogOut size={20} /> Logout
              </button>
            ) : (
              <button
                onClick={() => { handleLogin(); setIsOpen(false); }}
                className="w-full text-left px-3 py-2 text-base font-medium text-emerald-600 hover:bg-emerald-50 rounded-md flex items-center gap-2"
              >
                <LogIn size={20} /> Login with Google
              </button>
            )}
          </div>
        </motion.div>
      )}
    </nav>
  );
}
