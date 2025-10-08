// ...existing code...
document.addEventListener('DOMContentLoaded', () => {
  const navCollapse = document.getElementById('navbarNavAltMarkup');
  if (!navCollapse) return;

  // Ensure we have a Collapse instance (no toggle on init)
  const collapseInstance = bootstrap.Collapse.getOrCreateInstance(navCollapse, { toggle: false });

  // Hide navbar collapse when user scrolls
  window.addEventListener('scroll', () => {
    if (navCollapse.classList.contains('show')) {
      collapseInstance.hide();
    }
  }, { passive: true });
});
// ...existing code...