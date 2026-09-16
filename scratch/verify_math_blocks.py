import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    c = f.read()

math_blocks = re.findall(r'<div class="math-block[^"]*">(.*?)</div>', c, re.DOTALL)
print(f"Total LaTeX math-block elements: {len(math_blocks)}")
for i, mb in enumerate(math_blocks[:8]):
    print(f"\n--- Math Block {i+1} ---")
    print(mb.strip())

raw_boxes = re.findall(r'<div class="font-mono text-sm bg-gray-50 border border-black p-3 my-3 text-black overflow-x-auto">(.*?)</div>', c, re.DOTALL)
print(f"\nRemaining raw monospace boxes: {len(raw_boxes)}")

print(f"Total $$ pairs (display math): {c.count('$$') // 2}")
print(f"Total $ symbols (inline & display math): {c.count('$')}")
