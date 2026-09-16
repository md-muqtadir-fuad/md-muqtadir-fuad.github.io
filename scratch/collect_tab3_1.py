import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

all_rows = []
for pno in range(46, 52): # Pages 47 to 52
    page = doc[pno]
    tabs = page.find_tables().tables
    if tabs:
        tdata = tabs[0].extract()
        print(f"Page {pno+1}: {len(tdata)} rows")
        if pno == 46:
            # First page has header row 0
            header = [c.replace('\n', ' ') if c else '' for c in tdata[0]]
            print("  Header:", header)
            data_rows = tdata[1:]
        else:
            data_rows = tdata
        for r_idx, r in enumerate(data_rows):
            cleaned = [c.replace('\n', ' ').strip() if c else '' for c in r]
            print(f"  P{pno+1} r{r_idx}: {cleaned}")
            all_rows.append((pno+1, cleaned))

print(f"\nTotal rows collected: {len(all_rows)}")
