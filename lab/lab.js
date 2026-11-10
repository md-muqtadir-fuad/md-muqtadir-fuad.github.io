/**
 * MY WORKSPACE // EDITORIAL ARCHITECTURAL PARTITIONS
 * lab/demo1.js - Isolated Interactive Controller
 */

(function () {
  'use strict';

  // 1. Live BST Clock
  const clockEl = document.getElementById('liveClock');
  function updateClock() {
    if (!clockEl) return;
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    clockEl.textContent = `${h}:${m}:${s} BST`;
  }
  updateClock();
  setInterval(updateClock, 1000);

  // 2. Drawer Accordion Interaction
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

  // 3. Left sidebar trigger for Completed Projects
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
