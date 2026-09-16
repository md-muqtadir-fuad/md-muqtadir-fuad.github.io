import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(26, 43):
    page = doc[pno]
    tabs = page.find_tables().tables
    blocks = page.get_text('blocks')
    
    # Find figure caption
    fig_cap = None
    for b in blocks:
        if b[4].strip().startswith('Figure 2.'):
            fig_cap = fitz.Rect(b[:4])
            break
            
    # Find table caption and rows
    tab_cap = None
    for b in blocks:
        if b[4].strip().startswith('Table 2.'):
            tab_cap = fitz.Rect(b[:4])
            break

    # Find the image xref
    imgs = page.get_images()
    img_rects = page.get_image_rects(imgs[0][0]) if imgs else []
    
    print(f"Page {pno+1}: img_rect={img_rects[0] if img_rects else None}, fig_cap={fig_cap}")
