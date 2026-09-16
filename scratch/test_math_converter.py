import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
from build_math_latex import format_paragraph_with_math

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'<div class="font-mono text-sm bg-gray-50 border border-black p-3 my-3 text-black overflow-x-auto">(.*?)</div>', c, re.DOTALL)
print(f"Total raw boxes: {len(matches)}")
math_blocks = 0
paragraphs = 0
for m in matches:
    res = format_paragraph_with_math(m)
    if 'math-block' in res:
        math_blocks += 1
    else:
        paragraphs += 1

print(f"Converted into math-block ($$ LaTeX $$): {math_blocks}")
print(f"Converted into semantic prose / parameter badges: {paragraphs}")
