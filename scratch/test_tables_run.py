import json
import fitz
from build_ch6_ch7_tables import get_ch6_7_table_html

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

with open('scratch/ch6_7_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

rendered_count = 0
skipped_count = 0
for page_str, page_info in cat.items():
    pno = int(page_str)
    tabs = page_info['tables']
    caps = page_info['captions']
    for t_idx, tab_data in enumerate(tabs):
        res = get_ch6_7_table_html(pno, t_idx, tab_data, doc)
        if res == "":
            print(f"Page {pno} Table {t_idx}: SKIPPED (orphan or empty)")
            skipped_count += 1
        else:
            table_type = "UNKNOWN"
            if 'Relative Emphasis' in res:
                table_type = "DIGITAL LOGIC"
            elif 'Weighting Factor' in res:
                table_type = "PERFORMANCE INDEX"
            elif 'Table 6.1' in str(caps) or pno == 97:
                table_type = "CH6 MATERIAL"
            elif 'Table 6.2' in str(caps) or pno == 98:
                table_type = "CH6 MANUFACTURING"
            elif 'Table 6.3' in str(caps) or pno == 99:
                table_type = "CH6 JOINING"
            else:
                table_type = "STANDARD"
            print(f"Page {pno} Table {t_idx}: RENDERED [{table_type}] ({len(res)} chars)")
            rendered_count += 1

print(f"\nTotal Rendered: {rendered_count}, Total Skipped: {skipped_count}")
