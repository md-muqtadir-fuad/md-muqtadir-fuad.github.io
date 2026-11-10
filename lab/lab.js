// Workspace page: clock and drawer accordion. Used only by lab/lab.html.

(function () {
  'use strict';

  // Clock in the visitor's local time
  const clockEl = document.getElementById('liveClock');
  function updateClock() {
    if (!clockEl) return;
    clockEl.textContent = new Date().toLocaleTimeString('en-GB', { hour12: false });
  }
  updateClock();
  setInterval(updateClock, 1000);

  // Drawer accordion: one drawer open at a time
  const drawers = Array.from(document.querySelectorAll('.drawer-section'));

  function expandDrawer(drawerNameOrEl) {
    const target = typeof drawerNameOrEl === 'string'
      ? drawers.find((d) => d.dataset.drawer === drawerNameOrEl)
      : drawerNameOrEl;

    if (!target || target.classList.contains('expanded')) return;

    drawers.forEach((other) => {
      if (other !== target) {
        other.classList.remove('expanded');
        other.classList.add('collapsed');
      }
    });

    target.classList.remove('collapsed');
    target.classList.add('expanded');
  }

  drawers.forEach((drawer) => {
    const tab = drawer.querySelector('.drawer-tab');
    if (!tab) return;
    tab.addEventListener('click', () => expandDrawer(drawer));
  });

  // "Completed projects" link in the left column toggles that drawer
  const linkCompleted = document.getElementById('linkCompletedProjects');
  if (linkCompleted) {
    linkCompleted.addEventListener('click', (e) => {
      e.preventDefault();
      const completedDrawer = drawers.find((d) => d.dataset.drawer === 'completed');
      if (completedDrawer && completedDrawer.classList.contains('expanded')) {
        expandDrawer('ongoing');
      } else {
        expandDrawer('completed');
      }
    });
  }

})();
