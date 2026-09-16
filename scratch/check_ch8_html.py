with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

for p in range(126, 139):
    idx = html.find(f'id="page-{p}"')
    next_idx = html.find(f'id="page-{p+1}"')
    chunk = html[idx:next_idx] if next_idx != -1 else html[idx:idx+2000]
    print(f"\n==================== Page {p} in HTML ({len(chunk)} chars) ====================")
    lines = [l.strip() for l in chunk.split('\n') if l.strip()]
    for l in lines[:12]:
        print("  ", l[:100])
    if len(lines) > 12:
        print(f"  ... and {len(lines)-12} more lines")
