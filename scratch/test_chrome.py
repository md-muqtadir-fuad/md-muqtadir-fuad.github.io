import subprocess
import json
import time
import urllib.request

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
port = 9222

# Launch chrome with remote debugging
cmd = [
    chrome_path,
    "--headless=new",
    f"--remote-debugging-port={port}",
    "--disable-gpu",
    "--window-size=1280,800",
    "http://localhost:3000/blog-semi-automated-shoe-cleaning-machine.html"
]

proc = subprocess.Popen(cmd)
time.sleep(2)

try:
    # Get WebSocket debugger URL
    resp = urllib.request.urlopen(f"http://127.0.0.1:{port}/json").read()
    targets = json.loads(resp)
    ws_url = targets[0]['webSocketDebuggerUrl']
    print("Chrome connected! Target:", targets[0]['title'])

    # We can connect using websockets if installed, or urllib/curl, or simple python script
except Exception as e:
    print("Error connecting:", e)
finally:
    proc.terminate()
