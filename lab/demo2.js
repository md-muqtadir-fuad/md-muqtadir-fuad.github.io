/**
 * DEMO 2: SPATIAL WORKBENCH CONTROLLER
 * lab/demo2.js - Isolated JavaScript
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const viewport = document.getElementById('matViewport');
    const canvasPlane = document.getElementById('canvasPlane');
    if (!viewport || !canvasPlane) return;

    // Viewport transform state
    let panX = 150;
    let panY = 80;
    let zoom = 1.0;
    let isPanning = false;
    let startX = 0;
    let startY = 0;
    let highestZ = 10;

    function applyTransform() {
      canvasPlane.style.transform = `translate(${panX}px, ${panY}px) scale(${zoom})`;
    }
    applyTransform();

    // Pan Viewport by dragging on mat surface
    viewport.addEventListener('mousedown', (e) => {
      // If clicking directly on viewport or canvas plane (not cards)
      if (e.target === viewport || e.target === canvasPlane) {
        isPanning = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        viewport.classList.add('panning');
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (isPanning) {
        panX = e.clientX - startX;
        panY = e.clientY - startY;
        applyTransform();
      }
    });

    window.addEventListener('mouseup', () => {
      if (isPanning) {
        isPanning = false;
        viewport.classList.remove('panning');
      }
    });

    // Zoom via mouse wheel
    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = 1.1;
      if (e.deltaY < 0) {
        zoom = Math.min(2.0, zoom * zoomFactor);
      } else {
        zoom = Math.max(0.4, zoom / zoomFactor);
      }
      applyTransform();
    }, { passive: false });

    // Draggable Cards & Notes
    const draggables = document.querySelectorAll('.mat-draggable');
    draggables.forEach((el) => {
      let isDraggingCard = false;
      let cardStartX = 0;
      let cardStartY = 0;
      let elInitialLeft = 0;
      let elInitialTop = 0;

      el.addEventListener('mousedown', (e) => {
        // Prevent if clicking on an interactive link/button
        if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON') return;

        isDraggingCard = true;
        highestZ++;
        el.style.zIndex = highestZ;
        el.classList.add('is-dragging');

        cardStartX = e.clientX;
        cardStartY = e.clientY;
        elInitialLeft = parseFloat(el.style.left) || 0;
        elInitialTop = parseFloat(el.style.top) || 0;

        e.stopPropagation();
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDraggingCard) return;
        const dx = (e.clientX - cardStartX) / zoom;
        const dy = (e.clientY - cardStartY) / zoom;
        el.style.left = `${elInitialLeft + dx}px`;
        el.style.top = `${elInitialTop + dy}px`;
      });

      window.addEventListener('mouseup', () => {
        if (isDraggingCard) {
          isDraggingCard = false;
          el.classList.remove('is-dragging');
        }
      });
    });

    // Reset view button
    const btnReset = document.getElementById('btnResetView');
    if (btnReset) {
      btnReset.addEventListener('click', () => {
        panX = 100;
        panY = 60;
        zoom = 1.0;
        applyTransform();
      });
    }

    const btnZoomIn = document.getElementById('btnZoomIn');
    if (btnZoomIn) {
      btnZoomIn.addEventListener('click', () => {
        zoom = Math.min(2.0, zoom * 1.2);
        applyTransform();
      });
    }

    const btnZoomOut = document.getElementById('btnZoomOut');
    if (btnZoomOut) {
      btnZoomOut.addEventListener('click', () => {
        zoom = Math.max(0.4, zoom / 1.2);
        applyTransform();
      });
    }
  });
})();
