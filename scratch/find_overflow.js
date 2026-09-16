import { spawn } from 'child_process';
import http from 'http';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const port = 9333;

const chromeProc = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--window-size=1280,800',
  'http://localhost:3000/blog-semi-automated-shoe-cleaning-machine.html'
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
    await new Promise(r => setTimeout(r, 4000));

    const evalCode = `
      (() => {
        const table = document.querySelector('table.min-w-\\\\[1500px\\\\]');
        if (!table) return { error: 'table not found' };

        const ancestors = [];
        let curr = table;
        while (curr) {
          const style = window.getComputedStyle(curr);
          const rect = curr.getBoundingClientRect();
          ancestors.push({
            tag: curr.tagName,
            id: curr.id,
            className: curr.className,
            offsetWidth: curr.offsetWidth,
            scrollWidth: curr.scrollWidth,
            clientWidth: curr.clientWidth,
            rectWidth: rect.width,
            rectRight: rect.right,
            overflowX: style.overflowX,
            maxWidth: style.maxWidth,
            minWidth: style.minWidth,
            width: style.width,
            display: style.display
          });
          curr = curr.parentElement;
        }
        return { ancestors };
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
