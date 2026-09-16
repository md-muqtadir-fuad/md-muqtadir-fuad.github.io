import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'<div class="font-mono text-sm bg-gray-50 border border-black p-3 my-3 text-black overflow-x-auto">(.*?)</div>', c, re.DOTALL)
print(f"Total current raw math boxes: {len(matches)}")
for i, m in enumerate(matches):
    print(f"[{i+1}] {m.strip()[:140]}")
