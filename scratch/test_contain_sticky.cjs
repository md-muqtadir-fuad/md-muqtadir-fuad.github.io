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
        // Reset all overflow-x on html, body, main
        document.documentElement.style.cssText = '';
        document.body.style.cssText = '';
        const main = document.querySelector('main');
        main.style.overflowX = 'visible';
        main.style.overflowY = 'visible';
        document.documentElement.style.overflowX = 'visible';
        document.documentElement.style.overflowY = 'visible';
        document.body.style.overflowX = 'visible';
        document.body.style.overflowY = 'visible';

        // Remove any style tags we injected earlier or that have !important on html/body
        const injectedStyles = Array.from(document.querySelectorAll('style'));
        // Find our inline style in head
        injectedStyles.forEach(st => {
          if (st.textContent.includes('html, body {')) {
            st.textContent = st.textContent.replace(/html,\\s*body\\s*\\{[^}]*\\}/g, '');
          }
        });

        // Apply contain: paint (or overflow-x: auto; position: relative;) to all .overflow-x-auto containers:
        document.querySelectorAll('.overflow-x-auto').forEach(el => {
          el.style.contain = 'paint';
          el.style.position = 'relative';
          el.style.maxWidth = '100%';
        });

        // Test sticky on aside:
        const aside = document.querySelector('aside');
        const initialTop = aside.getBoundingClientRect().top;
        
        window.scrollTo(0, 1000);
        const scrolledTop = aside.getBoundingClientRect().top;
        const scrollY = window.scrollY;

        // Check horizontal scroll
        const docW = document.documentElement.clientWidth;
        const scrollW = document.documentElement.scrollWidth;

        return {
          scrollY,
          initialTop,
          scrolledTop,
          isStickyWorking: Math.abs(scrolledTop - 96) < 15,
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

    console.log('Result:', JSON.stringify(res.result ? res.result.value : res, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chromeProc.kill();
  }
}

main();
