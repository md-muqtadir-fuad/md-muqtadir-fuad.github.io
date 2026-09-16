const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9446;

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

    // Capture header banner authors
    const bannerShot = await sendCommand('Page.captureScreenshot', {
      format: 'png',
      clip: { x: 0, y: 0, width: 1280, height: 600, scale: 1 }
    });
    fs.writeFileSync('scratch/snap_banner_authors.png', Buffer.from(bannerShot.data, 'base64'));
    console.log('Saved scratch/snap_banner_authors.png');

    // Scroll to page 1 cover card
    const evalRes = await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const cover = document.querySelector('.border.border-black.p-4.bg-gray-50');
          if (cover) {
            const rect = cover.getBoundingClientRect();
            return { x: rect.x, y: window.scrollY + rect.y, width: rect.width, height: rect.height };
          }
          return null;
        })()
      `,
      returnByValue: true
    });

    if (evalRes && evalRes.result && evalRes.result.value) {
      const box = evalRes.result.value;
      await sendCommand('Runtime.evaluate', {
        expression: `window.scrollTo({ top: ${box.y - 100}, behavior: 'instant' })`
      });
      await new Promise(r => setTimeout(r, 400));
      const coverShot = await sendCommand('Page.captureScreenshot', {
        format: 'png',
        clip: { x: Math.max(0, box.x - 20), y: 80, width: box.width + 40, height: box.height + 60, scale: 1 }
      });
      fs.writeFileSync('scratch/snap_cover_authors.png', Buffer.from(coverShot.data, 'base64'));
      console.log('Saved scratch/snap_cover_authors.png');
    }

    // Capture blogs.html card
    await sendCommand('Page.navigate', { url: 'http://localhost:3000/blogs.html' });
    await new Promise(r => setTimeout(r, 1000));
    const blogsShot = await sendCommand('Page.captureScreenshot', {
      format: 'png',
      clip: { x: 0, y: 0, width: 1280, height: 650, scale: 1 }
    });
    fs.writeFileSync('scratch/snap_blogs_authors.png', Buffer.from(blogsShot.data, 'base64'));
    console.log('Saved scratch/snap_blogs_authors.png');

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chromeProc.kill();
  }
}

main();
