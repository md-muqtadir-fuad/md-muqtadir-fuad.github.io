/**
 * FUAD SYNAPSE LAB // CYBER-PHYSICAL WORKBENCH & EXPERIMENTAL RESEARCH DECK
 * Isolated JavaScript Controller for /lab/lab.html
 */

(function () {
  'use strict';

  // ==========================================================================
  // 1. AUDIO SYNTHESIZER (Web Audio API)
  // ==========================================================================
  class LabAudioEngine {
    constructor() {
      this.ctx = null;
      this.enabled = false;
    }

    init() {
      if (!this.ctx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {
          this.ctx = new AudioContext();
        }
      }
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume();
      }
    }

    toggle() {
      this.init();
      this.enabled = !this.enabled;
      if (this.enabled) {
        this.playChirp(880, 1320, 0.08);
      }
      return this.enabled;
    }

    playClick() {
      if (!this.enabled || !this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1400, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(400, this.ctx.currentTime + 0.03);
      gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.03);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.03);
    }

    playChirp(freq1, freq2, duration) {
      if (!this.enabled || !this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq1, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(freq2, this.ctx.currentTime + duration);
      gain.gain.setValueAtTime(0.05, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    }
  }

  const sound = new LabAudioEngine();

  // ==========================================================================
  // 2. SIMULATION CHAMBER ENGINE (Lorenz, Bézier, Vector Fluid)
  // ==========================================================================
  class SimulationChamber {
    constructor(canvas) {
      this.canvas = canvas;
      this.ctx = canvas.getContext('2d');
      this.mode = 'attractor'; // 'attractor' | 'bezier' | 'fluid'
      this.width = canvas.width;
      this.height = canvas.height;
      this.running = true;
      this.fps = 60;
      this.frameCount = 0;
      this.lastFpsUpdate = performance.now();

      // Mouse & Dragging
      this.mouse = { x: 0, y: 0, px: 0, py: 0, down: false };
      this.draggedPoint = null;

      // Parameters
      this.speed = 1.0;
      this.chaos = 1.0;

      // Mode 1: Lorenz Attractor State
      this.lorenz = {
        sigma: 10,
        rho: 28,
        beta: 8 / 3,
        dt: 0.007,
        scale: 11,
        angleX: 0.4,
        angleY: 0.7,
        points: [],
        maxPoints: 1800,
        x: 0.1, y: 0, z: 0
      };

      // Mode 2: Bézier Spline Workbench State
      this.bezier = {
        points: [
          { x: 100, y: 350, label: 'P0' },
          { x: 260, y: 120, label: 'P1' },
          { x: 560, y: 100, label: 'P2' },
          { x: 740, y: 360, label: 'P3' }
        ],
        showComb: true
      };

      // Mode 3: Fluid / Vector Field State
      this.fluid = {
        particles: [],
        count: 700
      };

      this.initEvents();
      this.resize();
      this.resetSim();
      this.loop = this.loop.bind(this);
      requestAnimationFrame(this.loop);
    }

    resize() {
      const rect = this.canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      this.width = rect.width;
      this.height = rect.height;
      this.canvas.width = rect.width * dpr;
      this.canvas.height = rect.height * dpr;
      this.ctx.scale(dpr, dpr);

      // Reposition Bézier points proportionally
      if (this.mode === 'bezier') {
        const w = this.width;
        const h = this.height;
        this.bezier.points = [
          { x: w * 0.15, y: h * 0.75, label: 'P0' },
          { x: w * 0.35, y: h * 0.25, label: 'P1' },
          { x: w * 0.65, y: h * 0.2, label: 'P2' },
          { x: w * 0.85, y: h * 0.75, label: 'P3' }
        ];
      }
    }

    initEvents() {
      window.addEventListener('resize', () => this.resize());

      const getPos = (e) => {
        const rect = this.canvas.getBoundingClientRect();
        return {
          x: e.clientX - rect.left,
          y: e.clientY - rect.top
        };
      };

      this.canvas.addEventListener('mousedown', (e) => {
        sound.init();
        const pos = getPos(e);
        this.mouse.down = true;
        this.mouse.x = this.mouse.px = pos.x;
        this.mouse.y = this.mouse.py = pos.y;

        if (this.mode === 'bezier') {
          for (let p of this.bezier.points) {
            const dist = Math.hypot(p.x - pos.x, p.y - pos.y);
            if (dist < 18) {
              this.draggedPoint = p;
              sound.playClick();
              break;
            }
          }
        }
      });

      window.addEventListener('mousemove', (e) => {
        const pos = getPos(e);
        this.mouse.px = this.mouse.x;
        this.mouse.py = this.mouse.y;
        this.mouse.x = pos.x;
        this.mouse.y = pos.y;

        const coordsEl = document.getElementById('telemetryCoords');
        if (coordsEl) {
          coordsEl.textContent = `X:${Math.round(pos.x)} Y:${Math.round(pos.y)}`;
        }

        if (this.mouse.down) {
          if (this.mode === 'attractor') {
            const dx = this.mouse.x - this.mouse.px;
            const dy = this.mouse.y - this.mouse.py;
            this.lorenz.angleY += dx * 0.01;
            this.lorenz.angleX += dy * 0.01;
          } else if (this.mode === 'bezier' && this.draggedPoint) {
            this.draggedPoint.x = Math.max(10, Math.min(this.width - 10, pos.x));
            this.draggedPoint.y = Math.max(10, Math.min(this.height - 10, pos.y));
          }
        }
      });

      window.addEventListener('mouseup', () => {
        this.mouse.down = false;
        this.draggedPoint = null;
      });

      // Touch events for mobile
      this.canvas.addEventListener('touchstart', (e) => {
        if (e.touches.length > 0) {
          const t = e.touches[0];
          const rect = this.canvas.getBoundingClientRect();
          const pos = { x: t.clientX - rect.left, y: t.clientY - rect.top };
          this.mouse.down = true;
          this.mouse.x = this.mouse.px = pos.x;
          this.mouse.y = this.mouse.py = pos.y;

          if (this.mode === 'bezier') {
            for (let p of this.bezier.points) {
              if (Math.hypot(p.x - pos.x, p.y - pos.y) < 28) {
                this.draggedPoint = p;
                break;
              }
            }
          }
        }
      }, { passive: true });

      this.canvas.addEventListener('touchmove', (e) => {
        if (e.touches.length > 0) {
          const t = e.touches[0];
          const rect = this.canvas.getBoundingClientRect();
          const pos = { x: t.clientX - rect.left, y: t.clientY - rect.top };
          const dx = pos.x - this.mouse.x;
          const dy = pos.y - this.mouse.y;
          this.mouse.x = pos.x;
          this.mouse.y = pos.y;

          if (this.mode === 'attractor') {
            this.lorenz.angleY += dx * 0.01;
            this.lorenz.angleX += dy * 0.01;
          } else if (this.mode === 'bezier' && this.draggedPoint) {
            this.draggedPoint.x = pos.x;
            this.draggedPoint.y = pos.y;
          }
        }
      }, { passive: true });

      this.canvas.addEventListener('touchend', () => {
        this.mouse.down = false;
        this.draggedPoint = null;
      });
    }

    setMode(newMode) {
      this.mode = newMode;
      this.resetSim();
      sound.playChirp(600, 1200, 0.1);

      const hintEl = document.getElementById('canvasHint');
      if (hintEl) {
        if (newMode === 'attractor') {
          hintEl.textContent = '🖱 Drag to rotate 3D Lorenz attractor';
        } else if (newMode === 'bezier') {
          hintEl.textContent = '🖱 Drag control points P0, P1, P2, P3';
        } else if (newMode === 'fluid') {
          hintEl.textContent = '🖱 Move mouse to perturb aerodynamic velocity field';
        }
      }
    }

    resetSim() {
      if (this.mode === 'attractor') {
        this.lorenz.points = [];
        this.lorenz.x = 0.1;
        this.lorenz.y = 0;
        this.lorenz.z = 0;
      } else if (this.mode === 'fluid') {
        this.fluid.particles = [];
        for (let i = 0; i < this.fluid.count; i++) {
          this.fluid.particles.push({
            x: Math.random() * this.width,
            y: Math.random() * this.height,
            vx: 0, vy: 0,
            age: Math.random() * 120,
            maxAge: 80 + Math.random() * 100
          });
        }
      }
    }

    loop(timestamp) {
      this.frameCount++;
      if (timestamp - this.lastFpsUpdate >= 1000) {
        this.fps = Math.round((this.frameCount * 1000) / (timestamp - this.lastFpsUpdate));
        this.frameCount = 0;
        this.lastFpsUpdate = timestamp;
        const fpsEl = document.getElementById('telemetryFps');
        if (fpsEl) fpsEl.textContent = `${this.fps} FPS`;
      }

      this.ctx.clearRect(0, 0, this.width, this.height);

      if (this.mode === 'attractor') {
        this.renderLorenz();
      } else if (this.mode === 'bezier') {
        this.renderBezier();
      } else if (this.mode === 'fluid') {
        this.renderFluid();
      }

      requestAnimationFrame(this.loop);
    }

    // ------------------------------------------------------------------------
    // Mode 1: Lorenz Attractor
    // ------------------------------------------------------------------------
    renderLorenz() {
      const { sigma, beta, dt, scale, angleX, angleY } = this.lorenz;
      const rho = 28 * this.chaos;
      const stepsPerFrame = Math.round(10 * this.speed);

      for (let i = 0; i < stepsPerFrame; i++) {
        const dx = sigma * (this.lorenz.y - this.lorenz.x) * dt;
        const dy = (this.lorenz.x * (rho - this.lorenz.z) - this.lorenz.y) * dt;
        const dz = (this.lorenz.x * this.lorenz.y - beta * this.lorenz.z) * dt;

        this.lorenz.x += dx;
        this.lorenz.y += dy;
        this.lorenz.z += dz;

        this.lorenz.points.push({ x: this.lorenz.x, y: this.lorenz.y, z: this.lorenz.z });
        if (this.lorenz.points.length > this.lorenz.maxPoints) {
          this.lorenz.points.shift();
        }
      }

      // Auto-rotation when not dragging
      if (!this.mouse.down) {
        this.lorenz.angleY += 0.003 * this.speed;
      }

      const cx = this.width / 2;
      const cy = this.height / 2;
      const cosY = Math.cos(this.lorenz.angleY);
      const sinY = Math.sin(this.lorenz.angleY);
      const cosX = Math.cos(this.lorenz.angleX);
      const sinX = Math.sin(this.lorenz.angleX);

      const project = (p) => {
        // Center attractor vertically (average z is around 25)
        const x0 = p.x;
        const y0 = p.y;
        const z0 = p.z - 25;

        // Rotate Y
        const x1 = x0 * cosY - z0 * sinY;
        const z1 = x0 * sinY + z0 * cosY;

        // Rotate X
        const y2 = y0 * cosX - z1 * sinX;
        const z2 = y0 * sinX + z1 * cosX;

        const fov = 400;
        const perspective = fov / (fov + z2 * scale * 0.4);
        return {
          px: cx + x1 * scale * perspective,
          py: cy + y2 * scale * perspective,
          depth: z2
        };
      };

      if (this.lorenz.points.length < 2) return;

      this.ctx.lineWidth = 1.2;
      for (let i = 1; i < this.lorenz.points.length; i++) {
        const p1 = project(this.lorenz.points[i - 1]);
        const p2 = project(this.lorenz.points[i]);

        const progress = i / this.lorenz.points.length;
        const alpha = Math.min(1, progress * 1.2);
        
        // Gradient color: Cyan to Electric Violet
        this.ctx.beginPath();
        this.ctx.strokeStyle = `hsla(${185 + progress * 80}, 100%, 55%, ${alpha})`;
        this.ctx.moveTo(p1.px, p1.py);
        this.ctx.lineTo(p2.px, p2.py);
        this.ctx.stroke();
      }

      // Lead glowing particle
      const lead = project(this.lorenz.points[this.lorenz.points.length - 1]);
      this.ctx.beginPath();
      this.ctx.arc(lead.px, lead.py, 3.5, 0, Math.PI * 2);
      this.ctx.fillStyle = '#00f0ff';
      this.ctx.shadowColor = '#00f0ff';
      this.ctx.shadowBlur = 12;
      this.ctx.fill();
      this.ctx.shadowBlur = 0;
    }

    // ------------------------------------------------------------------------
    // Mode 2: Bézier Spline Workbench
    // ------------------------------------------------------------------------
    renderBezier() {
      const [p0, p1, p2, p3] = this.bezier.points;
      const ctx = this.ctx;

      // Draw dashed control polygon
      ctx.beginPath();
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.setLineDash([4, 4]);
      ctx.lineWidth = 1;
      ctx.moveTo(p0.x, p0.y);
      ctx.lineTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.lineTo(p3.x, p3.y);
      ctx.stroke();
      ctx.setLineDash([]);

      // Cubic Bézier calculation
      const evaluate = (t) => {
        const mt = 1 - t;
        const mt2 = mt * mt;
        const mt3 = mt2 * mt;
        const t2 = t * t;
        const t3 = t2 * t;

        const x = mt3 * p0.x + 3 * mt2 * t * p1.x + 3 * mt * t2 * p2.x + t3 * p3.x;
        const y = mt3 * p0.y + 3 * mt2 * t * p1.y + 3 * mt * t2 * p2.y + t3 * p3.y;

        // 1st Derivative (Velocity / Tangent)
        const dx = 3 * mt2 * (p1.x - p0.x) + 6 * mt * t * (p2.x - p1.x) + 3 * t2 * (p3.x - p2.x);
        const dy = 3 * mt2 * (p1.y - p0.y) + 6 * mt * t * (p2.y - p1.y) + 3 * t2 * (p3.y - p2.y);

        // 2nd Derivative (Acceleration)
        const ddx = 6 * mt * (p2.x - 2 * p1.x + p0.x) + 6 * t * (p3.x - 2 * p2.x + p1.x);
        const ddy = 6 * mt * (p2.y - 2 * p1.y + p0.y) + 6 * t * (p3.y - 2 * p2.y + p1.y);

        // Curvature kappa = |x'y'' - y'x''| / (x'^2 + y'^2)^(3/2)
        const num = dx * ddy - dy * ddx;
        const denom = Math.pow(dx * dx + dy * dy, 1.5);
        const curvature = denom !== 0 ? num / denom : 0;

        return { x, y, dx, dy, curvature };
      };

      // Draw Curvature Comb Spikes
      const samples = 60;
      ctx.beginPath();
      ctx.strokeStyle = 'rgba(255, 183, 3, 0.45)';
      ctx.lineWidth = 1;
      for (let i = 0; i <= samples; i++) {
        const t = i / samples;
        const pt = evaluate(t);
        const len = Math.hypot(pt.dx, pt.dy);
        if (len > 0.001) {
          const nx = -pt.dy / len;
          const ny = pt.dx / len;
          const combHeight = pt.curvature * 3500;
          ctx.moveTo(pt.x, pt.y);
          ctx.lineTo(pt.x + nx * combHeight, pt.y + ny * combHeight);
        }
      }
      ctx.stroke();

      // Draw Main Bézier Spline with Gradient Glow
      ctx.beginPath();
      ctx.lineWidth = 3;
      ctx.strokeStyle = '#00f0ff';
      ctx.shadowColor = 'rgba(0, 240, 255, 0.5)';
      ctx.shadowBlur = 10;
      ctx.moveTo(p0.x, p0.y);
      ctx.bezierCurveTo(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y);
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Draw Control Point Handles
      this.bezier.points.forEach((p, idx) => {
        const isSelected = this.draggedPoint === p;
        ctx.beginPath();
        ctx.arc(p.x, p.y, isSelected ? 8 : 6, 0, Math.PI * 2);
        ctx.fillStyle = idx === 0 || idx === 3 ? '#00ff9d' : '#ffb703';
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#fff';
        ctx.stroke();

        ctx.font = '11px "JetBrains Mono", monospace';
        ctx.fillStyle = '#fff';
        ctx.fillText(`${p.label} (${Math.round(p.x)}, ${Math.round(p.y)})`, p.x + 10, p.y - 10);
      });
    }

    // ------------------------------------------------------------------------
    // Mode 3: Aerodynamic Vector Field / Fluid
    // ------------------------------------------------------------------------
    renderFluid() {
      const ctx = this.ctx;
      const speedMult = this.speed * 2.5;

      ctx.fillStyle = 'rgba(4, 5, 8, 0.2)';
      ctx.fillRect(0, 0, this.width, this.height);

      this.fluid.particles.forEach((p) => {
        // Base flow from left to right + noise vortices
        const scale = 0.006 * this.chaos;
        const angle = Math.sin(p.x * scale) * Math.cos(p.y * scale) * Math.PI * 2;
        
        let fx = Math.cos(angle) * 1.5 + 1.8;
        let fy = Math.sin(angle) * 1.2;

        // Interaction with mouse obstacle/vortex
        const dx = p.x - this.mouse.x;
        const dy = p.y - this.mouse.y;
        const dist = Math.hypot(dx, dy);
        if (dist < 120 && dist > 1) {
          const force = (120 - dist) / 120;
          fx += (dx / dist) * force * 5;
          fy += (dy / dist) * force * 5;
        }

        p.vx = p.vx * 0.9 + fx * 0.1;
        p.vy = p.vy * 0.9 + fy * 0.1;

        const prevX = p.x;
        const prevY = p.y;
        p.x += p.vx * speedMult;
        p.y += p.vy * speedMult;
        p.age++;

        // Reset if offscreen or expired
        if (p.x > this.width || p.x < 0 || p.y > this.height || p.y < 0 || p.age > p.maxAge) {
          p.x = 0;
          p.y = Math.random() * this.height;
          p.vx = 2;
          p.vy = 0;
          p.age = 0;
        }

        // Draw particle stream segment
        const velocity = Math.hypot(p.vx, p.vy);
        const hue = 180 + Math.min(100, velocity * 25);
        ctx.beginPath();
        ctx.strokeStyle = `hsla(${hue}, 100%, 60%, 0.7)`;
        ctx.lineWidth = 1.2;
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      });
    }

    capturePNG() {
      const link = document.createElement('a');
      link.download = `fuad-lab-${this.mode}-${Date.now()}.png`;
      link.href = this.canvas.toDataURL('image/png');
      link.click();
      sound.playChirp(1200, 2400, 0.15);
    }
  }

  // ==========================================================================
  // 3. MINI OSCILLOSCOPE WAVEFORMS ON PROJECT CARDS
  // ==========================================================================
  function initMiniCanvases() {
    const miniCanvases = document.querySelectorAll('.card-canvas-mini');
    miniCanvases.forEach((canvas) => {
      const type = canvas.dataset.type || 'wave';
      const ctx = canvas.getContext('2d');
      let offset = Math.random() * 100;

      function drawMini() {
        const w = (canvas.width = canvas.clientWidth);
        const h = (canvas.height = canvas.clientHeight);
        ctx.clearRect(0, 0, w, h);

        offset += 0.05;

        // Grid lines
        ctx.strokeStyle = 'rgba(0, 240, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, h / 2);
        ctx.lineTo(w, h / 2);
        ctx.stroke();

        ctx.beginPath();
        ctx.lineWidth = 1.5;

        if (type === 'bezier') {
          ctx.strokeStyle = '#00f0ff';
          ctx.moveTo(0, h * 0.8);
          ctx.bezierCurveTo(w * 0.3, h * 0.1 + Math.sin(offset) * 10, w * 0.7, h * 0.9, w, h * 0.2);
        } else if (type === 'ecg') {
          ctx.strokeStyle = '#00ff9d';
          ctx.moveTo(0, h / 2);
          for (let x = 0; x < w; x++) {
            const phase = (x + offset * 15) % 60;
            let y = h / 2;
            if (phase > 20 && phase < 25) y -= 18;
            else if (phase >= 25 && phase < 30) y += 12;
            ctx.lineTo(x, y);
          }
        } else if (type === 'fourier') {
          ctx.strokeStyle = '#ffb703';
          ctx.moveTo(0, h / 2);
          for (let x = 0; x < w; x += 2) {
            const y = h / 2 + Math.sin(x * 0.08 + offset) * 12 + Math.sin(x * 0.03 - offset * 1.5) * 8;
            ctx.lineTo(x, y);
          }
        } else if (type === 'stepper') {
          ctx.strokeStyle = '#b5179e';
          ctx.moveTo(0, h * 0.7);
          for (let x = 0; x < w; x += 16) {
            const high = (Math.floor(x / 16) + Math.floor(offset * 2)) % 2 === 0;
            const y = high ? h * 0.25 : h * 0.75;
            ctx.lineTo(x, y);
            ctx.lineTo(x + 16, y);
          }
        } else {
          ctx.strokeStyle = '#00f0ff';
          ctx.moveTo(0, h / 2);
          for (let x = 0; x < w; x += 2) {
            ctx.lineTo(x, h / 2 + Math.sin(x * 0.05 + offset) * 14);
          }
        }
        ctx.stroke();

        requestAnimationFrame(drawMini);
      }

      drawMini();
    });
  }

  // ==========================================================================
  // 4. INTERACTIVE EMBEDDED TERMINAL (LAB-SHELL)
  // ==========================================================================
  class LabTerminal {
    constructor(dockEl, simEngine) {
      this.dock = dockEl;
      this.sim = simEngine;
      this.output = dockEl.querySelector('.terminal-output');
      this.input = dockEl.querySelector('.terminal-input');
      this.header = dockEl.querySelector('.terminal-header');
      this.toggleBtn = dockEl.querySelector('.term-toggle-btn');
      this.history = [];
      this.historyIndex = -1;

      this.init();
    }

    init() {
      // Toggle minimize/expand
      this.header.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') {
          this.dock.classList.toggle('minimized');
          sound.playClick();
        }
      });

      this.toggleBtn.addEventListener('click', () => {
        this.dock.classList.toggle('minimized');
        sound.playClick();
      });

      // Terminal Command Dispatcher
      this.input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const raw = this.input.value.trim();
          if (raw) {
            this.history.push(raw);
            this.historyIndex = this.history.length;
            this.execute(raw);
          }
          this.input.value = '';
          sound.playClick();
        } else if (e.key === 'ArrowUp') {
          if (this.historyIndex > 0) {
            this.historyIndex--;
            this.input.value = this.history[this.historyIndex];
          }
          e.preventDefault();
        } else if (e.key === 'ArrowDown') {
          if (this.historyIndex < this.history.length - 1) {
            this.historyIndex++;
            this.input.value = this.history[this.historyIndex];
          } else {
            this.historyIndex = this.history.length;
            this.input.value = '';
          }
          e.preventDefault();
        }
      });
    }

    log(text, className = '') {
      const p = document.createElement('div');
      p.className = className;
      p.innerHTML = text;
      this.output.appendChild(p);
      this.output.scrollTop = this.output.scrollHeight;
    }

    execute(cmdStr) {
      this.log(`<span class="term-prompt">fuad@lab:~$</span> <span class="term-cmd">${cmdStr}</span>`);
      const parts = cmdStr.toLowerCase().split(/\s+/);
      const cmd = parts[0];
      const arg = parts[1];

      switch (cmd) {
        case 'help':
          this.log(`Available Commands:<br>
  - <span class="term-line-cyan">projects</span> : List all active lab projects & research bays<br>
  - <span class="term-line-cyan">sim &lt;attractor|bezier|fluid&gt;</span> : Switch simulation chamber mode<br>
  - <span class="term-line-cyan">status</span> : Display live hardware & research telemetry<br>
  - <span class="term-line-cyan">matrix</span> : Toggle high-tech scanlines overlay<br>
  - <span class="term-line-cyan">whoami</span> : Display researcher identity & BUET affiliation<br>
  - <span class="term-line-cyan">portfolio</span> : Return to main portfolio view<br>
  - <span class="term-line-cyan">clear</span> : Clear terminal screen`);
          break;

        case 'projects':
        case 'list':
          this.log(`ACTIVE RESEARCH BAYS:<br>
  [BAY-01] BezierLab: Mathematical Spline Synthesizer<br>
  [BAY-02] Dengue Epidemiology Forecasting Framework (PLOS ONE)<br>
  [BAY-03] Physics-Informed Spectral Matching Machine<br>
  [BAY-04] FabLab Automated Shoe Cleaning Robot<br>
  [BAY-05] IoT Sensor Sorting Conveyor<br>
  [BAY-06] Retro Space Shooter Physics Rig<br>
  [BAY-07] BanglaBERT & Resource-Constrained NLP Benchmarks`);
          break;

        case 'sim':
          if (['attractor', 'bezier', 'fluid'].includes(arg)) {
            this.sim.setMode(arg);
            // Update UI buttons
            document.querySelectorAll('.sim-mode-btn').forEach((btn) => {
              btn.classList.toggle('active', btn.dataset.mode === arg);
            });
            this.log(`Simulation switched to: <span class="term-line-success">${arg.toUpperCase()}</span>`, 'term-line-success');
          } else {
            this.log(`Usage: sim &lt;attractor | bezier | fluid&gt;`, 'term-line-warn');
          }
          break;

        case 'status':
          this.log(`NODE STATUS: ONLINE<br>
  FPS: ${this.sim.fps} | COORD: (${Math.round(this.sim.mouse.x)}, ${Math.round(this.sim.mouse.y)})<br>
  AFFILIATION: Institute of Appropriate Technology, BUET<br>
  PROJECT PIN: 14011 (Fab Lab Prototyping Facility)`, 'term-line-info');
          break;

        case 'matrix':
          const scanlines = document.getElementById('crtScanlines');
          if (scanlines) {
            scanlines.classList.toggle('disabled');
            const state = scanlines.classList.contains('disabled') ? 'OFF' : 'ON';
            this.log(`CRT Matrix Scanlines: <span class="term-line-cyan">${state}</span>`);
          }
          break;

        case 'whoami':
          this.log(`Md. Muqtadir Fuad — Program Engineer (Fab Lab), BUET.<br>Industrial & Production Engineering Researcher.`, 'term-line-success');
          break;

        case 'portfolio':
          this.log(`Navigating to / ...`, 'term-line-info');
          setTimeout(() => (window.location.href = '/'), 500);
          break;

        case 'clear':
          this.output.innerHTML = '';
          break;

        default:
          this.log(`Command not recognized: '${cmd}'. Type <span class="term-line-cyan">'help'</span> for instructions.`, 'term-line-error');
          break;
      }
    }
  }

  // ==========================================================================
  // 5. BLUEPRINT & SCHEMATICS DATA & MODAL CONTROLLER
  // ==========================================================================
  const SCHEMATICS = {
    bezierlab: {
      badge: 'BAY 01 // GEOMETRIC ENGINE',
      title: 'BezierLab: Parametric Spline & Curvature Synthesis',
      diagram: `[P0] ───(Tangent Vector t0)───> [P1]
   \\                                  \\
    \\ (De Casteljau Subdivision)       \\
     \\                                  \\
      [P(t)] = (1-t)³P0 + 3(1-t)²t P1 + 3(1-t)t² P2 + t³ P3
       \\                                  \\
        [P2] ───(Curvature Comb κ)──────> [P3]`,
      body: `<p><strong>Core Concept:</strong> BezierLab is a specialized mathematical workbench for generating, evaluating, and exporting arbitrary-order Bézier curves and B-spline paths for CNC machining and vector rendering.</p>
      <p class="mt-3"><strong>Key Mathematical Formulations:</strong></p>
      <ul style="padding-left: 1.25rem; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 0.4rem;">
        <li>Parametric cubic curve: <code>P(t) = (1-t)³P₀ + 3(1-t)²t P₁ + 3(1-t)t² P₂ + t³P₃</code></li>
        <li>Curvature analysis: <code>κ(t) = |x'y'' - y'x''| / (x'² + y'²)^(3/2)</code></li>
        <li>Continuous curvature combs normal to tangent vectors for G2 continuity verification in rapid prototyping.</li>
      </ul>`
    },
    dengue: {
      badge: 'BAY 02 // EPIDEMIOLOGY AI',
      title: 'Tactical vs. Strategic Dengue Forecasting Framework',
      diagram: `[Climate Covariates] ────┐
  (Temp, Rainfall, Hum)  │
                         ▼
[Serotype Distributions] ──> [Feature Engineering & Lag Decomposition]
                         │
                         ▼
              [Multi-Horizon Ensemble]
        ├── Tactical (1-4 weeks): GBDT + Rolling Lags
        └── Strategic (5-12 weeks): Climate Transfer Models
                         │
                         ▼
              [PLOS ONE Published Validation]`,
      body: `<p><strong>Published in PLOS ONE:</strong> An adaptable framework for horizon-dependent dengue forecasting using data-driven approaches with serotype and climate covariates across Bangladesh.</p>
      <p class="mt-3"><strong>Impact & Architecture:</strong> Demonstrates that short-term outbreaks require autoregressive serotype dynamics, whereas long-range seasonal planning hinges upon lagged meteorological covariates.</p>`
    },
    spectral: {
      badge: 'BAY 03 // HYBRID PHYSICS-ML',
      title: 'Forward-Inverse Spectral Recipe Matcher',
      diagram: `[Target Reflectance R_λ] ──> [Module B: Sparse Inverse Reconstructor]
                                       │ (Median Blend / Sparse L1)
                                       ▼
                             [Candidate Recipe Blend]
                                       │
                                       ▼
  [Process Parameters] ────> [Module A: Multi-Target Forward Quality Model]
                             (Gradient Boosted Decision Trees)
                                       │
                                       ▼
                             [Module C: Feasibility & ΔE Ranking]`,
      body: `<p><strong>Industrial Problem:</strong> Traditional Kubelka-Munk physics fails to predict sparse textile dye recipes under shop-floor process variations.</p>
      <p class="mt-3"><strong>Solution:</strong> A hybrid physics-informed machine learning architecture combining spectral descriptors with gradient boosting, yielding a component-wise median blend recipe MAE of 0.0295 and eliminating costly physical dye laboratory trials.</p>`
    },
    shoeshiner: {
      badge: 'BAY 04 // MECHATRONICS',
      title: 'Semi-Automated Shoe Cleaning & Polishing Machine',
      diagram: `[Foot Presence Sensor] ──> [State Controller / Microcontroller]
                                 │
            ┌────────────────────┼────────────────────┐
            ▼                    ▼                    ▼
     [Rotary Brush Actuators] [Wax Dispersion] [Linear Cam Guide]
            │                    │                    │
            └────────────────────┴────────────────────┘
                                 │
                                 ▼
                     [Safety Interlock & Cycle End]`,
      body: `<p><strong>FabLab Mechatronics Project:</strong> Designed and fabricated at BUET Fab Lab. Combines mechanical cam-guided brush kinematics with an automated liquid wax metering system for rapid ergonomic shoe maintenance.</p>`
    },
    conveyor: {
      badge: 'BAY 05 // IOT & COMPUTER VISION',
      title: 'IoT Dynamic Sorting Conveyor Platform',
      diagram: `[High-Speed Camera / IR] ──> [Edge Vision Node] ──> [Cloud Dashboard / MQTT]
                                       │
                                       ▼
                       [Sorting Solenoid Diverter Gate]
                                       │
                                       ▼
                        [Bin Allocation & Telemetry]`,
      body: `<p><strong>Real-time Telemetry:</strong> High-throughput automated conveyor platform featuring optical object classification, MQTT telemetry broadcast, and dynamic pneumatically assisted divergence gates.</p>`
    },
    spaceshooter: {
      badge: 'BAY 06 // KINETIC ENGINE',
      title: 'Retro Space Shooter Arcade Physics Rig',
      diagram: `[User Input Vector] ──> [Kinetic State Machine (60 FPS)]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
[AABB Hitbox Query]   [Particle Emitter Pool]   [Web Audio Synth]
       │                       │                       │
       └───────────────────────┴───────────────────────┘
                               │
                               ▼
                       [HTML5 Canvas Blit]`,
      body: `<p><strong>Playable Arcade Engine:</strong> Built directly within this portfolio at <code>/games/space-shooter.html</code>. Features pure vanilla Canvas 2D particle dynamics, responsive controls, powerup multipliers, and zero third-party dependencies.</p>`
    }
  };

  function initModals() {
    const modalOverlay = document.getElementById('schematicModal');
    const modalBadge = document.getElementById('modalBadge');
    const modalTitle = document.getElementById('modalTitle');
    const modalDiagram = document.getElementById('modalDiagram');
    const modalBody = document.getElementById('modalBody');
    const closeBtn = document.getElementById('modalCloseBtn');

    document.querySelectorAll('[data-blueprint]').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const key = btn.dataset.blueprint;
        const data = SCHEMATICS[key];
        if (data) {
          modalBadge.textContent = data.badge;
          modalTitle.textContent = data.title;
          modalDiagram.textContent = data.diagram;
          modalBody.innerHTML = data.body;
          modalOverlay.classList.add('active');
          sound.playChirp(700, 1400, 0.1);
        }
      });
    });

    const closeModal = () => {
      modalOverlay.classList.remove('active');
      sound.playClick();
    };

    closeBtn.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // ==========================================================================
  // 6. FILTER PILLS
  // ==========================================================================
  function initFilters() {
    const pills = document.querySelectorAll('.filter-pill');
    const cards = document.querySelectorAll('.lab-card');

    pills.forEach((pill) => {
      pill.addEventListener('click', () => {
        sound.playClick();
        pills.forEach((p) => p.classList.remove('active'));
        pill.classList.add('active');

        const category = pill.dataset.filter;
        cards.forEach((card) => {
          if (category === 'all' || card.dataset.category === category) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // ==========================================================================
  // 7. DOM READY BOOTSTRAP
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Simulation Chamber
    const canvas = document.getElementById('labCanvas');
    const chamber = new SimulationChamber(canvas);

    // Mode Buttons
    document.querySelectorAll('.sim-mode-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.sim-mode-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        chamber.setMode(btn.dataset.mode);
      });
    });

    // Sliders
    const speedSlider = document.getElementById('sliderSpeed');
    if (speedSlider) {
      speedSlider.addEventListener('input', (e) => {
        chamber.speed = parseFloat(e.target.value);
      });
    }

    const chaosSlider = document.getElementById('sliderChaos');
    if (chaosSlider) {
      chaosSlider.addEventListener('input', (e) => {
        chamber.chaos = parseFloat(e.target.value);
      });
    }

    // Action buttons
    const btnReset = document.getElementById('btnResetSim');
    if (btnReset) {
      btnReset.addEventListener('click', () => {
        chamber.resetSim();
        sound.playClick();
      });
    }

    const btnCapture = document.getElementById('btnCapturePNG');
    if (btnCapture) {
      btnCapture.addEventListener('click', () => {
        chamber.capturePNG();
      });
    }

    // Sound Toggle HUD Button
    const btnAudio = document.getElementById('btnToggleAudio');
    if (btnAudio) {
      btnAudio.addEventListener('click', () => {
        const enabled = sound.toggle();
        btnAudio.textContent = enabled ? 'SFX: ON' : 'SFX: OFF';
        btnAudio.classList.toggle('active', enabled);
      });
    }

    // CRT Toggle HUD Button
    const btnCrt = document.getElementById('btnToggleCrt');
    const crtOverlay = document.getElementById('crtScanlines');
    if (btnCrt && crtOverlay) {
      btnCrt.addEventListener('click', () => {
        sound.playClick();
        crtOverlay.classList.toggle('disabled');
        const active = !crtOverlay.classList.contains('disabled');
        btnCrt.textContent = active ? 'CRT: ON' : 'CRT: OFF';
        btnCrt.classList.toggle('active', active);
      });
    }

    // Realtime UTC/Local Clock
    const clockEl = document.getElementById('telemetryClock');
    if (clockEl) {
      const updateClock = () => {
        const now = new Date();
        clockEl.textContent = now.toTimeString().split(' ')[0] + ' LCL';
      };
      updateClock();
      setInterval(updateClock, 1000);
    }

    // Initialize Card Mini-Waveforms
    initMiniCanvases();

    // Initialize Terminal
    const termDock = document.getElementById('terminalDock');
    if (termDock) {
      new LabTerminal(termDock, chamber);
    }

    // Initialize Modals & Filters
    initModals();
    initFilters();
  });
})();
