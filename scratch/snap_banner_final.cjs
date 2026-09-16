const { spawn } = require('child_process');
const fs = require('fs');

const chromeProc = spawn('C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe', [
  '--headless=new',
  '--remote-debugging-port=9449',
  '--disable-gpu',
  '--window-size=1280,750',
  'about:blank'
]);

async function getWsUrl() {
  for (let i = 0; i < 20; i++) {
    try {
      const res = await fetch('http://127.0.0.1:9449/json');
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
  await new Promise(r => setTimeout(r, 1200));

  const shot = await send('Page.captureScreenshot', {
    format: 'png',
    clip: { x: 0, y: 0, width: 1280, height: 600, scale: 1 }
  });
  fs.writeFileSync('scratch/snap_banner_bw_final.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved scratch/snap_banner_bw_final.png');

  ws.close();
  chromeProc.kill();
}

main();
