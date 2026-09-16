import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in [45, 46, 52, 53]: # PDF pages 46, 47, 53, 54
    print(f"\n==================== PDF Page {pno+1} ====================")
    print(doc[pno].get_text())
