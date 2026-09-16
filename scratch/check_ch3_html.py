import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find pages 46 to 54
for p in range(46, 55):
    idx = html.find(f'id="page-{p}"')
    next_idx = html.find(f'id="page-{p+1}"')
    if idx != -1:
        chunk = html[idx:next_idx] if next_idx != -1 else html[idx:idx+2000]
        print(f"\n==================== Page {p} in HTML ({len(chunk)} chars) ====================")
        lines = [l.strip() for l in chunk.split('\n') if l.strip()]
        for l in lines[:15]:
            print("  ", l[:100])
        if len(lines) > 15:
            print(f"  ... and {len(lines)-15} more lines")
