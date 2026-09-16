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
        // Find a reference where link is on the 2nd line
        const ref = document.querySelectorAll('.apa-reference')[1];
        const link = ref.querySelector('a');

        // Test with inline-flex (current)
        const rect1 = link.getBoundingClientRect();

        // Change to inline
        link.className = 'text-blue-700 hover:text-black hover:underline font-mono text-xs font-bold ml-1.5 whitespace-nowrap inline';
        const rect2 = link.getBoundingClientRect();

        // Change to inline-block
        link.className = 'text-blue-700 hover:text-black hover:underline font-mono text-xs font-bold ml-1.5 whitespace-nowrap inline-block';
        const rect3 = link.getBoundingClientRect();

        return {
          withInlineFlex: { left: rect1.left, right: rect1.right },
          withInline: { left: rect2.left, right: rect2.right, diffFromFlex: rect2.left - rect1.left },
          withInlineBlock: { left: rect3.left, right: rect3.right, diffFromFlex: rect3.left - rect1.left }
        };
      })()
    `;

    const res = await sendCommand('Runtime.evaluate', {
      expression: evalCode,
      returnByValue: true
    });

    console.log('Comparison:', JSON.stringify(res.result ? res.result.value : res, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
