import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(45, 54):
    pdf_page = pno + 1
    page = doc[pno]
    print(f"\n==================== PDF Page {pdf_page} (Rep {pno-19}) ====================")
    blocks = page.get_text("blocks")
    for b in blocks:
        if b[6] == 0:
            txt = b[4].strip()
            if txt:
                print("--- Block ---")
                print(txt[:300])
