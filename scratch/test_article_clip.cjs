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
        // Let's test removing overflow-x: hidden from body, main, html
        // and see what happens to sticky AND what happens to scrollWidth!
        
        document.documentElement.style.overflowX = 'visible';
        document.body.style.overflowX = 'visible';
        const main = document.querySelector('main');
        if (main) main.style.overflowX = 'visible';

        // What if we put overflow-x: clip on article?
        const article = document.querySelector('article');
        if (article) {
          article.style.overflowX = 'clip';
          article.style.maxWidth = '100%';
        }

        // Test sticky
        const aside = document.querySelector('aside');
        const beforeScrollTop = aside.getBoundingClientRect().top;

        window.scrollTo(0, 1200);
        const scrolledAsideTop = aside.getBoundingClientRect().top;
        const scrollY = window.scrollY;

        // Check horizontal scroll
        const docW = document.documentElement.clientWidth;
        const scrollW = document.documentElement.scrollWidth;

        window.scrollTo(0, 0);

        return {
          scrollY,
          beforeScrollTop,
          scrolledAsideTop, // Should be ~96px (top-24 = 6rem = 96px)
          isStickyWorking: Math.abs(scrolledAsideTop - 96) < 10,
          docW,
          scrollW,
          hasHorizontalScroll: scrollW > docW
        };
      })()
    `;

    const res = await sendCommand('Runtime.evaluate', {
      expression: evalCode,
      returnByValue: true
    });

    console.log('Result with article overflow-x: clip and main/body/html visible:', JSON.stringify(res.result ? res.result.value : res, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
