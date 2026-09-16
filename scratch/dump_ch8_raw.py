import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

with open('scratch/ch8_raw_text.txt', 'w', encoding='utf-8') as f:
    for pno in range(125, 138):
        pdf_p = pno + 1
        rep_p = pno - 19
        txt = doc[pno].get_text()
        f.write(f"\n================================================================================\n")
        f.write(f"PDF PAGE {pdf_p} (Report Page {rep_p})\n")
        f.write(f"================================================================================\n")
        f.write(txt)

print("Saved scratch/ch8_raw_text.txt successfully!")
