import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')
for p in range(138, 142):
    print(f"\n==================== PDF PAGE {p+1} (Rep Page {p-19}) ====================")
    text = doc[p].get_text()
    for line in text.split('\n'):
        if line.strip():
            print(repr(line.strip()))
