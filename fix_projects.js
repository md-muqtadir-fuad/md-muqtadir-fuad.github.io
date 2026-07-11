const fs = require('fs');
let html = fs.readFileSync('projects.html', 'utf8');

const replacements = [
  {
    target: '<a href="https://github.com/md-muqtadir-fuad/iot-conveyor-belt"\n              class="font-mono text-sm uppercase tracking-wider">View Source &rarr;</a>',
    link: '/blog-iot-conveyor.html'
  },
  {
    target: '<a href="https://github.com/md-muqtadir-fuad/badhan-web-automation"\n              class="font-mono text-sm uppercase tracking-wider">View Source &rarr;</a>',
    link: '/blog-badhan.html'
  },
  {
    target: '<a href="https://github.com/md-muqtadir-fuad/iot-web-platform"\n              class="font-mono text-sm uppercase tracking-wider">View Source &rarr;</a>',
    link: '/blog-iot-platform.html'
  },
  {
    target: '<a href="https://github.com/md-muqtadir-fuad/BNWP-WikiConnect-Theme"\n              class="font-mono text-sm uppercase tracking-wider">View Source &rarr;</a>',
    link: '/blog-bnwp.html'
  },
  {
    target: '<a href="https://github.com/md-muqtadir-fuad/Shoe-Shiner-Pro"\n              class="font-mono text-sm uppercase tracking-wider">View Source &rarr;</a>',
    link: '/blog-shoe-shiner.html'
  }
];

replacements.forEach(r => {
  const replacement = `<div class="flex flex-wrap gap-4">
              \${r.target.replace('class="font-mono', 'class="font-mono text-sm uppercase tracking-wider hover:underline"').replace('">View Source', '">View Source')}
              <a href="\${r.link}" class="font-mono text-sm uppercase tracking-wider hover:underline">Read Blog &rarr;</a>
            </div>`;
  html = html.replace(r.target, replacement);
});

fs.writeFileSync('projects.html', html);
console.log('Projects fixed');
