/**
 * DEMO 3: EXPLORABLE INTERACTIVE LABORATORY CONTROLLER
 * lab/demo3.js - Isolated JavaScript
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {

    // ========================================================================
    // APPARATUS 01: FOUR-BAR LINKAGE KINEMATICS SIMULATOR
    // ========================================================================
    (function initLinkage() {
      const canvas = document.getElementById('canvasLinkage');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const slider = document.getElementById('sliderCrankAngle');
      const readout = document.getElementById('readoutAngle');

      // Link dimensions
      const a = 50;  // Crank AB
      const b = 130; // Coupler BC
      const c = 90;  // Rocker CD
      const d = 140; // Ground AD

      let crankAngle = 0;
      let trace = [];

      function solveLinkage(theta) {
        const Ax = 80;
        const Ay = 180;
        const Dx = Ax + d;
        const Dy = Ay;

        const Bx = Ax + a * Math.cos(theta);
        const By = Ay - a * Math.sin(theta);

        // Distance from B to D
        const BD = Math.hypot(Dx - Bx, Dy - By);
        if (BD > b + c || BD < Math.abs(b - c)) return null;

        // Angle of line BD
        const angleBD = Math.atan2(Dy - By, Dx - Bx);
        // Angle CBD using law of cosines
        const cosCBD = (b * b + BD * BD - c * c) / (2 * b * BD);
        const angleCBD = Math.acos(Math.max(-1, Math.min(1, cosCBD)));

        // Position of C
        const Cx = Bx + b * Math.cos(angleBD - angleCBD);
        const Cy = By + b * Math.sin(angleBD - angleCBD);

        // Coupler point P (tracer point)
        const Px = (Bx + Cx) / 2 + (Cy - By) * 0.35;
        const Py = (By + Cy) / 2 - (Cx - Bx) * 0.35;

        return { A: {x: Ax, y: Ay}, B: {x: Bx, y: By}, C: {x: Cx, y: Cy}, D: {x: Dx, y: Dy}, P: {x: Px, y: Py} };
      }

      function draw() {
        const w = (canvas.width = canvas.clientWidth * (window.devicePixelRatio || 1));
        const h = (canvas.height = canvas.clientHeight * (window.devicePixelRatio || 1));
        ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);

        const rw = canvas.clientWidth;
        const rh = canvas.clientHeight;
        ctx.clearRect(0, 0, rw, rh);

        const pts = solveLinkage(crankAngle);
        if (!pts) return;

        // Trace coupler curve
        trace.push({ x: pts.P.x, y: pts.P.y });
        if (trace.length > 250) trace.shift();

        ctx.beginPath();
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([3, 3]);
        trace.forEach((pt, i) => {
          if (i === 0) ctx.moveTo(pt.x, pt.y);
          else ctx.lineTo(pt.x, pt.y);
        });
        ctx.stroke();
        ctx.setLineDash([]);

        // Ground link
        ctx.beginPath();
        ctx.strokeStyle = '#9ca3af';
        ctx.lineWidth = 3;
        ctx.moveTo(pts.A.x, pts.A.y);
        ctx.lineTo(pts.D.x, pts.D.y);
        ctx.stroke();

        // Links AB, BC, CD
        ctx.beginPath();
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = 3;
        ctx.moveTo(pts.A.x, pts.A.y);
        ctx.lineTo(pts.B.x, pts.B.y);
        ctx.lineTo(pts.C.x, pts.C.y);
        ctx.lineTo(pts.D.x, pts.D.y);
        ctx.stroke();

        // Coupler triangle
        ctx.beginPath();
        ctx.fillStyle = 'rgba(2, 132, 199, 0.12)';
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 1.5;
        ctx.moveTo(pts.B.x, pts.B.y);
        ctx.lineTo(pts.C.x, pts.C.y);
        ctx.lineTo(pts.P.x, pts.P.y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Pin joints
        [pts.A, pts.B, pts.C, pts.D].forEach((pt) => {
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, 5, 0, Math.PI * 2);
          ctx.fillStyle = '#fff';
          ctx.strokeStyle = '#111';
          ctx.lineWidth = 2;
          ctx.fill();
          ctx.stroke();
        });

        // Tracer point P
        ctx.beginPath();
        ctx.arc(pts.P.x, pts.P.y, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#dc2626';
        ctx.fill();
      }

      if (slider) {
        slider.addEventListener('input', (e) => {
          crankAngle = (parseFloat(e.target.value) * Math.PI) / 180;
          if (readout) readout.textContent = `${e.target.value}°`;
          draw();
        });
      }

      draw();
    })();

    // ========================================================================
    // APPARATUS 02: BÉZIER CURVATURE COMB (BEZIERLAB)
    // ========================================================================
    (function initBezier() {
      const canvas = document.getElementById('canvasBezier');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const readoutCurv = document.getElementById('readoutMaxCurv');

      const points = [
        { x: 60, y: 220 },
        { x: 180, y: 50 },
        { x: 380, y: 70 },
        { x: 500, y: 220 }
      ];

      let dragged = null;

      function draw() {
        const rw = canvas.clientWidth;
        const rh = canvas.clientHeight;
        canvas.width = rw * (window.devicePixelRatio || 1);
        canvas.height = rh * (window.devicePixelRatio || 1);
        ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
        ctx.clearRect(0, 0, rw, rh);

        const [p0, p1, p2, p3] = points;

        // Control Polygon
        ctx.beginPath();
        ctx.strokeStyle = '#d1d5db';
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1;
        ctx.moveTo(p0.x, p0.y);
        ctx.lineTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.lineTo(p3.x, p3.y);
        ctx.stroke();
        ctx.setLineDash([]);

        // Curvature calculation
        let maxK = 0;
        const samples = 80;

        ctx.beginPath();
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 1;

        for (let i = 0; i <= samples; i++) {
          const t = i / samples;
          const mt = 1 - t;
          const mt2 = mt * mt;
          const t2 = t * t;

          const x = mt * mt2 * p0.x + 3 * mt2 * t * p1.x + 3 * mt * t2 * p2.x + t * t2 * p3.x;
          const y = mt * mt2 * p0.y + 3 * mt2 * t * p1.y + 3 * mt * t2 * p2.y + t * t2 * p3.y;

          const dx = 3 * mt2 * (p1.x - p0.x) + 6 * mt * t * (p2.x - p1.x) + 3 * t2 * (p3.x - p2.x);
          const dy = 3 * mt2 * (p1.y - p0.y) + 6 * mt * t * (p2.y - p1.y) + 3 * t2 * (p3.y - p2.y);

          const ddx = 6 * mt * (p2.x - 2 * p1.x + p0.x) + 6 * t * (p3.x - 2 * p2.x + p1.x);
          const ddy = 6 * mt * (p2.y - 2 * p1.y + p0.y) + 6 * t * (p3.y - 2 * p2.y + p1.y);

          const num = dx * ddy - dy * ddx;
          const den = Math.pow(dx * dx + dy * dy, 1.5);
          const k = den !== 0 ? num / den : 0;
          if (Math.abs(k) > maxK) maxK = Math.abs(k);

          const len = Math.hypot(dx, dy);
          if (len > 0.001) {
            const nx = -dy / len;
            const ny = dx / len;
            const combLen = k * 3500;
            ctx.moveTo(x, y);
            ctx.lineTo(x + nx * combLen, y + ny * combLen);
          }
        }
        ctx.stroke();

        // Main curve
        ctx.beginPath();
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 2.5;
        ctx.moveTo(p0.x, p0.y);
        ctx.bezierCurveTo(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);
        ctx.stroke();

        // Handles
        points.forEach((p, idx) => {
          ctx.beginPath();
          ctx.arc(p.x, p.y, 6, 0, Math.PI * 2);
          ctx.fillStyle = idx === 0 || idx === 3 ? '#10b981' : '#f59e0b';
          ctx.fill();
          ctx.strokeStyle = '#fff';
          ctx.lineWidth = 2;
          ctx.stroke();
        });

        if (readoutCurv) {
          readoutCurv.textContent = `κ_max: ${(maxK * 1000).toFixed(2)} mm⁻¹`;
        }
      }

      canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;
        points.forEach((p) => {
          if (Math.hypot(p.x - mx, p.y - my) < 15) {
            dragged = p;
          }
        });
      });

      window.addEventListener('mousemove', (e) => {
        if (!dragged) return;
        const rect = canvas.getBoundingClientRect();
        dragged.x = Math.max(10, Math.min(canvas.clientWidth - 10, e.clientX - rect.left));
        dragged.y = Math.max(10, Math.min(canvas.clientHeight - 10, e.clientY - rect.top));
        draw();
      });

      window.addEventListener('mouseup', () => {
        dragged = null;
      });

      draw();
    })();

    // ========================================================================
    // APPARATUS 03: DENGUE CLIMATE LAG COUPLING
    // ========================================================================
    (function initDengue() {
      const canvas = document.getElementById('canvasDengue');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const slider = document.getElementById('sliderLagWeeks');
      const readout = document.getElementById('readoutLag');
      const readoutR2 = document.getElementById('readoutR2');

      let lag = 5; // weeks

      function draw() {
        const rw = canvas.clientWidth;
        const rh = canvas.clientHeight;
        canvas.width = rw * (window.devicePixelRatio || 1);
        canvas.height = rh * (window.devicePixelRatio || 1);
        ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
        ctx.clearRect(0, 0, rw, rh);

        const weeks = 52;
        const step = rw / weeks;

        // Climate wave (Humidity/Rainfall)
        ctx.beginPath();
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 2;
        for (let w = 0; w <= weeks; w++) {
          const x = w * step;
          const y = rh * 0.5 - Math.sin((w - 20) * 0.12) * (rh * 0.3);
          if (w === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Outbreak wave with lag
        ctx.beginPath();
        ctx.strokeStyle = '#dc2626';
        ctx.lineWidth = 2.5;
        for (let w = 0; w <= weeks; w++) {
          const x = w * step;
          const y = rh * 0.5 - Math.sin((w - 20 - lag) * 0.12) * (rh * 0.35);
          if (w === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Calculate coupling correlation
        const idealLag = 5;
        const r2 = Math.max(0.1, 1 - Math.abs(lag - idealLag) * 0.18).toFixed(2);
        if (readoutR2) readoutR2.textContent = `R²: ${r2}`;
      }

      if (slider) {
        slider.addEventListener('input', (e) => {
          lag = parseInt(e.target.value, 10);
          if (readout) readout.textContent = `${lag} Weeks`;
          draw();
        });
      }

      draw();
    })();

  });
})();
