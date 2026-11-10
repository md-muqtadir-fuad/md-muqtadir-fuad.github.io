/**
 * DEMO 1: INDUSTRIAL HARDWARE CONTROLLER
 * lab/demo1.js - Isolated JavaScript
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('crtCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    // State controlled by physical dials & switches
    const state = {
      freq1: 3.0,
      freq2: 4.0,
      damping: 0.8,
      mode: 'lissajous', // 'harmonic' | 'lissajous' | 'bezier'
      phase: 0
    };

    // Knobs setup
    const dials = [
      { id: 'dialFreq1', param: 'freq1', min: 1.0, max: 12.0, step: 0.1, valEl: 'valFreq1', unit: 'Hz' },
      { id: 'dialFreq2', param: 'freq2', min: 1.0, max: 12.0, step: 0.1, valEl: 'valFreq2', unit: 'Hz' },
      { id: 'dialDamp', param: 'damping', min: 0.1, max: 2.0, step: 0.05, valEl: 'valDamp', unit: '' }
    ];

    dials.forEach((d) => {
      const el = document.getElementById(d.id);
      const valDisplay = document.getElementById(d.valEl);
      if (!el) return;

      let startY = 0;
      let startVal = state[d.param];

      const onMouseDown = (e) => {
        startY = e.clientY;
        startVal = state[d.param];
        window.addEventListener('mousemove', onMouseMove);
        window.addEventListener('mouseup', onMouseUp);
        e.preventDefault();
      };

      const onMouseMove = (e) => {
        const delta = (startY - e.clientY) * 0.05;
        let newVal = Math.max(d.min, Math.min(d.max, startVal + delta * d.step * 10));
        newVal = Math.round(newVal * 100) / 100;
        state[d.param] = newVal;

        // Rotate visual knob (-135deg to +135deg)
        const pct = (newVal - d.min) / (d.max - d.min);
        const rot = -135 + pct * 270;
        el.style.transform = `rotate(${rot}deg)`;

        if (valDisplay) {
          valDisplay.textContent = newVal.toFixed(1) + (d.unit ? ' ' + d.unit : '');
        }

        const segEl = document.getElementById('segmentReadout');
        if (segEl) {
          segEl.textContent = `${state.freq1.toFixed(1)} / ${state.freq2.toFixed(1)}`;
        }
      };

      const onMouseUp = () => {
        window.removeEventListener('mousemove', onMouseMove);
        window.removeEventListener('mouseup', onMouseUp);
      };

      el.addEventListener('mousedown', onMouseDown);
    });

    // Switches setup
    document.querySelectorAll('.switch-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.switch-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        state.mode = btn.dataset.mode;
        const modeReadout = document.getElementById('readoutMode');
        if (modeReadout) modeReadout.textContent = `MODE: ${state.mode.toUpperCase()}`;
      });
    });

    // Oscilloscope Animation Loop
    function resizeCanvas() {
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * (window.devicePixelRatio || 1);
      canvas.height = rect.height * (window.devicePixelRatio || 1);
      ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    function renderCRT() {
      const rect = canvas.getBoundingClientRect();
      const w = rect.width;
      const h = rect.height;
      state.phase += 0.025;

      ctx.fillStyle = '#080c09';
      ctx.fillRect(0, 0, w, h);

      // CRT phosphor grid
      ctx.strokeStyle = 'rgba(76, 217, 100, 0.08)';
      ctx.lineWidth = 1;
      const gridSize = 24;
      ctx.beginPath();
      for (let x = 0; x < w; x += gridSize) {
        ctx.moveTo(x, 0); ctx.lineTo(x, h);
      }
      for (let y = 0; y < h; y += gridSize) {
        ctx.moveTo(0, y); ctx.lineTo(w, y);
      }
      ctx.stroke();

      // Main Phosphor Trace
      ctx.beginPath();
      ctx.strokeStyle = '#4cd964';
      ctx.lineWidth = 2;
      ctx.shadowColor = '#4cd964';
      ctx.shadowBlur = 8;

      const cx = w / 2;
      const cy = h / 2;

      if (state.mode === 'lissajous') {
        const radiusX = w * 0.38;
        const radiusY = h * 0.38;
        const points = 400;
        for (let i = 0; i <= points; i++) {
          const t = (i / points) * Math.PI * 2;
          const x = cx + radiusX * Math.sin(state.freq1 * t + state.phase);
          const y = cy + radiusY * Math.sin(state.freq2 * t) * state.damping;
          if (i === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
      } else if (state.mode === 'harmonic') {
        ctx.moveTo(0, cy);
        for (let x = 0; x < w; x += 2) {
          const t = (x / w) * Math.PI * 4;
          const y = cy + Math.sin(t * state.freq1 + state.phase) * (h * 0.25) * state.damping +
                         Math.cos(t * state.freq2 * 0.5) * 20;
          ctx.lineTo(x, y);
        }
      } else if (state.mode === 'bezier') {
        const p0 = { x: w * 0.1, y: h * 0.8 };
        const p1 = { x: w * 0.3, y: h * 0.2 + Math.sin(state.phase * 2) * 40 };
        const p2 = { x: w * 0.7, y: h * 0.2 + Math.cos(state.phase * 2) * 40 };
        const p3 = { x: w * 0.9, y: h * 0.8 };
        ctx.moveTo(p0.x, p0.y);
        ctx.bezierCurveTo(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      requestAnimationFrame(renderCRT);
    }

    renderCRT();
  });
})();
