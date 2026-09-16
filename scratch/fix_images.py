import fitz
import os
from PIL import Image

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')
out_dir = r'c:\Users\DELL\Desktop\venv-python\portfolio-ai\portfolio-static\md-muqtadir-fuad.github.io\assets\images\pd-report'

# Re-extract and render all images properly
# If an image has an smask or when rendered on page, render the exact page image rect with white background!
for pno in range(len(doc)):
    page = doc[pno]
    imgs = page.get_images(full=True)
    for i, item in enumerate(imgs):
        xref = item[0]
        smask = item[1]
        rects = page.get_image_rects(xref)
        ext = 'png'
        fname = f'page_{pno+1:03d}_img_{i+1}_{xref}.png'
        fpath = os.path.join(out_dir, fname)
        
        if rects:
            # Render the image clip directly from the page with alpha=False (white background)
            # Use 200 DPI for high resolution
            rect = rects[0]
            pix = page.get_pixmap(clip=rect, dpi=200, alpha=False)
            pix.save(fpath)
        else:
            # Fallback to extract_image
            base_img = doc.extract_image(xref)
            ext = base_img['ext']
            fname = f'page_{pno+1:03d}_img_{i+1}_{xref}.{ext}'
            fpath = os.path.join(out_dir, fname)
            with open(fpath, 'wb') as f:
                f.write(base_img['image'])

print("Successfully re-rendered all images with clean white backgrounds!")
