// Simple JS for interactivity

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const menuBtn = document.getElementById('menu-btn');
  const mobileNav = document.getElementById('mobile-nav');

  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', () => {
      mobileNav.classList.toggle('hidden');
      menuBtn.textContent = mobileNav.classList.contains('hidden') ? 'MENU' : 'CLOSE';
    });
  }

  // Active link highlighting for Multi-Page Navigation
  const currentPath = window.location.pathname;
  document.querySelectorAll('nav a, #mobile-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    
    // Determine active path matching logic
    const isActive = href === currentPath || 
                     (currentPath === '/' && href === '/') || 
                     (currentPath.includes('index.html') && href === '/') ||
                     (href !== '/' && currentPath.includes(href));
                     
    if (isActive) {
      link.classList.add('bg-black', 'text-white');
    }
  });

  // Smooth scrolling for anchor links (if any stay on page)
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href')?.substring(1);
      if (!targetId || targetId === '') return;
      
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Abstract toggling
  const abstractToggles = document.querySelectorAll('.abstract-toggle');
  abstractToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const abstractId = toggle.getAttribute('data-abstract-id');
      const abstractContainer = document.getElementById(abstractId);
      
      if (abstractContainer) {
        abstractContainer.classList.toggle('hidden');
        
        // Optional: Update button text state if desired
        if (abstractContainer.classList.contains('hidden')) {
          toggle.classList.remove('bg-black', 'text-white');
        } else {
          toggle.classList.add('bg-black', 'text-white');
        }
      }
    });
  });
});
