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

    // Test removing or hiding elements to see which one brings scrollWidth down to 1256
    const evalCode = `
      (() => {
        const initialScrollWidth = document.documentElement.scrollWidth;
        const initialClientWidth = document.documentElement.clientWidth;

        // Let's test hiding major sections to locate what causes scrollWidth to be 2193
        const sections = Array.from(document.querySelectorAll('main > * , article > *'));
        const culprits = [];

        // Check if hiding all tables with min-w-[1500px] fixes it:
        const wideTables = Array.from(document.querySelectorAll('table.min-w-\\\\[1500px\\\\]'));
        wideTables.forEach(t => t.style.display = 'none');
        const afterHidingWideTables = document.documentElement.scrollWidth;
        wideTables.forEach(t => t.style.display = '');

        // Check if hiding the whole article fixes it:
        const article = document.querySelector('article');
        article.style.display = 'none';
        const afterHidingArticle = document.documentElement.scrollWidth;
        article.style.display = '';

        // Check each child of article:
        const children = Array.from(article.children);
        const childEffects = [];
        for (let i = 0; i < children.length; i++) {
          const child = children[i];
          child.style.display = 'none';
          const sw = document.documentElement.scrollWidth;
          child.style.display = '';
          if (sw < initialScrollWidth) {
            childEffects.push({
              index: i,
              tag: child.tagName,
              id: child.id,
              className: child.className.slice(0, 50),
              swIfHidden: sw,
              reduction: initialScrollWidth - sw
            });
          }
        }

        // Also test applying overflow-x: hidden to html, body, main, article:
        document.documentElement.style.overflowX = 'hidden';
        const swWithHtmlHidden = document.documentElement.scrollWidth;
        document.documentElement.style.overflowX = '';

        document.body.style.overflowX = 'hidden';
        const swWithBodyHidden = document.documentElement.scrollWidth;
        document.body.style.overflowX = '';

        return {
          initialScrollWidth,
          initialClientWidth,
          afterHidingWideTables,
          afterHidingArticle,
          childEffects,
          swWithHtmlHidden,
          swWithBodyHidden
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
