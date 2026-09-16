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
        const links = Array.from(document.querySelectorAll('.apa-reference a'));
        if (!links.length) return { error: 'no apa links found' };

        const firstLink = links[0];
        const rect = firstLink.getBoundingClientRect();
        const style = window.getComputedStyle(firstLink);
        const parent = firstLink.parentElement;
        const parentStyle = window.getComputedStyle(parent);

        // Check the text node right before this link:
        const prevSpan = firstLink.previousElementSibling;
        const prevRect = prevSpan ? prevSpan.getBoundingClientRect() : null;

        return {
          linkOuter: firstLink.outerHTML,
          linkRect: { left: rect.left, right: rect.right, width: rect.width },
          prevSpanOuter: prevSpan ? prevSpan.outerHTML : null,
          prevRect: prevRect ? { left: prevRect.left, right: prevRect.right, width: prevRect.width } : null,
          display: style.display,
          marginLeft: style.marginLeft,
          position: style.position,
          parentIndent: parentStyle.textIndent,
          parentPaddingLeft: parentStyle.paddingLeft
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
