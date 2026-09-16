with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

for p in [48, 49, 50, 51, 52]:
    idx = html.find(f'id="page-{p}"')
    next_idx = html.find(f'id="page-{p+1}"')
    chunk = html[idx:next_idx]
    # Check if there are <p> or other non-table tags
    print(f"=== Page {p} Tags ===")
    tags = [line.strip() for line in chunk.split('\n') if line.strip().startswith('<p')]
    print(f"Paragraph count: {len(tags)}")
    for t in tags[:5]:
        print("  ", t)
