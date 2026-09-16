import sys, fitz
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(125, 138): # PDF Pages 126 to 138
    pdf_page = pno + 1
    rep_page = pno - 19
    page = doc[pno]
    print(f"\n============================== PDF Page {pdf_page} (Rep {rep_page}) ==============================")
    tabs = page.find_tables().tables
    print(f"Tables count: {len(tabs)}")
    for t_idx, t in enumerate(tabs):
        data = t.extract()
        print(f"  Table {t_idx} (bbox={t.bbox}): {len(data)} rows x {len(data[0]) if data else 0} cols")
        for r_idx, r in enumerate(data):
            cleaned_r = [c.replace('\n', ' ') if c else '' for c in r]
            print(f"    r{r_idx}: {cleaned_r}")
    imgs = page.get_images(full=True)
    print(f"Images count: {len(imgs)}")
    for img_idx, img in enumerate(imgs):
        print(f"  Image {img_idx}: xref={img[0]}, size={img[2]}x{img[3]}")
    txt = page.get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    print(f"Text sample (first 10 lines):")
    for l in lines[:10]:
        print("  ", l)
