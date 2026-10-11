import tailwindcss from '@tailwindcss/vite';
import fs from 'fs';
import path from 'path';
import {defineConfig} from 'vite';

function getBlogInputs() {
  const postsDir = path.resolve(__dirname, 'blogs-posts/posts');
  const blogInputs: Record<string, string> = {};
  if (fs.existsSync(postsDir)) {
    const files = fs.readdirSync(postsDir);
    for (const file of files) {
      if (file.endsWith('.html')) {
        const name = file.replace(/\.html$/, '');
        blogInputs[name] = path.resolve(postsDir, file);
      }
    }
  }
  return blogInputs;
}

function markdownWatcherPlugin() {
  return {
    name: 'vite-plugin-markdown-blogs',
    configureServer(server: any) {
      const contentDir = path.resolve(__dirname, 'blogs-posts/content');
      // Home page sections generated from content/*.md. Import paths must stay literal so Vite can resolve them.
      const homeSections: Record<string, () => Promise<void>> = {
        [path.resolve(__dirname, 'content/updates.md')]: () => import('./scripts/build-updates.js').then(m => m.buildUpdates()),
        [path.resolve(__dirname, 'content/publications.md')]: () => import('./scripts/build-publications.js').then(m => m.buildPublications()),
      };
      server.watcher.add([contentDir, ...Object.keys(homeSections)]);

      const handleChange = async (file: string) => {
        const basename = path.basename(file).toLowerCase();
        const homeSection = homeSections[path.resolve(file)];
        if (homeSection) {
          console.log(`[markdown-watcher] Detected change in ${path.basename(file)}, rebuilding home page section...`);
          try {
            await homeSection();
            server.ws.send({ type: 'full-reload' });
          } catch (err) {
            console.error(`[markdown-watcher] Error rebuilding ${path.basename(file)}:`, err);
          }
          return;
        }
        if (file.endsWith('.md') && !basename.startsWith('_') && basename !== 'readme.md' && basename !== 'template.md') {
          console.log(`[markdown-watcher] Detected change in ${path.basename(file)}, rebuilding blogs...`);
          try {
            const { buildBlogs } = await import('./scripts/build-blogs.js');
            buildBlogs();
            server.ws.send({ type: 'full-reload' });
          } catch (err) {
            console.error('[markdown-watcher] Error rebuilding blogs:', err);
          }
        }
      };

      server.watcher.on('add', handleChange);
      server.watcher.on('change', handleChange);
      server.watcher.on('unlink', handleChange);
    },
  };
}

export default defineConfig(() => {
  return {
    plugins: [tailwindcss(), markdownWatcherPlugin()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          experience: path.resolve(__dirname, 'experience.html'),
          projects: path.resolve(__dirname, 'projects.html'),
          publications: path.resolve(__dirname, 'publications.html'),
          achievements: path.resolve(__dirname, 'achievements.html'),
          contacts: path.resolve(__dirname, 'contacts.html'),
          blogs: path.resolve(__dirname, 'blogs-posts/blogs.html'),
          '404': path.resolve(__dirname, '404.html'),
          ...getBlogInputs(),
        },
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});