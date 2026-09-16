const { spawn } = require('child_process');
const fs = require('fs');

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

    // Scroll to the second apa-reference
    await sendCommand('Runtime.evaluate', {
      expression: `
        const refs = document.querySelectorAll('.apa-reference');
        if (refs[2]) {
          refs[2].scrollIntoView({ block: 'center' });
        }
      `
    });
    await new Promise(r => setTimeout(r, 1000));

    const shot = await sendCommand('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('c:/Users/DELL/Desktop/venv-python/portfolio-ai/portfolio-static/md-muqtadir-fuad.github.io/scratch/ref_screenshot.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved screenshot to scratch/ref_screenshot.png');

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
