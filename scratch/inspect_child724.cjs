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
        const article = document.querySelector('article');
        const child724 = article.children[724];
        
        // Let's inspect child 724
        const outerHtml = child724 ? child724.outerHTML.slice(0, 1000) : 'not found';
        const styles = window.getComputedStyle(child724);

        // Why is child 724 breaking overflow?
        // Let's test various CSS fixes on child 724:
        const tests = {};

        // Test 1: style="overflow-x: auto; width: 100%; max-width: 100%;"
        child724.style.overflowX = 'auto';
        child724.style.width = '100%';
        child724.style.maxWidth = '100%';
        tests.maxWidth100 = document.documentElement.scrollWidth;

        // Test 2: style="position: relative;"
        child724.style.position = 'relative';
        tests.posRelative = document.documentElement.scrollWidth;

        // Test 3: style="contain: paint;" or "overflow: hidden;"
        child724.style.contain = 'paint';
        tests.containPaint = document.documentElement.scrollWidth;

        // Test 4: style="contain: layout paint;"
        child724.style.contain = 'layout paint';
        tests.containLayoutPaint = document.documentElement.scrollWidth;

        // Reset
        child724.style.cssText = '';

        // Test 5: What if table has width: max-content or something?
        const table = child724.querySelector('table');
        const tableStyle = table ? window.getComputedStyle(table) : null;

        // Test 6: Check KaTeX inside table
        const katexInTable = child724.querySelectorAll('.katex');
        
        // Let's test if .katex or something inside the table has position: absolute or something sticking out:
        const allInside = Array.from(child724.querySelectorAll('*'));
        const wideInside = allInside.filter(el => {
          const rect = el.getBoundingClientRect();
          return rect.right > 1280;
        }).map(el => ({
          tag: el.tagName,
          className: el.className.toString().slice(0, 50),
          rectRight: el.getBoundingClientRect().right,
          rectLeft: el.getBoundingClientRect().left,
          position: window.getComputedStyle(el).position
        })).slice(0, 10);

        return {
          child724Tag: child724.tagName,
          child724Class: child724.className,
          tests,
          outerHtml,
          katexCount: katexInTable.length,
          wideInsideCount: wideInside.length,
          wideInside
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
