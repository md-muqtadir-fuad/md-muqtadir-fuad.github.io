const { spawn } = require('child_process');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9444;

const chromeProc = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--window-size=1280,800',
  'about:blank'
]);

async function getWsUrl() {
  for (let i = 0; i < 20; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      const data = await res.json();
      const pageTarget = data.find(t => t.type === 'page');
      if (pageTarget && pageTarget.webSocketDebuggerUrl) {
        return pageTarget.webSocketDebuggerUrl;
      }
    } catch (e) {
      await new Promise(r => setTimeout(r, 200));
    }
  }
  throw new Error('Timeout waiting for Chrome CDP');
}

async function main() {
  try {
    const wsUrl = await getWsUrl();
    const ws = new WebSocket(wsUrl);

    await new Promise(r => ws.onopen = r);

    let msgId = 1;
    function sendCommand(method, params = {}) {
      return new Promise((resolve) => {
        const id = msgId++;
        const handler = (event) => {
          const res = JSON.parse(event.data);
          if (res.id === id) {
            ws.removeEventListener('message', handler);
            resolve(res.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    await sendCommand('Page.enable');
    await sendCommand('Page.navigate', { url: 'http://localhost:3000/blog-semi-automated-shoe-cleaning-machine.html' });
    await new Promise(r => setTimeout(r, 3000));

    const evalCode = `
      (() => {
        // Add a style tag with the proposed global CSS fixes
        const style = document.createElement('style');
        style.textContent = \`
          html, body {
            overflow-x: hidden !important;
            max-width: 100vw !important;
          }
          .overflow-x-auto {
            position: relative !important;
            max-width: 100% !important;
          }
          main, article {
            min-width: 0 !important;
            max-width: 100% !important;
          }
        \`;
        document.head.appendChild(style);

        const docWidth = document.documentElement.clientWidth;
        const scrollWidth = document.documentElement.scrollWidth;
        const bodyScrollWidth = document.body.scrollWidth;

        // Check if anything at all sticks out beyond docWidth
        const stickingOut = [];
        document.querySelectorAll('*').forEach(el => {
          const rect = el.getBoundingClientRect();
          if (rect.right > docWidth + 1) {
            stickingOut.push({
              tag: el.tagName,
              id: el.id,
              class: el.className.toString().slice(0, 50),
              rectRight: Math.round(rect.right),
              rectLeft: Math.round(rect.left),
              rectWidth: Math.round(rect.width)
            });
          }
        });

        // Also test scrolling horizontally:
        window.scrollTo(500, 0);
        const scrollXAfterScroll = window.scrollX;
        window.scrollTo(0, 0);

        return {
          docWidth,
          scrollWidth,
          bodyScrollWidth,
          hasPageScroll: scrollWidth > docWidth,
          scrollXAfterScroll,
          stickingOutCount: stickingOut.length,
          topStickingOut: stickingOut.slice(0, 5)
        };
      })()
    `;

    const res = await sendCommand('Runtime.evaluate', {
      expression: evalCode,
      returnByValue: true
    });

    console.log(JSON.stringify(res.result ? res.result.value : res, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
