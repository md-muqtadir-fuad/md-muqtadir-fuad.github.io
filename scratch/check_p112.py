import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ch6_7_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)
t112 = cat['112']['tables'][1]
for idx, r in enumerate(t112):
    cleaned = [c.replace('\n', ' ') if c else '' for c in r]
    print(f"Row {idx:2d} (len {len(r):2d}): {cleaned}")
