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

    // Test a container at 700px width with text-indent: -2rem and padding-left: 2rem
    const evalCode = `
      (() => {
        // Let's create an exact test element matching the user's rendering
        const div = document.createElement('div');
        div.className = 'apa-reference pl-8 -indent-8 font-serif text-sm text-gray-800 leading-relaxed mb-4';
        div.style.width = '700px';
        div.innerHTML = \`
          <span class="font-medium">University Grants Commission of Bangladesh. (2024).</span>
          <span class="italic">List of recognized private universities in Bangladesh.</span>
          <span>UGC Institutional Directory.</span>
          <span class="text-gray-600" id="test-note"> (Total institutions: 115)</span>
          <a id="test-link" href="#" class="text-blue-700 font-mono text-xs font-bold inline-flex items-center gap-0.5 ml-1">[LINK]</a>
        \`;
        document.body.appendChild(div);

        const noteSpan = document.getElementById('test-note');
        const linkEl = document.getElementById('test-link');

        const noteRange = document.createRange();
        noteRange.selectNodeContents(noteSpan);
        const noteRects = Array.from(noteRange.getClientRects());
        const lastNoteRect = noteRects[noteRects.length - 1];

        const linkRect = linkEl.getBoundingClientRect();

        // Now test changing display of link to inline
        linkEl.style.display = 'inline';
        const linkRectInline = linkEl.getBoundingClientRect();

        // Now test changing display of link to inline-block
        linkEl.style.display = 'inline-block';
        const linkRectInlineBlock = linkEl.getBoundingClientRect();

        div.remove();

        return {
          lastNoteRect: { right: lastNoteRect.right, top: lastNoteRect.top, bottom: lastNoteRect.bottom },
          linkWithInlineFlex: { left: linkRect.left, top: linkRect.top, overlap: lastNoteRect.right - linkRect.left },
          linkWithInline: { left: linkRectInline.left, top: linkRectInline.top, overlap: lastNoteRect.right - linkRectInline.left },
          linkWithInlineBlock: { left: linkRectInlineBlock.left, top: linkRectInlineBlock.top, overlap: lastNoteRect.right - linkRectInlineBlock.left }
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
