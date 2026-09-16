const { spawn } = require('child_process');
const fs = require('fs');

const chromeProc = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
  '--headless=new',
  '--remote-debugging-port=9455',
  '--disable-gpu',
  '--window-size=1280,900',
  'about:blank'
]);

async function main() {
  await new Promise(r => setTimeout(r, 600));
  const res = await fetch('http://127.0.0.1:9455/json');
  const data = await res.json();
  const ws = new WebSocket(data[0].webSocketDebuggerUrl);
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
  await new Promise(r => setTimeout(r, 1500));

  // Scroll to #page-48
  await send('Runtime.evaluate', {
    expression: "document.getElementById('page-48').scrollIntoView({ block: 'center' });"
  });
  await new Promise(r => setTimeout(r, 600));

  const shot = await send('Page.captureScreenshot', {
    format: 'png',
    clip: { x: 0, y: 0, width: 1280, height: 800, scale: 1 }
  });
  fs.writeFileSync('scratch/snap_page_48_53.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved scratch/snap_page_48_53.png');
  ws.close();
  chromeProc.kill();
}
main();
