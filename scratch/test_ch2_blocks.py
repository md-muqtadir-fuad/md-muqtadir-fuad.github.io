import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(26, 31): # test pages 27 to 31
    page = doc[pno]
    print(f"\n================ PAGE {pno+1} ================")
    blocks = page.get_text('blocks')
    for b in blocks:
        txt = b[4].strip()
        if txt:
            print(f"[{b[1]:.1f} - {b[3]:.1f}] {txt!r}")
