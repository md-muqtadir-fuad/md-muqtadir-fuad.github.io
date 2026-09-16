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
        const refs = Array.from(document.querySelectorAll('.apa-reference'));
        const overlaps = [];

        refs.forEach((ref, idx) => {
          const link = ref.querySelector('a');
          if (!link) return;
          const linkRect = link.getBoundingClientRect();

          // Get all text and spans inside ref
          const spans = Array.from(ref.querySelectorAll('span'));
          const lastSpan = spans[spans.length - 1];
          const lastSpanRect = lastSpan ? lastSpan.getBoundingClientRect() : null;

          // Check if link overlaps lastSpan or preceding text
          // Create a range for the last text before link
          const range = document.createRange();
          if (lastSpan) {
            range.selectNodeContents(lastSpan);
            const rangeRects = Array.from(range.getClientRects());
            const lastRect = rangeRects[rangeRects.length - 1];
            if (lastRect) {
              const isOverlapping = (
                linkRect.top < lastRect.bottom &&
                linkRect.bottom > lastRect.top &&
                linkRect.left < lastRect.right
              );
              overlaps.push({
                idx,
                text: ref.textContent.slice(0, 50),
                linkLeft: Math.round(linkRect.left),
                linkTop: Math.round(linkRect.top),
                lastTextRight: Math.round(lastRect.right),
                lastTextTop: Math.round(lastRect.top),
                isOverlapping,
                overlapPx: Math.round(lastRect.right - linkRect.left)
              });
            }
          }
        });

        return { overlaps: overlaps.slice(0, 10) };
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
