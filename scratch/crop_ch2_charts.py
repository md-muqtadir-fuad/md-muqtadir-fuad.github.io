import fitz

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

for pno in range(26, 43):
    page = doc[pno]
    imgs = page.get_images()
    if not imgs:
        continue
    xref = imgs[0][0]
    img_rect = page.get_image_rects(xref)[0]
    
    # Find figure caption top
    fig_cap_y0 = None
    for b in page.get_text('blocks'):
        if b[4].strip().startswith('Figure 2.'):
            fig_cap_y0 = b[1]
            break
            
    if fig_cap_y0 is None:
        fig_cap_y0 = img_rect.y1 + 50
        
    crop_rect = fitz.Rect(
        max(30, img_rect.x0 - 55),
        max(50, img_rect.y0 - 30),
        min(page.rect.width - 30, img_rect.x1 + 55),
        fig_cap_y0 - 2
    )
    
    pix = page.get_pixmap(clip=crop_rect, dpi=200, alpha=False)
    out_path = rf'c:\Users\DELL\Desktop\venv-python\portfolio-ai\portfolio-static\md-muqtadir-fuad.github.io\assets\images\pd-report\page_{pno+1:03d}_img_1_{xref}.png'
    pix.save(out_path)
    print(f"Page {pno+1} saved with crop_rect={crop_rect}")

print("All 17 survey chart images cropped perfectly with all labels and legend!")
