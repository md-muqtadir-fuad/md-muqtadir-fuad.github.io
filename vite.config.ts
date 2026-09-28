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
          blogs: path.resolve(__dirname, 'blogs-posts/blogs.html'),
          '404': path.resolve(__dirname, '404.html'),
          'blog-badhan': path.resolve(__dirname, 'blogs-posts/posts/blog-badhan.html'),
          'blog-bezierlab': path.resolve(__dirname, 'blogs-posts/posts/blog-bezierlab.html'),
          'blog-bnwp': path.resolve(__dirname, 'blogs-posts/posts/blog-bnwp.html'),
          'blog-dengue': path.resolve(__dirname, 'blogs-posts/posts/blog-dengue.html'),
          'blog-egov-lens': path.resolve(__dirname, 'blogs-posts/posts/blog-egov-lens.html'),
          'blog-iot-conveyor': path.resolve(__dirname, 'blogs-posts/posts/blog-iot-conveyor.html'),
          'blog-iot-platform': path.resolve(__dirname, 'blogs-posts/posts/blog-iot-platform.html'),
          'blog-querynest': path.resolve(__dirname, 'blogs-posts/posts/blog-querynest.html'),
          'blog-shoe-shiner': path.resolve(__dirname, 'blogs-posts/posts/blog-shoe-shiner.html'),
          'blog-semi-automated-shoe-cleaning-machine': path.resolve(__dirname, 'blogs-posts/posts/blog-semi-automated-shoe-cleaning-machine.html'),
          'blog-scientific-figures-tools': path.resolve(__dirname, 'blogs-posts/posts/blog-scientific-figures-tools.html'),
          'blog-ug-thesis': path.resolve(__dirname, 'blogs-posts/posts/blog-ug-thesis.html'),
        },
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});