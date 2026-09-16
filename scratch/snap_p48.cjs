const { spawn } = require('child_process');
const fs = require('fs');

const chromeProc = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new',
  '--remote-debugging-port=9459',
  '--disable-gpu',
  '--window-size=1280,900',
  'about:blank'
]);

async function getWsUrl() {
  for (let i = 0; i < 25; i++) {
    try {
      const res = await fetch('http://127.0.0.1:9459/json');
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
  const wsUrl = await getWsUrl();
  const ws = new WebSocket(wsUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  const send = (method, params = {}) => new Promise(resolve => {
    const curId = id++;
    const handler = (e) => {
      const d = JSON.parse(e.data);
      if (d.id === curId) { ws.removeEventListener('message', handler); resolve(d.result); }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id: curId, method, params }));
  });

  await send('Page.enable');
  await send('Page.navigate', { url: 'http://localhost:3000/blog-semi-automated-shoe-cleaning-machine.html' });
  await new Promise(r => setTimeout(r, 2000));

  // Get bounding rect of #page-48
  const evalRes = await send('Runtime.evaluate', {
    expression: `
      (() => {
        const el = document.getElementById('page-48');
        el.scrollIntoView({ block: 'center' });
        const rect = el.getBoundingClientRect();
        return { y: rect.top + window.scrollY, x: rect.left, width: rect.width, height: rect.height };
      })()
    `,
    returnByValue: true
  });

  await new Promise(r => setTimeout(r, 500));

  const yCenter = evalRes.result.value.y;
  const shot = await send('Page.captureScreenshot', {
    format: 'png',
    clip: { x: 0, y: Math.max(0, yCenter - 250), width: 1280, height: 600, scale: 1 }
  });

  fs.writeFileSync('scratch/snap_page_48_53.png', Buffer.from(shot.data, 'base64'));
  console.log('Successfully saved scratch/snap_page_48_53.png');
  ws.close();
  chromeProc.kill();
}
main().catch(err => {
  console.error(err);
  chromeProc.kill();
});
