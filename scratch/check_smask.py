import fitz
import os
from PIL import Image

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')
out_dir = r'c:\Users\DELL\Desktop\venv-python\portfolio-ai\portfolio-static\md-muqtadir-fuad.github.io\assets\images\pd-report'

# Let's check how many images have smask
smask_count = 0
for pno in range(len(doc)):
    page = doc[pno]
    for img in page.get_images():
        if img[1] != 0: # smask xref is non-zero
            smask_count += 1

print(f"Total images with soft-mask (smask): {smask_count}")
