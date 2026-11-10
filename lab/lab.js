/**
 * ==============================================================================
 * SYNAPSE LAB // SPATIAL CUTTING MAT & PROTOTYPING WORKBENCH
 * lab/lab.js - Isolated Interactive Controller for /lab/lab.html
 * ==============================================================================
 */

(function () {
  'use strict';

  // DOM Elements
  const viewport = document.getElementById('matViewport');
  const plane = document.getElementById('matPlane');
  const rulerTopCanvas = document.getElementById('rulerTopCanvas');
  const rulerLeftCanvas = document.getElementById('rulerLeftCanvas');
  const deskCoordsEl = document.getElementById('deskCoords');
  const deskZoomEl = document.getElementById('deskZoom');

  const btnAutoArrange = document.getElementById('btnAutoArrange');
  const btnCenterDesk = document.getElementById('btnCenterDesk');
  const btnZoomIn = document.getElementById('btnZoomIn');
  const btnZoomOut = document.getElementById('btnZoomOut');
  const btnZoomReset = document.getElementById('btnZoomReset');

  // Camera State
  let panX = 0;
  let panY = 0;
  let scale = 1.0;
  const MIN_SCALE = 0.45;
  const MAX_SCALE = 1.85;

  let isPanning = false;
  let startPointerX = 0;
  let startPointerY = 0;
  let startPanX = 0;
  let startPanY = 0;

  // Active Pointers for Pinch-to-Zoom
  const activePointers = new Map();
  let initialPinchDistance = null;
  let initialPinchScale = 1.0;
  let pinchCenter = { x: 0, y: 0 };

  // Card Management
  let highestZ = 20;
  const cards = Array.from(document.querySelectorAll('.mat-card, .mat-sticky-note'));

  // Default Organized Grid Positions
  const defaultPositions = [
    { id: 'card-bezier', x: 1680, y: 1720 },
    { id: 'card-dengue', x: 2070, y: 1720 },
    { id: 'card-spectral', x: 2460, y: 1720 },
    { id: 'card-robot', x: 1680, y: 2240 },
    { id: 'card-conveyor', x: 2070, y: 2240 },
    { id: 'card-arcade', x: 2460, y: 2240 },
    { id: 'stickyNote', x: 1420, y: 1760 }
  ];

  // ============================================================================
  // 1. CAMERA & VIEWPORT TRANSFORM
  // ============================================================================

  function updateTransform() {
    plane.style.transform = `translate3d(${panX}px, ${panY}px, 0px) scale(${scale})`;

    // Metric readouts in cm / mm
    const gridOffsetMmX = Math.round((-panX / scale) / 2); // 2px ≈ 1mm
    const gridOffsetMmY = Math.round((-panY / scale) / 2);
    if (deskCoordsEl) {
      deskCoordsEl.textContent = `X: ${gridOffsetMmX}mm  Y: ${gridOffsetMmY}mm`;
    }
    if (deskZoomEl) {
      deskZoomEl.textContent = `SCALE: ${Math.round(scale * 100)}%`;
    }

    renderRulers();
  }

  function centerOnDesk(smooth = false) {
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;

    // Cluster center in mat canvas coordinates
    const targetCenterX = 2120;
    const targetCenterY = 2100;

    // Determine initial comfortable scale based on screen width
    let targetScale = 0.95;
    if (vw < 800) targetScale = 0.55;
    else if (vw < 1200) targetScale = 0.75;
    else if (vw < 1600) targetScale = 0.88;

    const targetPanX = vw / 2 - targetCenterX * targetScale;
    const targetPanY = vh / 2 - targetCenterY * targetScale;

    if (!smooth) {
      panX = targetPanX;
      panY = targetPanY;
      scale = targetScale;
      updateTransform();
      return;
    }

    // Smooth animation
    const startX = panX;
    const startY = panY;
    const startS = scale;
    const duration = 400;
    const startTime = performance.now();

    function ease(t) {
      return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
    }

    function step(now) {
      const elapsed = now - startTime;
      const progress = Math.min(1, elapsed / duration);
      const t = ease(progress);

      panX = startX + (targetPanX - startX) * t;
      panY = startY + (targetPanY - startY) * t;
      scale = startS + (targetScale - startS) * t;
      updateTransform();

      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  function zoomAtPoint(factor, clientX, clientY) {
    const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale * factor));
    if (newScale === scale) return;

    const rect = viewport.getBoundingClientRect();
    const originX = clientX - rect.left;
    const originY = clientY - rect.top;

    panX = originX - (originX - panX) * (newScale / scale);
    panY = originY - (originY - panY) * (newScale / scale);
    scale = newScale;

    updateTransform();
  }

  // ============================================================================
  // 2. METRIC MILLIMETER RULERS
  // ============================================================================

  function initRulerCanvases() {
    const dpr = window.devicePixelRatio || 1;

    if (rulerTopCanvas) {
      const rect = rulerTopCanvas.parentElement.getBoundingClientRect();
      rulerTopCanvas.width = rect.width * dpr;
      rulerTopCanvas.height = rect.height * dpr;
    }

    if (rulerLeftCanvas) {
      const rect = rulerLeftCanvas.parentElement.getBoundingClientRect();
      rulerLeftCanvas.width = rect.width * dpr;
      rulerLeftCanvas.height = rect.height * dpr;
    }

    renderRulers();
  }

  function renderRulers() {
    const dpr = window.devicePixelRatio || 1;

    // Top Horizontal Ruler
    if (rulerTopCanvas && rulerTopCanvas.parentElement) {
      const ctx = rulerTopCanvas.getContext('2d');
      const w = rulerTopCanvas.width / dpr;
      const h = rulerTopCanvas.height / dpr;

      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = '#101a17';
      ctx.fillRect(0, 0, w, h);

      // 100px on canvas plane = major grid mark (50mm)
      // 20px on canvas plane = minor mark (10mm)
      const minorScreenStep = 20 * scale;
      const majorScreenStep = 100 * scale;

      // Start position aligned with canvas origin
      const startX = panX % majorScreenStep;

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
      ctx.fillStyle = '#8da49b';
      ctx.font = '9px monospace';
      ctx.textBaseline = 'middle';

      // Draw minor ticks
      ctx.beginPath();
      for (let x = panX % minorScreenStep; x < w; x += minorScreenStep) {
        if (x < 0) continue;
        ctx.moveTo(x, h - 4);
        ctx.lineTo(x, h);
      }
      ctx.stroke();

      // Draw major ticks & numerals
      ctx.strokeStyle = 'rgba(46, 204, 113, 0.6)';
      ctx.beginPath();
      for (let x = panX % majorScreenStep; x < w; x += majorScreenStep) {
        if (x < 0) continue;
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);

        const canvasCoord = Math.round((x - panX) / scale);
        const mm = Math.round(canvasCoord / 2);
        if (x + 35 < w) {
          ctx.fillText(`${mm}mm`, x + 4, 10);
        }
      }
      ctx.stroke();
      ctx.restore();
    }

    // Left Vertical Ruler
    if (rulerLeftCanvas && rulerLeftCanvas.parentElement) {
      const ctx = rulerLeftCanvas.getContext('2d');
      const w = rulerLeftCanvas.width / dpr;
      const h = rulerLeftCanvas.height / dpr;

      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = '#101a17';
      ctx.fillRect(0, 0, w, h);

      const minorScreenStep = 20 * scale;
      const majorScreenStep = 100 * scale;

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
      ctx.fillStyle = '#8da49b';
      ctx.font = '8px monospace';

      // Draw minor ticks
      ctx.beginPath();
      for (let y = panY % minorScreenStep; y < h; y += minorScreenStep) {
        if (y < 0) continue;
        ctx.moveTo(w - 4, y);
        ctx.lineTo(w, y);
      }
      ctx.stroke();

      // Draw major ticks
      ctx.strokeStyle = 'rgba(46, 204, 113, 0.6)';
      ctx.beginPath();
      for (let y = panY % majorScreenStep; y < h; y += majorScreenStep) {
        if (y < 0) continue;
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);

        const canvasCoord = Math.round((y - panY) / scale);
        const mm = Math.round(canvasCoord / 2);
        if (y + 12 < h) {
          ctx.save();
          ctx.translate(4, y + 10);
          ctx.fillText(`${mm}`, 0, 0);
          ctx.restore();
        }
      }
      ctx.stroke();
      ctx.restore();
    }
  }

  // ============================================================================
  // 3. POINTER INTERACTIONS: PANNING & PINCH-ZOOM
  // ============================================================================

  viewport.addEventListener('pointerdown', (e) => {
    // If clicking directly on a link or button, let it fire normally
    if (e.target.closest('a, button, input')) return;

    // Check if target is inside a draggable card
    const card = e.target.closest('.mat-card, .mat-sticky-note');
    if (card) {
      initCardDrag(card, e);
      return;
    }

    // Otherwise, initiate cutting mat pan
    activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

    if (activePointers.size === 1) {
      isPanning = true;
      viewport.classList.add('is-panning');
      startPointerX = e.clientX;
      startPointerY = e.clientY;
      startPanX = panX;
      startPanY = panY;
      viewport.setPointerCapture(e.pointerId);
    } else if (activePointers.size === 2) {
      // 2-finger pinch initiate
      isPanning = false;
      const pts = Array.from(activePointers.values());
      initialPinchDistance = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
      initialPinchScale = scale;
      pinchCenter = {
        x: (pts[0].x + pts[1].x) / 2,
        y: (pts[0].y + pts[1].y) / 2
      };
    }
  });

  viewport.addEventListener('pointermove', (e) => {
    if (activePointers.has(e.pointerId)) {
      activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    }

    if (activePointers.size === 2 && initialPinchDistance) {
      const pts = Array.from(activePointers.values());
      const currentDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
      const ratio = currentDist / initialPinchDistance;
      const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, initialPinchScale * ratio));

      const rect = viewport.getBoundingClientRect();
      const originX = pinchCenter.x - rect.left;
      const originY = pinchCenter.y - rect.top;

      panX = originX - (originX - panX) * (newScale / scale);
      panY = originY - (originY - panY) * (newScale / scale);
      scale = newScale;
      updateTransform();
      return;
    }

    if (isPanning && activePointers.size === 1) {
      const dx = e.clientX - startPointerX;
      const dy = e.clientY - startPointerY;
      panX = startPanX + dx;
      panY = startPanY + dy;
      updateTransform();
    }
  });

  function endMatPan(e) {
    if (activePointers.has(e.pointerId)) {
      activePointers.delete(e.pointerId);
    }
    if (activePointers.size < 2) {
      initialPinchDistance = null;
    }
    if (activePointers.size === 0) {
      isPanning = false;
      viewport.classList.remove('is-panning');
    }
  }

  viewport.addEventListener('pointerup', endMatPan);
  viewport.addEventListener('pointercancel', endMatPan);

  // Mouse Wheel Zoom / Trackpad Pan
  viewport.addEventListener('wheel', (e) => {
    e.preventDefault();

    if (e.ctrlKey || e.metaKey || Math.abs(e.deltaY) > 40) {
      // Zoom centered on cursor
      const zoomFactor = e.deltaY < 0 ? 1.08 : 0.92;
      zoomAtPoint(zoomFactor, e.clientX, e.clientY);
    } else {
      // Trackpad 2-finger pan
      panX -= e.deltaX;
      panY -= e.deltaY;
      updateTransform();
    }
  }, { passive: false });

  // ============================================================================
  // 4. CARD DRAGGING & REORDERING
  // ============================================================================

  function initCardDrag(card, e) {
    e.stopPropagation();

    // Bring card to front
    highestZ += 1;
    card.style.zIndex = highestZ;

    card.classList.add('is-dragging');

    const cardRect = card.getBoundingClientRect();
    const planeRect = plane.getBoundingClientRect();

    // Current card position in plane coordinates
    const initialLeft = parseFloat(card.style.left) || (cardRect.left - planeRect.left) / scale;
    const initialTop = parseFloat(card.style.top) || (cardRect.top - planeRect.top) / scale;

    const startX = e.clientX;
    const startY = e.clientY;

    card.setPointerCapture(e.pointerId);

    function onPointerMove(moveEvent) {
      const dx = (moveEvent.clientX - startX) / scale;
      const dy = (moveEvent.clientY - startY) / scale;

      const newLeft = Math.round(initialLeft + dx);
      const newTop = Math.round(initialTop + dy);

      card.style.left = `${newLeft}px`;
      card.style.top = `${newTop}px`;
    }

    function onPointerUp(upEvent) {
      card.classList.remove('is-dragging');
      card.removeEventListener('pointermove', onPointerMove);
      card.removeEventListener('pointerup', onPointerUp);
      card.removeEventListener('pointercancel', onPointerUp);
      try {
        card.releasePointerCapture(upEvent.pointerId);
      } catch (_) {}
    }

    card.addEventListener('pointermove', onPointerMove);
    card.addEventListener('pointerup', onPointerUp);
    card.addEventListener('pointercancel', onPointerUp);
  }

  // Double click card to bring forward or focus
  cards.forEach((card) => {
    card.addEventListener('dblclick', () => {
      highestZ += 2;
      card.style.zIndex = highestZ;
    });
  });

  // ============================================================================
  // 5. AUTO-ARRANGE & TOP CONTROLS
  // ============================================================================

  function autoArrangeCards() {
    defaultPositions.forEach((pos) => {
      const el = document.getElementById(pos.id);
      if (!el) return;

      // Animate smoothly
      el.style.transition = 'left 0.4s cubic-bezier(0.16, 1, 0.3, 1), top 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      el.style.left = `${pos.x}px`;
      el.style.top = `${pos.y}px`;

      setTimeout(() => {
        el.style.transition = '';
      }, 420);
    });

    centerOnDesk(true);
  }

  if (btnAutoArrange) {
    btnAutoArrange.addEventListener('click', autoArrangeCards);
  }

  if (btnCenterDesk) {
    btnCenterDesk.addEventListener('click', () => centerOnDesk(true));
  }

  if (btnZoomIn) {
    btnZoomIn.addEventListener('click', () => {
      const rect = viewport.getBoundingClientRect();
      zoomAtPoint(1.2, rect.left + rect.width / 2, rect.top + rect.height / 2);
    });
  }

  if (btnZoomOut) {
    btnZoomOut.addEventListener('click', () => {
      const rect = viewport.getBoundingClientRect();
      zoomAtPoint(0.83, rect.left + rect.width / 2, rect.top + rect.height / 2);
    });
  }

  if (btnZoomReset) {
    btnZoomReset.addEventListener('click', () => {
      centerOnDesk(true);
    });
  }

  // ============================================================================
  // 6. MICRO-SCHEMATIC ANIMATED VISUALIZATIONS
  // ============================================================================

  // Dossier 1: Bézier Spline Evaluator
  function initBezierCanvas() {
    const canvas = document.getElementById('canvasBezier');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    let tVal = 0;

    function render() {
      tVal = (tVal + 0.008) % 1;
      ctx.clearRect(0, 0, w, h);

      // Background grid
      ctx.strokeStyle = '#e2dfd2';
      ctx.lineWidth = 1;
      for (let x = 0; x < w; x += 20) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
      }
      for (let y = 0; y < h; y += 20) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(w, y);
        ctx.stroke();
      }

      // 4 Control points
      const p0 = { x: 25, y: h - 18 };
      const p1 = { x: 75 + Math.sin(tVal * Math.PI * 2) * 20, y: 15 };
      const p2 = { x: 210, y: h - 15 + Math.cos(tVal * Math.PI * 2) * 12 };
      const p3 = { x: w - 25, y: 22 };

      // Hull lines
      ctx.strokeStyle = '#d0cbbe';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(p0.x, p0.y);
      ctx.lineTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.lineTo(p3.x, p3.y);
      ctx.stroke();
      ctx.setLineDash([]);

      // Cubic curve
      ctx.strokeStyle = '#0284c7';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(p0.x, p0.y);
      ctx.bezierCurveTo(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);
      ctx.stroke();

      // de Casteljau point evaluation
      const u = tVal;
      const q0 = { x: p0.x + (p1.x - p0.x) * u, y: p0.y + (p1.y - p0.y) * u };
      const q1 = { x: p1.x + (p2.x - p1.x) * u, y: p1.y + (p2.y - p1.y) * u };
      const q2 = { x: p2.x + (p3.x - p2.x) * u, y: p2.y + (p3.y - p2.y) * u };
      const r0 = { x: q0.x + (q1.x - q0.x) * u, y: q0.y + (q1.y - q0.y) * u };
      const r1 = { x: q1.x + (q2.x - q1.x) * u, y: q1.y + (q2.y - q1.y) * u };
      const pt = { x: r0.x + (r1.x - r0.x) * u, y: r0.y + (r1.y - r0.y) * u };

      // Eval tangent point
      ctx.fillStyle = '#2ecc71';
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2);
      ctx.fill();

      // Control points
      [p0, p1, p2, p3].forEach((p, idx) => {
        ctx.fillStyle = idx === 0 || idx === 3 ? '#1e293b' : '#d97706';
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    return render;
  }

  // Dossier 2: Dengue Signal Decomposer
  function initDengueCanvas() {
    const canvas = document.getElementById('canvasDengue');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    let phase = 0;

    function render() {
      phase += 0.03;
      ctx.clearRect(0, 0, w, h);

      // Baseline
      ctx.strokeStyle = '#e2dfd2';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, h / 2);
      ctx.lineTo(w, h / 2);
      ctx.stroke();

      // IMF 1: High frequency climatic wavelet
      ctx.strokeStyle = 'rgba(2, 132, 199, 0.4)';
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      for (let x = 0; x < w; x++) {
        const y = h / 2 + Math.sin(x * 0.12 + phase * 2) * 12;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Ensembled prediction curve
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      for (let x = 0; x < w; x++) {
        const trend = Math.sin(x * 0.025 + phase * 0.4) * 22;
        const seasonal = Math.sin(x * 0.07 + phase) * 8;
        const y = h / 2 + trend + seasonal;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Threshold indicator
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.6)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(0, 18);
      ctx.lineTo(w, 18);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    return render;
  }

  // Dossier 3: Kubelka-Munk Spectral Curve
  function initSpectralCanvas() {
    const canvas = document.getElementById('canvasSpectral');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    let pulse = 0;

    function render() {
      pulse += 0.02;
      ctx.clearRect(0, 0, w, h);

      // Spectrum fill
      const grad = ctx.createLinearGradient(0, 0, w, 0);
      grad.addColorStop(0, '#6366f1');
      grad.addColorStop(0.35, '#06b6d4');
      grad.addColorStop(0.7, '#10b981');
      grad.addColorStop(1, '#f59e0b');

      ctx.fillStyle = grad;
      ctx.globalAlpha = 0.15;
      ctx.beginPath();
      ctx.moveTo(0, h);
      for (let x = 0; x < w; x++) {
        const normX = x / w;
        const peak = Math.exp(-Math.pow((normX - 0.52), 2) / 0.04);
        const y = h - 12 - (peak * 50 + Math.sin(normX * 8 + pulse) * 4);
        ctx.lineTo(x, y);
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      ctx.fill();
      ctx.globalAlpha = 1.0;

      // Curve line
      ctx.strokeStyle = '#0284c7';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < w; x++) {
        const normX = x / w;
        const peak = Math.exp(-Math.pow((normX - 0.52), 2) / 0.04);
        const y = h - 12 - (peak * 50 + Math.sin(normX * 8 + pulse) * 4);
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Spectral wavelength markers
      ctx.fillStyle = '#78716c';
      ctx.font = '8px monospace';
      ctx.fillText('400nm', 6, h - 3);
      ctx.fillText('550nm', w / 2 - 14, h - 3);
      ctx.fillText('700nm', w - 30, h - 3);
    }

    return render;
  }

  // Dossier 4: Cam Linkage & Kinematics
  function initKinematicsCanvas() {
    const canvas = document.getElementById('canvasKinematics');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    let theta = 0;

    function render() {
      theta += 0.035;
      ctx.clearRect(0, 0, w, h);

      const cx = 90;
      const cy = h / 2;
      const camR1 = 18;
      const camR2 = 28;

      // Rotating eccentric cam
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(theta);

      ctx.fillStyle = '#e2dfd2';
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.ellipse(6, 0, camR2, camR1, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Cam pivot
      ctx.fillStyle = '#0284c7';
      ctx.beginPath();
      ctx.arc(0, 0, 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // Follower arm
      const followerDisp = Math.cos(theta) * 12;
      const followerX = cx + camR2 + 8 + followerDisp;

      ctx.strokeStyle = '#d97706';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(followerX, cy);
      ctx.lineTo(w - 30, cy);
      ctx.stroke();

      // Polishing toolhead
      ctx.fillStyle = '#2ecc71';
      ctx.fillRect(w - 30, cy - 14, 18, 28);

      // Trajectory curve on right
      ctx.strokeStyle = 'rgba(2, 132, 199, 0.4)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      for (let i = 0; i < 40; i++) {
        const x = w - 8 - i;
        const y = cy + Math.sin(theta - i * 0.15) * 14;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    return render;
  }

  // Dossier 5: Dynamic Sorting Conveyor
  function initConveyorCanvas() {
    const canvas = document.getElementById('canvasConveyor');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    let offset = 0;

    function render() {
      offset = (offset + 1.2) % 30;
      ctx.clearRect(0, 0, w, h);

      // Conveyor belt bed
      ctx.fillStyle = '#334155';
      ctx.fillRect(15, h - 22, w - 30, 10);

      // Rollers
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 2;
      for (let x = 20; x < w - 20; x += 30) {
        ctx.beginPath();
        ctx.arc(x + offset, h - 17, 4, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Optical beam trigger
      const beamX = w * 0.45;
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.7)';
      ctx.setLineDash([2, 2]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(beamX, 8);
      ctx.lineTo(beamX, h - 22);
      ctx.stroke();
      ctx.setLineDash([]);

      // Actuator solenoid
      ctx.fillStyle = '#10b981';
      ctx.fillRect(beamX - 10, 5, 20, 8);

      // Moving package items
      const pkgPos = (offset * 4) % (w - 60) + 20;
      ctx.fillStyle = '#e2dfd2';
      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 1.5;
      ctx.fillRect(pkgPos, h - 38, 16, 16);
      ctx.strokeRect(pkgPos, h - 38, 16, 16);
    }

    return render;
  }

  // Dossier 6: 2D Deterministic Physics Engine
  function initArcadeCanvas() {
    const canvas = document.getElementById('canvasArcade');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    // 6 verlet particles
    const particles = [
      { x: 40, y: 35, vx: 1.2, vy: 0.8 },
      { x: 120, y: 55, vx: -1.0, vy: 1.1 },
      { x: 180, y: 25, vx: 0.9, vy: -0.7 },
      { x: 240, y: 45, vx: -1.3, vy: -0.6 }
    ];

    function render() {
      ctx.clearRect(0, 0, w, h);

      // Update & bounce particles
      particles.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 15 || p.x > w - 15) p.vx *= -1;
        if (p.y < 15 || p.y > h - 15) p.vy *= -1;
      });

      // Spatial springs / mesh connections
      ctx.strokeStyle = 'rgba(2, 132, 199, 0.35)';
      ctx.lineWidth = 1;
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const d = Math.hypot(particles[i].x - particles[j].x, particles[i].y - particles[j].y);
          if (d < 110) {
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
          }
        }
      }

      // Draw particle cores
      particles.forEach((p) => {
        ctx.fillStyle = '#2ecc71';
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#0284c7';
        ctx.beginPath();
        ctx.arc(p.x, p.y, 6, 0, Math.PI * 2);
        ctx.stroke();
      });
    }

    return render;
  }

  // Master Render Loop for micro-schematics
  function startSchematicLoop() {
    const renders = [
      initBezierCanvas(),
      initDengueCanvas(),
      initSpectralCanvas(),
      initKinematicsCanvas(),
      initConveyorCanvas(),
      initArcadeCanvas()
    ].filter(Boolean);

    function loop() {
      renders.forEach((fn) => fn());
      requestAnimationFrame(loop);
    }

    requestAnimationFrame(loop);
  }

  // ============================================================================
  // 7. INITIALIZATION & RESIZE
  // ============================================================================

  function init() {
    initRulerCanvases();
    centerOnDesk(false);
    startSchematicLoop();

    window.addEventListener('resize', () => {
      initRulerCanvases();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
