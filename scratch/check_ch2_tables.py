import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(26, 43):
    page = doc[pno]
    tabs = page.find_tables().tables
    if tabs:
        rows = tabs[0].extract()
        last_row = rows[-1]
        print(f"Page {pno+1} (Q{pno-25}): {len(rows)} rows. Last row: {last_row}")
