import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ch6_7_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

for p, pinfo in cat.items():
    for t_idx, t in enumerate(pinfo['tables']):
        r0 = t[0] if t else []
        r1 = t[1] if len(t) > 1 else []
        if any('positive decision' in str(c).lower() for c in r0):
            print(f"\n==================== Page {p} Table {t_idx} (DL) ====================")
            for idx, r in enumerate(t):
                c_name = (r[0] or '').replace('\n', ' ')
                print(f"Row {idx:2d}: col0='{c_name}' | non-empty={sum(1 for x in r if x)}")
        elif any('scaled' in str(c).lower() or 'weighted' in str(c).lower() for c in r0 + r1):
            print(f"\n==================== Page {p} Table {t_idx} (PI) ====================")
            for idx, r in enumerate(t):
                c_name = (r[0] or '').replace('\n', ' ')
                print(f"Row {idx:2d}: col0='{c_name}' | non-empty={sum(1 for x in r if x)}")
