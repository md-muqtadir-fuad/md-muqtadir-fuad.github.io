const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9447;

const chromeProc = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--window-size=1280,900',
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
    await new Promise(r => setTimeout(r, 1200));

    // Find cover card and scroll to it
    const evalRes = await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const el = document.querySelectorAll('.border.border-black.p-4.bg-gray-50')[0];
          if (el) {
            el.scrollIntoView({ behavior: 'instant', block: 'center' });
            const rect = el.getBoundingClientRect();
            return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
          }
          return null;
        })()
      `,
      returnByValue: true
    });

    await new Promise(r => setTimeout(r, 400));
    const coverShot = await sendCommand('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/snap_cover_page.png', Buffer.from(coverShot.data, 'base64'));
    console.log('Saved scratch/snap_cover_page.png');

    // Scroll to forwarding letter
    await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const el = document.getElementById('forwarding-letter');
          if (el) {
            el.scrollIntoView({ behavior: 'instant', block: 'start' });
          }
        })()
      `
    });
    await new Promise(r => setTimeout(r, 400));
    const letterShot = await sendCommand('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('scratch/snap_forwarding_letter.png', Buffer.from(letterShot.data, 'base64'));
    console.log('Saved scratch/snap_forwarding_letter.png');

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chromeProc.kill();
  }
}

main();
