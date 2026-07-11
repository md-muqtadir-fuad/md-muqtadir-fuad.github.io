import tailwindcss from '@tailwindcss/vite';
import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    plugins: [tailwindcss()],
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
          blogs: path.resolve(__dirname, 'blogs.html'),
          '404': path.resolve(__dirname, '404.html'),
          'blog-badhan': path.resolve(__dirname, 'blog-badhan.html'),
          'blog-bezierlab': path.resolve(__dirname, 'blog-bezierlab.html'),
          'blog-bnwp': path.resolve(__dirname, 'blog-bnwp.html'),
          'blog-dengue': path.resolve(__dirname, 'blog-dengue.html'),
          'blog-egov-lens': path.resolve(__dirname, 'blog-egov-lens.html'),
          'blog-iot-conveyor': path.resolve(__dirname, 'blog-iot-conveyor.html'),
          'blog-iot-platform': path.resolve(__dirname, 'blog-iot-platform.html'),
          'blog-querynest': path.resolve(__dirname, 'blog-querynest.html'),
          'blog-shoe-shiner': path.resolve(__dirname, 'blog-shoe-shiner.html'),
        },
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});