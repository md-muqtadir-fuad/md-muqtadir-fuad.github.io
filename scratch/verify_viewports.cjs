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

    const viewports = [
      { width: 375, height: 667, name: 'Mobile' },
      { width: 768, height: 1024, name: 'Tablet' },
      { width: 1024, height: 768, name: 'Small Laptop' },
      { width: 1280, height: 800, name: 'Standard Desktop' },
      { width: 1920, height: 1080, name: 'Large Desktop' }
    ];

    const results = [];

    for (const vp of viewports) {
      await sendCommand('Emulation.setDeviceMetricsOverride', {
        width: vp.width,
        height: vp.height,
        deviceScaleFactor: 1,
        mobile: vp.width < 800
      });
      await new Promise(r => setTimeout(r, 500));

      const evalCode = `
        (() => {
          // Scroll to sec-5-3-5-2
          const sec = document.getElementById('sec-5-3-5-2');
          if (sec) sec.scrollIntoView();

          const docW = document.documentElement.clientWidth;
          const scrollW = document.documentElement.scrollWidth;
          const bodyScrollW = document.body.scrollWidth;

          // Attempt to scroll horizontally
          window.scrollTo(1000, window.scrollY);
          const scrollXAfterScroll = window.scrollX;
          window.scrollTo(0, window.scrollY);

          return {
            docW,
            scrollW,
            bodyScrollW,
            hasHorizontalScroll: scrollW > docW,
            scrollXAfterScroll
          };
        })()
      `;

      const evalRes = await sendCommand('Runtime.evaluate', {
        expression: evalCode,
        returnByValue: true
      });

      results.push({
        viewport: vp.name,
        width: vp.width,
        ...evalRes.result.value
      });
    }

    console.log('Multi-viewport test results:', JSON.stringify(results, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
