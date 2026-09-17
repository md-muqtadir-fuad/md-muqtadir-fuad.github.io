import os
import sys
import re
import html
import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_appendix_reference import get_appendix_a_html, get_appendix_b_html, get_references_html
from build_math_latex import format_paragraph_with_math, format_table_cell
from build_ch6_ch7_tables import get_ch6_7_table_html
from build_ch1 import get_ch1_html
from build_ch2 import get_ch2_html
from build_ch3 import get_ch3_page_html
from build_ch4 import get_ch4_html
from build_ch8 import get_ch8_page_html
from build_ch9 import get_ch9_page_html

AUTHORS_DATA = [
    {
        "name": "Md. Muqtadir Fuad",
        "id": "2008079",
        "linkedin": "https://www.linkedin.com/in/md-muqtadir-fuad/",
        "is_primary": True
    },
    {
        "name": "Abdullah Al Mazid",
        "id": "2008080",
        "linkedin": "https://www.linkedin.com/in/abdullahalmazid/",
        "is_primary": False
    },
    {
        "name": "Md. Ashiqur Rahman Noor",
        "id": "2008081",
        "linkedin": "https://www.linkedin.com/in/ashiqur-rahman-noor/",
        "is_primary": False
    },
    {
        "name": "Md Sadiqul Haque",
        "id": "2008082",
        "linkedin": "https://www.linkedin.com/in/mdsadiqulhaquee/",
        "is_primary": False
    },
    {
        "name": "Ananya Halder",
        "id": "2008083",
        "linkedin": "https://www.linkedin.com/in/ananyahalder01/",
        "is_primary": False
    },
    {
        "name": "Yashna Noor",
        "id": "2008084",
        "linkedin": "https://www.linkedin.com/in/yashna-noor-csca23456/",
        "is_primary": False
    }
]

LINKEDIN_ICON_SVG = '<svg class="w-3.5 h-3.5 inline-block shrink-0 rounded-[2px]" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect width="24" height="24" rx="4" fill="#000000"/><path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/></svg>'

def get_author_in_badge(url, name):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="in-badge" title="LinkedIn: {name}" aria-label="LinkedIn: {name}">{LINKEDIN_ICON_SVG}</a>'

def build_clean_html():
    pdf_path = r'C:\Users\DELL\Downloads\pd_report.pdf'
    doc = fitz.open(pdf_path)
    output_html_path = r'c:\Users\DELL\Desktop\venv-python\portfolio-ai\portfolio-static\md-muqtadir-fuad.github.io\blog-semi-automated-shoe-cleaning-machine.html'
    img_dir = r'c:\Users\DELL\Desktop\venv-python\portfolio-ai\portfolio-static\md-muqtadir-fuad.github.io\assets\images\pd-report'
    
    # 1. Map figures to images on body pages (page >= 20)
    fig_to_img = {}
    for pno in range(20, len(doc)):
        page = doc[pno]
        text = page.get_text()
        imgs = page.get_images(full=True)
        matches = re.findall(r'(Figure\s+\d+\s*\.\s*\d+\s*:[^\n]+)', text)
        if matches:
            for i, fig in enumerate(matches):
                clean_fig = ' '.join(fig.split())
                if pno == 133: # Page 134: Break Even Analysis vector chart
                    fig_to_img[clean_fig] = '/assets/images/pd-report/figure_8_1_break_even_chart.png'
                elif i < len(imgs):
                    xref = imgs[i][0]
                    # The re-rendered clean png filename
                    fname = f'page_{pno+1:03d}_img_{i+1}_{xref}.png'
                    fig_to_img[clean_fig] = f'/assets/images/pd-report/{fname}'

    print(f"Mapped {len(fig_to_img)} figures for body pages.")

    def clean_str(s):
        if not s:
            return ""
        s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl').replace('\ufb00', 'ff')
        s = s.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
        s = s.replace('\ufffd', "'")
        return s

    def get_report_page_num(pno):
        pdf_page = pno + 1
        if pdf_page == 1:
            return "Cover"
        elif pdf_page == 2:
            return "Title & Faculty"
        elif pdf_page == 3:
            return "I"
        elif pdf_page == 4:
            return "II"
        elif pdf_page == 5:
            return "III"
        elif pdf_page == 6:
            return "IV"
        elif pdf_page == 7:
            return "V"
        elif 8 <= pdf_page <= 13:
            romans = ["i", "ii", "iii", "iv", "v", "vi"]
            return romans[pdf_page - 8]
        elif 14 <= pdf_page <= 17:
            romans = ["vii", "viii", "ix", "x"]
            return romans[pdf_page - 14]
        elif 18 <= pdf_page <= 20:
            romans = ["xi", "xii", "xiii"]
            return romans[pdf_page - 18]
        else:
            return str(pdf_page - 20)

    all_content_html = []

    for pno in range(len(doc)):
        page = doc[pno]
        pdf_page = pno + 1
        rep_page = get_report_page_num(pno)

        # --- Chapter 1 (PDF Pages 21 to 25): Consolidated and semantically cleaned ---
        if pdf_page == 21:
            page_html = []
            page_html.append('<div class="pdf-page-marker my-10 pt-4 border-t-2 border-black/20 text-xs font-mono text-gray-500 flex justify-between items-center" id="page-21">')
            page_html.append('  <span id="page-22"></span><span id="page-23"></span><span id="page-24"></span><span id="page-25"></span>')
            page_html.append('  <span class="font-bold">Report Pages 1-5</span>')
            page_html.append('  <span>PDF Pages 21-25 / 151</span>')
            page_html.append('</div>\n')
            page_html.append(get_ch1_html())
            all_content_html.append('\n'.join(page_html))
            continue

        if 22 <= pdf_page <= 25:
            continue

        # --- Chapter 2 (PDF Pages 26 to 45): Consolidated survey presentation ---
        if pdf_page == 26:
            page_html = []
            page_html.append('<div class="pdf-page-marker my-10 pt-4 border-t-2 border-black/20 text-xs font-mono text-gray-500 flex justify-between items-center" id="page-26">')
            page_html.append('  ' + ''.join(f'<span id="page-{page}"></span>' for page in range(27, 46)))
            page_html.append('  <span class="font-bold">Report Pages 6-25</span>')
            page_html.append('  <span>PDF Pages 26-45 / 151</span>')
            page_html.append('</div>\n')
            page_html.append(get_ch2_html())
            all_content_html.append('\n'.join(page_html))
            continue

        if 27 <= pdf_page <= 45:
            continue
        
        # --- PDF Pages 48 to 53 (Report Pages 28 to 33): Consolidated Range ---
        if pdf_page == 48:
            page_html = []
            page_html.append(f'<div class="pdf-page-marker my-10 pt-4 border-t-2 border-black/20 text-xs font-mono text-gray-500 flex justify-between items-center" id="page-48">')
            page_html.append('  <span id="page-49"></span><span id="page-50"></span><span id="page-51"></span><span id="page-52"></span><span id="page-53"></span>')
            page_html.append('  <span class="font-bold">Report Pages 28–33</span>')
            page_html.append('  <span>PDF Pages 48–53 / 151</span>')
            page_html.append('</div>\n')
            
            ch3_html = get_ch3_page_html(53)
            if ch3_html:
                page_html.append(ch3_html)
            all_content_html.append('\n'.join(page_html))
            continue

        if 49 <= pdf_page <= 53:
            continue

        # --- Chapter 4 (PDF Pages 55 to 59): Consolidated functional decomposition ---
        if pdf_page == 55:
            page_html = []
            page_html.append('<div class="pdf-page-marker my-10 pt-4 border-t-2 border-black/20 text-xs font-mono text-gray-500 flex justify-between items-center" id="page-55">')
            page_html.append('  ' + ''.join(f'<span id="page-{page}"></span>' for page in range(56, 60)))
            page_html.append('  <span class="font-bold">Report Pages 35-39</span>')
            page_html.append('  <span>PDF Pages 55-59 / 151</span>')
            page_html.append('</div>\n')
            page_html.append(get_ch4_html())
            all_content_html.append('\n'.join(page_html))
            continue

        if 56 <= pdf_page <= 59:
            continue

        page_html = []
        page_html.append(f'<div class="pdf-page-marker my-10 pt-4 border-t-2 border-black/20 text-xs font-mono text-gray-500 flex justify-between items-center" id="page-{pdf_page}">')
        page_html.append(f'  <span class="font-bold">Report Page {rep_page}</span>')
        page_html.append(f'  <span>PDF Page {pdf_page} / 151</span>')
        page_html.append(f'</div>\n')

        # --- Cover Page (PDF Page 1) ---
        if pdf_page == 1:
            page_html.append('<div class="text-center py-12 border-2 border-black p-8 bg-gray-50 my-6">')
            page_html.append('  <div class="mb-6"><img src="/assets/images/pd-report/page_001_img_2_31.png" alt="BUET Logo" class="mx-auto h-24 object-contain" /></div>')
            page_html.append('  <h2 class="font-mono text-lg tracking-wider font-bold mb-2">BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY</h2>')
            page_html.append('  <h3 class="font-mono text-md font-semibold text-gray-700 mb-8">DEPARTMENT OF INDUSTRIAL AND PRODUCTION ENGINEERING</h3>')
            page_html.append('  <p class="font-mono text-sm tracking-widest text-gray-600 mb-2">IPE 304</p>')
            page_html.append('  <p class="font-mono text-xs uppercase text-gray-500 mb-6">A Report On</p>')
            page_html.append('  <h1 class="text-3xl md:text-5xl font-bold font-mono tracking-tight mb-8">Semi-Automated Shoe Cleaning Machine</h1>')
            page_html.append('  <div class="my-8"><img src="/assets/images/pd-report/page_001_img_1_30.png" alt="CAD Model of Semi-Automated Shoe Cleaning Machine" class="mx-auto max-h-[350px] border border-black object-contain shadow-sm" /></div>')
            page_html.append('</div>\n')
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Title & Faculty Page (PDF Page 2) ---
        if pdf_page == 2:
            page_html.append('<div class="border border-black p-8 my-6 bg-white space-y-6 font-mono">')
            page_html.append('  <div class="text-center border-b border-black pb-6">')
            page_html.append('    <p class="text-xs uppercase text-gray-500 mb-1">A Report On</p>')
            page_html.append('    <h2 class="text-2xl md:text-3xl font-bold tracking-tight">Semi-Automated Shoe Cleaning Machine</h2>')
            page_html.append('    <p class="text-sm text-gray-700 mt-2"><strong>Course No:</strong> IPE 304 | <strong>Course Title:</strong> Product Design-II Sessional</p>')
            page_html.append('    <p class="text-sm text-gray-700"><strong>Date of Submission:</strong> 15-12-2024</p>')
            page_html.append('  </div>')
            page_html.append('  <div class="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">')
            page_html.append('    <div class="border border-black p-4 bg-gray-50">')
            page_html.append('      <h3 class="font-bold text-sm uppercase tracking-wider mb-4 border-b border-black pb-1">Submitted To</h3>')
            page_html.append('      <ul class="space-y-3 text-xs leading-relaxed">')
            page_html.append('        <li><strong>Dr Shuva Ghosh</strong><br><span class="text-gray-600">Associate Professor</span></li>')
            page_html.append('        <li><strong>Dr A.B.M. Mainul Bari</strong><br><span class="text-gray-600">Associate Professor</span></li>')
            page_html.append('        <li><strong>Nafisa Anzum Sristi</strong><br><span class="text-gray-600">Lecturer</span></li>')
            page_html.append('        <li><strong>Zahin Ar Rafi</strong><br><span class="text-gray-600">Lecturer</span></li>')
            page_html.append('      </ul>')
            page_html.append('      <p class="text-xs text-gray-600 mt-4 pt-2 border-t border-gray-300">Department of Industrial and Production Engineering, BUET</p>')
            page_html.append('    </div>')
            page_html.append('    <div class="border border-black p-4 bg-gray-50">')
            page_html.append('      <h3 class="font-bold text-sm uppercase tracking-wider mb-4 border-b border-black pb-1">Submitted By: Group- B14</h3>')
            page_html.append('      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs leading-relaxed">')
            page_html.append('        <li><strong>Md. Muqtadir Fuad</strong><br><span class="text-gray-600">Student ID: 2008079</span></li>')
            page_html.append('        <li><strong>Abdullah Al Mazid</strong><br><span class="text-gray-600">Student ID: 2008080</span></li>')
            page_html.append('        <li><strong>Md. Ashiqur Rahman Noor</strong><br><span class="text-gray-600">Student ID: 2008081</span></li>')
            page_html.append('        <li><strong>Md Sadiqul Haque</strong><br><span class="text-gray-600">Student ID: 2008082</span></li>')
            page_html.append('        <li><strong>Ananya Halder</strong><br><span class="text-gray-600">Student ID: 2008083</span></li>')
            page_html.append('        <li><strong>Yashna Noor</strong><br><span class="text-gray-600">Student ID: 2008084</span></li>')
            page_html.append('      </ul>')
            page_html.append('      <p class="text-xs text-gray-600 mt-4 pt-2 border-t border-gray-300">Department of Industrial and Production Engineering, BUET</p>')
            page_html.append('    </div>')
            page_html.append('  </div>')
            page_html.append('</div>\n')
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Forwarding Letter (PDF Page 4) ---
        if pdf_page == 4:
            page_html.append('<h2 class="text-2xl md:text-3xl font-bold font-mono tracking-tight mt-12 mb-6 pb-2 border-b-2 border-black" id="forwarding-letter">FORWARDING LETTER</h2>')
            page_html.append('<div class="border border-gray-300 p-8 my-6 bg-white space-y-5 font-serif text-sm leading-relaxed text-gray-800 rounded-xs shadow-2xs">')
            page_html.append('  <div class="font-mono text-xs text-gray-600 mb-4"><strong>Date:</strong> December 15, 2024</div>')
            page_html.append('  <div class="font-sans text-xs space-y-1 mb-4 text-gray-700">')
            page_html.append('    <p class="font-semibold text-black">Dr. Shuva Ghosh, <span class="font-normal text-gray-600">Associate Professor</span></p>')
            page_html.append('    <p class="font-semibold text-black">Dr. A.B.M. Mainul Bari, <span class="font-normal text-gray-600">Associate Professor</span></p>')
            page_html.append('    <p class="font-semibold text-black">Nafisa Anzum Sristi, <span class="font-normal text-gray-600">Lecturer</span></p>')
            page_html.append('    <p class="font-semibold text-black">Zahin Ar Rafi, <span class="font-normal text-gray-600">Lecturer</span></p>')
            page_html.append('    <p class="text-gray-500 font-mono text-[11px] pt-1">Department of Industrial and Production Engineering, BUET</p>')
            page_html.append('  </div>')
            page_html.append('  <div class="font-mono text-xs font-bold text-black border-y border-gray-200 py-2">Subject: Report on &ldquo;Semi-Automated Shoe Cleaning Machine&rdquo;</div>')
            page_html.append('  <p><strong>Honorable Teachers,</strong></p>')
            page_html.append('  <p>It is our great pleasure to present the report entitled &ldquo;Semi-Automated Shoe Cleaning Machine&rdquo; to you. We are very thankful to you for your kind help to accomplish this product design project.</p>')
            page_html.append('  <p>The semi-automated shoe cleaning machine is a unique innovation that combines traditional cleaning methods with modern technology to deliver an efficient and user-friendly experience. By incorporating semi-automated mechanisms, the machine allows users to control the cleaning process, ensuring thorough cleaning and polishing of shoes with minimal effort. In this report, we showcased the functions, working principles, manufacturing processes, and overall costing of the Semi-Automated Shoe Cleaning Machine.</p>')
            page_html.append('  <p>We would like to thank you for your cooperation in completing this project. We solemnly apologize for the involuntary mistakes, if there are any.</p>')
            page_html.append('  <div class="pt-4 mt-6 border-t border-gray-200">')
            page_html.append('    <p class="font-mono text-xs font-semibold mb-3">Sincerely yours,</p>')
            page_html.append('    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 font-mono text-xs">')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Md. Muqtadir Fuad</strong><br><span class="text-gray-500">Student ID: 2008079</span></div>')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Abdullah Al Mazid</strong><br><span class="text-gray-500">Student ID: 2008080</span></div>')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Md. Ashiqur Rahman Noor</strong><br><span class="text-gray-500">Student ID: 2008081</span></div>')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Md Sadiqul Haque</strong><br><span class="text-gray-500">Student ID: 2008082</span></div>')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Ananya Halder</strong><br><span class="text-gray-500">Student ID: 2008083</span></div>')
            page_html.append('      <div class="border-b border-gray-200 pb-1"><strong>Yashna Noor</strong><br><span class="text-gray-500">Student ID: 2008084</span></div>')
            page_html.append('    </div>')
            page_html.append('    <p class="text-xs text-gray-500 font-mono mt-3">Level-3, Term-2 &bull; Department of Industrial and Production Engineering, BUET</p>')
            page_html.append('  </div>')
            page_html.append('</div>\n')
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Index Pages: Pages 8 to 20 (TOC, List of Tables, List of Illustrations) ---
        if 8 <= pdf_page <= 20:
            # We want to format index pages cleanly as index lists with dotted leaders
            # and NOT generate <figure> or chapter headings that conflict with real ones
            text = page.get_text()
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            
            page_html.append('<div class="my-6 p-6 border border-black bg-gray-50/50 font-mono text-xs">')
            for line in lines:
                if line == rep_page or line == str(pdf_page):
                    continue
                line_clean = clean_str(line)
                
                # Check major index headings
                if line_clean == 'TABLE OF CONTENTS':
                    page_html.append(f'  <h3 class="text-lg font-bold uppercase tracking-wider border-b border-black pb-2 mb-4 text-black" id="table-of-contents">{html.escape(line_clean)}</h3>')
                elif line_clean == 'List of Tables':
                    page_html.append(f'  <h3 class="text-lg font-bold uppercase tracking-wider border-b border-black pb-2 mb-4 text-black" id="list-of-tables">{html.escape(line_clean)}</h3>')
                elif line_clean == 'List of Illustrations':
                    page_html.append(f'  <h3 class="text-lg font-bold uppercase tracking-wider border-b border-black pb-2 mb-4 text-black" id="list-of-illustrations">{html.escape(line_clean)}</h3>')
                else:
                    # Look for dotted items: Title ...... Page
                    dot_match = re.match(r'^(.*?)[\s\.]+(\d+|[IVXLCDMivxlcdm]+)$', line_clean)
                    if dot_match:
                        title_part = dot_match.group(1).strip(' .')
                        page_part = dot_match.group(2).strip()
                        page_html.append(f'  <div class="flex justify-between items-baseline py-1 border-b border-gray-200 hover:bg-gray-100 transition-colors">')
                        page_html.append(f'    <span class="text-gray-800 font-medium">{html.escape(title_part)}</span>')
                        page_html.append(f'    <span class="text-gray-500 font-bold ml-4 shrink-0">{html.escape(page_part)}</span>')
                        page_html.append(f'  </div>')
                    else:
                        page_html.append(f'  <div class="py-1 text-gray-700">{html.escape(line_clean)}</div>')
            page_html.append('</div>\n')
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Appendix A: Pages 143 to 146 (Questionnaire in Clean APA Format) ---
        if 143 <= pdf_page <= 146:
            app_a_html = get_appendix_a_html(pdf_page)
            page_html.append(app_a_html)
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Appendix B: Page 147 (Material Constants Tables in APA Format) ---
        if pdf_page == 147:
            app_b_html = get_appendix_b_html()
            page_html.append(app_b_html)
            all_content_html.append('\n'.join(page_html))
            continue

        # --- References: Pages 148 to 151 (APA 7th Edition Style) ---
        if 148 <= pdf_page <= 151:
            ref_html = get_references_html(pdf_page)
            page_html.append(ref_html)
            all_content_html.append('\n'.join(page_html))
            continue

        # --- Chapter 2 Survey Questions: Pages 27 to 43 ---
        if 27 <= pdf_page <= 43:
            # Page 27 has the section title 2.3 Survey Result
            if pdf_page == 27:
                page_html.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-8 mb-3" id="sec-2-3"><span class="text-gray-400 mr-2">2.3</span>Survey Result</h3>')
                page_html.append('<p class="text-base text-gray-800 leading-relaxed mb-6">The survey, involving 34 individuals, is summarized below using pie charts to depict the results and their percentages.</p>')

            # 1. Extract full multi-block question prompt
            q_lines = []
            found_q = False
            q_y1 = 0
            tab_cap_y0 = page.rect.height
            for b in page.get_text('blocks'):
                txt = b[4].strip()
                if re.match(r'^\d+\.\s+', txt):
                    found_q = True
                    q_lines.append(txt)
                    q_y1 = b[3]
                elif found_q:
                    if txt.startswith('o ') or txt.startswith('Table') or txt.startswith('Figure') or txt == 'o':
                        break
                    if not txt.startswith('2.') and not txt.startswith('Chapter'):
                        q_lines.append(txt)
                        q_y1 = b[3]
            prompt = clean_str(' '.join(' '.join(q_lines).split()))

            q_num = str(pdf_page - 26)
            q_text = prompt
            q_match = re.match(r'^(\d+)\.\s*(.*)', prompt)
            if q_match:
                q_num = q_match.group(1)
                q_text = q_match.group(2)

            # Find table cap y0 for bounds
            for b in page.get_text('blocks'):
                txt = b[4].strip()
                if txt.startswith('Table 2.'):
                    tab_cap_y0 = b[1]
                    break

            # 2. Options
            options = []
            for b in page.get_text('blocks'):
                txt = b[4].strip()
                if b[1] >= q_y1 - 2 and b[3] <= tab_cap_y0 + 2:
                    if txt.startswith('Table') or re.match(r'^\d+\.\s+', txt):
                        continue
                    lines = [l.strip() for l in txt.split('\n') if l.strip()]
                    i = 0
                    while i < len(lines):
                        l = lines[i]
                        if l in ['o', '•', '*']:
                            if i + 1 < len(lines):
                                options.append(clean_str(lines[i+1]))
                                i += 2
                                continue
                        elif l.startswith('o ') or l.startswith('• '):
                            options.append(clean_str(l[2:].strip()))
                        elif l.startswith('o') and len(l) > 1 and l[1].isupper():
                            options.append(clean_str(l[1:].strip()))
                        i += 1

            # 3. Table caption & Figure caption
            tab_cap = ""
            fig_cap = ""
            for b in page.get_text('blocks'):
                txt = clean_str(' '.join(b[4].strip().split()))
                if txt.startswith('Table 2.'):
                    tab_cap = txt
                elif txt.startswith('Figure 2.'):
                    fig_cap = txt

            # 4. Table data
            tabs = page.find_tables().tables
            tab_rows = []
            if tabs:
                raw_rows = tabs[0].extract()
                for r in raw_rows:
                    cells = [clean_str(c.strip()) for c in r if c is not None and c.strip()]
                    if not cells:
                        continue
                    if any('\n' in c and ('Daily' in c or 'Weekly' in c or 'Yes' in c or 'Quiet' in c or 'Reviews' in c or '%' in c) for c in cells):
                        continue
                    if 'Option' in cells[0] or (len(cells) >= 2 and any('Response' in c for c in cells)):
                        tab_rows.append(cells)
                    elif len(cells) >= 2:
                        tab_rows.append(cells)

            # 5. Image path
            imgs = page.get_images()
            img_path = f"/assets/images/pd-report/page_{pdf_page:03d}_img_1_{imgs[0][0]}.png" if imgs else ""

            # Render Executive Survey Card
            page_html.append('<div class="survey-card my-6 border border-gray-300 p-5 bg-white shadow-2xs hover:border-black transition-colors rounded-xs">')
            page_html.append('  <div class="flex items-start gap-3 mb-2">')
            page_html.append(f'    <span class="inline-flex items-center justify-center px-2 py-0.5 bg-black text-white font-mono text-xs font-bold shrink-0">Q{q_num}</span>')
            page_html.append(f'    <h4 class="text-base md:text-lg font-bold font-mono text-black leading-snug">{html.escape(q_text)}</h4>')
            page_html.append('  </div>')

            if options:
                page_html.append('  <div class="flex flex-wrap gap-2 mb-5 font-mono text-xs text-gray-700 sm:pl-9">')
                page_html.append('    <span class="text-gray-400 font-semibold uppercase tracking-wider text-[10px] self-center mr-1">Survey Options:</span>')
                for opt in options:
                    page_html.append(f'    <span class="inline-flex items-center gap-1.5 border border-gray-200 px-2.5 py-1 bg-gray-50 text-gray-800 rounded-xs"><span class="w-1.5 h-1.5 rounded-full bg-black inline-block"></span><span>{html.escape(opt)}</span></span>')
                page_html.append('  </div>')

            page_html.append('  <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">')

            # Table column (7 cols on lg)
            page_html.append('    <div class="lg:col-span-7">')
            if tab_cap:
                page_html.append(f'      <div class="font-mono text-xs uppercase font-bold text-gray-800 mb-2 flex items-center gap-1.5"><span class="w-2 h-2 bg-black inline-block"></span><span>{html.escape(tab_cap)}</span></div>')
            if tab_rows:
                page_html.append('      <div class="overflow-x-auto relative max-w-full border border-black">')
                page_html.append('        <table class="w-full border-collapse font-mono text-xs text-left bg-white">')
                header = tab_rows[0]
                page_html.append('          <thead><tr class="bg-gray-100 text-black border-b border-black">')
                for idx_col, col in enumerate(header):
                    align = 'text-right' if idx_col > 0 else 'text-left'
                    page_html.append(f'            <th class="border border-black p-2 font-bold uppercase {align}">{html.escape(col).replace(chr(10), "<br>")}</th>')
                page_html.append('          </tr></thead>')
                page_html.append('          <tbody>')
                for r_idx, r in enumerate(tab_rows[1:]):
                    bg = 'bg-gray-50/60' if r_idx % 2 == 1 else 'bg-white'
                    page_html.append(f'            <tr class="{bg} border-b border-gray-200 hover:bg-yellow-50/30 transition-colors">')
                    for idx_c, c in enumerate(r):
                        align = 'text-right font-medium' if idx_c > 0 else 'text-left'
                        page_html.append(f'              <td class="border border-black p-2 {align} text-gray-800">{html.escape(c).replace(chr(10), "<br>")}</td>')
                    page_html.append('            </tr>')
                page_html.append('          </tbody>')
                page_html.append('        </table>')
                page_html.append('      </div>')
            page_html.append('    </div>')

            # Chart column (5 cols on lg)
            page_html.append('    <div class="lg:col-span-5 flex flex-col items-center justify-center p-2 bg-gray-50/40 rounded-xs border border-gray-100">')
            if img_path:
                page_html.append(f'      <img src="{img_path}" alt="{html.escape(fig_cap)}" class="w-auto h-auto max-h-[190px] max-w-full object-contain" loading="lazy" />')
            if fig_cap:
                page_html.append(f'      <figcaption class="text-center font-mono text-xs font-semibold text-gray-600 mt-2">{html.escape(fig_cap)}</figcaption>')
            page_html.append('    </div>')

            page_html.append('  </div>')
            page_html.append('</div>\n')

            all_content_html.append('\n'.join(page_html))
            continue

        # --- Chapter 3 Custom Renderer (PDF Pages 46 to 54) ---
        if 46 <= pdf_page <= 54:
            ch3_html = get_ch3_page_html(pdf_page)
            if ch3_html:
                page_html.append(ch3_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- Chapter 8 Custom Renderer (PDF Pages 126 to 138) ---
        if 126 <= pdf_page <= 138:
            ch8_html = get_ch8_page_html(pdf_page)
            if ch8_html:
                page_html.append(ch8_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- Chapter 9 & Conclusion Custom Renderer (PDF Pages 139 to 142) ---
        if 139 <= pdf_page <= 142:
            ch9_html = get_ch9_page_html(pdf_page)
            if ch9_html:
                page_html.append(ch9_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- Appendix A Custom Renderer (PDF Pages 143 to 146) ---
        if 143 <= pdf_page <= 146:
            app_a_html = get_appendix_a_html(pdf_page)
            if app_a_html:
                page_html.append(app_a_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- Appendix B Custom Renderer (PDF Page 147) ---
        if pdf_page == 147:
            app_b_html = get_appendix_b_html()
            if app_b_html:
                page_html.append(app_b_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- References Custom Renderer (PDF Pages 148 to 151) ---
        if 148 <= pdf_page <= 151:
            ref_html = get_references_html(pdf_page)
            if ref_html:
                page_html.append(ref_html)
                all_content_html.append('\n'.join(page_html))
                continue

        # --- General Content Pages (3-7, 21-26, 44-45, 55-142) ---
        tables = page.find_tables()
        tab_list = tables.tables
        tab_rects = [fitz.Rect(t.bbox) for t in tab_list]
        
        raw_blocks = page.get_text("blocks")
        sorted_blocks = sorted(raw_blocks, key=lambda b: (round(b[1], 1), round(b[0], 1)))
        
        items = []
        for b in sorted_blocks:
            if b[6] == 0: # text block
                bbox = fitz.Rect(b[:4])
                in_tab = False
                for tr in tab_rects:
                    if bbox in tr or tr.intersects(bbox):
                        in_tab = True
                        break
                if not in_tab:
                    items.append(('text', b[1], b[4]))
                    
        for tab in tab_list:
            items.append(('table', tab.bbox[1], tab))
            
        items.sort(key=lambda x: x[1])
        
        skip_item_indices = set()
        tab_counter = 0
        for item_idx, (item_type, y_pos, item_data) in enumerate(items):
            if item_idx in skip_item_indices:
                continue
            if item_type == 'table':
                tab = item_data
                tab_data = tab.extract()
                t_idx = tab_counter
                tab_counter += 1

                # Custom specialized renderer for Chapter 6 & Chapter 7 tables
                if 96 <= pdf_page <= 125:
                    custom_html = get_ch6_7_table_html(pdf_page, t_idx, tab_data, doc)
                    if custom_html:
                        page_html.append(custom_html)
                    continue

                if not tab_data:
                    continue
                cleaned_rows = []
                for row in tab_data:
                    cleaned_row = [clean_str(cell.strip()) if cell else "" for cell in row]
                    if any(cleaned_row):
                        cleaned_rows.append(cleaned_row)
                if not cleaned_rows:
                    continue
                    
                table_html = ['<div class="overflow-x-auto relative max-w-full my-6 border border-black shadow-xs">']
                table_html.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white">')
                
                header_row = cleaned_rows[0]
                table_html.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
                for col in header_row:
                    col_esc = format_table_cell(col)
                    table_html.append(f'      <th class="border border-black p-2.5 font-bold uppercase">{col_esc}</th>')
                table_html.append('    </tr></thead>')
                
                table_html.append('    <tbody>')
                for r_idx, row in enumerate(cleaned_rows[1:]):
                    bg_cls = 'bg-gray-50/70' if r_idx % 2 == 1 else 'bg-white'
                    table_html.append(f'      <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
                    for cell in row:
                        cell_esc = format_table_cell(cell)
                        table_html.append(f'        <td class="border border-black p-2 align-top text-gray-800">{cell_esc}</td>')
                    table_html.append('      </tr>')
                table_html.append('    </tbody>')
                table_html.append('  </table>')
                table_html.append('</div>\n')
                page_html.append('\n'.join(table_html))

            elif item_type == 'text':
                raw_text = clean_str(item_data.strip())
                if not raw_text:
                    continue
                
                # Filter out isolated page numbers
                if raw_text == rep_page or raw_text == str(pdf_page):
                    continue
                if re.match(r'^(i{1,3}|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|\d+)$', raw_text, re.I):
                    continue
                    
                lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
                
                # We process block lines
                idx = 0
                while idx < len(lines):
                    line = lines[idx]
                    line_clean = ' '.join(line.split())
                    
                    # 1. Chapter Title (Page >= 21)
                    ch_match = re.match(r'^(Chapter\s+(\d+|[A-Za-z0-9]+))[:\s]*(.*)$', line_clean, re.I)
                    if ch_match and pdf_page >= 21:
                        ch_num = ch_match.group(1)
                        ch_title = ch_match.group(3).strip()
                        ch_num_val = ch_match.group(2).lower()
                        # If title is on next line in this block
                        if not ch_title and idx + 1 < len(lines):
                            idx += 1
                            ch_title = lines[idx].strip()
                        # If still empty, check next item in items!
                        if not ch_title and item_idx + 1 < len(items) and items[item_idx + 1][0] == 'text':
                            next_raw = clean_str(items[item_idx + 1][2].strip())
                            next_first_line = next_raw.split('\n')[0].strip()
                            if not re.match(r'^\d+\.\d+', next_first_line) and not next_first_line.startswith('Table') and not next_first_line.startswith('Figure'):
                                ch_title = next_first_line
                                skip_item_indices.add(item_idx + 1)
                        ch_id = f"ch-{ch_num_val}"
                        page_html.append(f'<div class="mt-14 mb-8 pt-6 border-t-2 border-black" id="{ch_id}">')
                        page_html.append(f'  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2.5 py-1 inline-block mb-3">{html.escape(ch_num)}</span>')
                        page_html.append(f'  <h2 class="text-2xl md:text-4xl font-bold font-mono tracking-tight text-black">{html.escape(ch_title)}</h2>')
                        page_html.append('</div>\n')
                        idx += 1
                        continue

                    # 2. Major sections (COPYRIGHT NOTICE, FORWARDING LETTER, PREFACE, ABSTRACT, ACKNOWLEDGEMENT, APPENDIX, REFERENCE, Conclusion)
                    if re.match(r'^(COPYRIGHT NOTICE|FORWARDING LETTER|PREFACE|ABSTRACT|ACKNOWLEDGEMENT|APPENDIX|REFERENCE|Conclusion)$', line_clean, re.I):
                        sec_id = re.sub(r'[^a-zA-Z0-9]+', '-', line_clean.lower()).strip('-')
                        page_html.append(f'<h2 class="text-2xl md:text-3xl font-bold font-mono tracking-tight mt-12 mb-6 pb-2 border-b-2 border-black" id="{sec_id}">{html.escape(line_clean)}</h2>\n')
                        idx += 1
                        continue

                    # 3. Subheadings (1.1, 2.3, 5.3.1, 5.3.2.1) on Page >= 21
                    sec_match = re.match(r'^(\d+\.\d+(\.\d+)*)\s*(.*)$', line_clean)
                    if sec_match and pdf_page >= 21:
                        sec_num = sec_match.group(1)
                        sec_title = sec_match.group(3).strip()
                        if not sec_title and idx + 1 < len(lines):
                            idx += 1
                            sec_title = lines[idx]
                        depth = len(sec_num.split('.'))
                        sec_id = f"sec-{sec_num.replace('.', '-')}"
                        if depth == 2:
                            page_html.append(f'<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="{sec_id}"><span class="text-gray-400 mr-2">{html.escape(sec_num)}</span>{html.escape(sec_title)}</h3>\n')
                        elif depth == 3:
                            page_html.append(f'<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="{sec_id}"><span class="text-gray-400 mr-2">{html.escape(sec_num)}</span>{html.escape(sec_title)}</h4>\n')
                        else:
                            page_html.append(f'<h5 class="text-base font-bold font-mono mt-6 mb-2" id="{sec_id}"><span class="text-gray-400 mr-2">{html.escape(sec_num)}</span>{html.escape(sec_title)}</h5>\n')
                        idx += 1
                        continue

                    # 4. Figure Caption (Page >= 21)
                    fig_match = re.match(r'^(Figure\s+\d+\s*\.\s*\d+\s*:[^\n]+)', line_clean)
                    if fig_match and pdf_page >= 21:
                        fig_title = fig_match.group(1)
                        clean_fig_title = ' '.join(fig_title.split())
                        img_path = fig_to_img.get(clean_fig_title)
                        
                        fig_html = ['<figure class="my-8 max-w-2xl mx-auto border border-gray-300 p-4 bg-white shadow-2xs hover:border-black transition-colors rounded-xs">']
                        if img_path:
                            fig_html.append(f'  <div class="flex justify-center p-2 bg-white">')
                            fig_html.append(f'    <img src="{img_path}" alt="{html.escape(clean_fig_title)}" class="max-h-[320px] w-auto object-contain" loading="lazy" />')
                            fig_html.append(f'  </div>')
                        fig_html.append(f'  <figcaption class="text-center font-mono text-xs text-gray-700 font-bold border-t border-gray-200 pt-3 mt-2">{html.escape(clean_fig_title)}</figcaption>')
                        fig_html.append('</figure>\n')
                        page_html.append('\n'.join(fig_html))
                        idx += 1
                        continue

                    # 5. Table Caption
                    tab_match = re.match(r'^(Table\s+\d+\s*\.\s*\d+[\s:]+[^\n]+)', line_clean)
                    if tab_match and pdf_page >= 21 and not line_clean.startswith('Table of Contents'):
                        tab_title = tab_match.group(1)
                        clean_tab_title = ' '.join(tab_title.split())
                        page_html.append(f'<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>{html.escape(clean_tab_title)}</div>\n')
                        idx += 1
                        continue

                    # 6. Bullets
                    bullet_match = re.match(r'^[•❖\*\-]\s*(.*)$', line_clean)
                    if bullet_match:
                        b_text = bullet_match.group(1)
                        b_esc = html.escape(b_text)
                        page_html.append(f'<li class="relative pl-6 mb-2 list-none font-sans text-gray-800 leading-relaxed"><span class="absolute left-0 text-black font-mono font-bold">→</span>{b_esc}</li>\n')
                        idx += 1
                        continue

                    # 7. Questionnaire Radio Options
                    radio_match = re.match(r'^o\s+(.*)$', line_clean)
                    if radio_match:
                        r_text = radio_match.group(1)
                        page_html.append(f'<div class="flex items-center gap-3 font-mono text-sm my-1.5 pl-4 text-gray-700"><span class="w-3.5 h-3.5 rounded-full border border-black inline-block shrink-0 bg-white"></span><span>{html.escape(r_text)}</span></div>\n')
                        idx += 1
                        continue

                    # 8. Regular text or equations
                    # Collect all following regular lines in this block to form a coherent paragraph
                    para_lines = [line]
                    idx += 1
                    while idx < len(lines):
                        next_line = lines[idx]
                        next_clean = ' '.join(next_line.split())
                        # Check if next_line starts a heading, table caption, figure caption, bullet, or radio
                        is_special = (
                            re.match(r'^(Chapter\s+(\d+|[A-Za-z0-9]+))', next_clean, re.I) or
                            re.match(r'^(COPYRIGHT NOTICE|FORWARDING LETTER|PREFACE|ABSTRACT|ACKNOWLEDGEMENT|APPENDIX|REFERENCE|Conclusion)$', next_clean, re.I) or
                            re.match(r'^(\d+\.\d+(\.\d+)*)\s+', next_clean) or
                            re.match(r'^(Figure\s+\d+\s*\.\s*\d+\s*:)', next_clean) or
                            re.match(r'^(Table\s+\d+\s*\.\s*\d+[\s:]+)', next_clean) or
                            re.match(r'^[•❖\*\-]\s+', next_clean) or
                            re.match(r'^o\s+', next_clean)
                        )
                        if is_special:
                            break
                        para_lines.append(next_line)
                        idx += 1
                        
                    full_para = ' '.join(para_lines)
                    rendered_p = format_paragraph_with_math(full_para)
                    page_html.append(rendered_p + '\n')

        all_content_html.append('\n'.join(page_html))

    print(f"Generated clean HTML content for {len(all_content_html)} pages.")

    author_banner_lines = []
    for a in AUTHORS_DATA:
        badge = get_author_in_badge(a["linkedin"], a["name"])
        name_cls = 'font-bold text-black' if a["is_primary"] else ''
        name_span = f'<span class="{name_cls}">{a["name"]}</span>' if name_cls else f'<span>{a["name"]}</span>'
        author_banner_lines.append(f'<div class="flex items-center flex-wrap">{name_span} {badge}</div>')
    authors_banner_block = '\n            '.join(author_banner_lines)

    json_ld_authors = []
    for a in AUTHORS_DATA:
        extra_dept = ',\n          "department": "Department of Industrial and Production Engineering"' if a["is_primary"] else ''
        json_ld_authors.append(f'''      {{{{
        "@type": "Person",
        "name": "{a['name']}",
        "sameAs": "{a['linkedin']}",
        "affiliation": {{{{
          "@type": "EducationalOrganization",
          "name": "Bangladesh University of Engineering and Technology"{extra_dept}
        }}}}
      }}}}''')
    json_ld_authors_block = ',\n'.join(json_ld_authors)

    # 3. Assemble Full HTML Document
    full_html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- SEO Primary Meta Tags -->
  <title>Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Report | Md. Muqtadir Fuad</title>
  <meta name="title" content="Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Report | Md. Muqtadir Fuad" />
  <meta name="description" content="Comprehensive 151-page capstone engineering report on Semi-Automated Shoe Cleaning Machine (IPE 304, BUET): SolidWorks 3D CAD modeling, ANSYS FEA simulation, QFD House of Quality, weighted material selection, and cost &amp; sensitivity analysis." />
  <meta name="keywords" content="Semi-Automated Shoe Cleaning Machine, Product Design, IPE 304, BUET, Industrial and Production Engineering, SolidWorks CAD, ANSYS FEA Simulation, QFD House of Quality, Material Selection, Digital Logic Method, Performance Index, Break-Even Analysis, Sensitivity Analysis, Footwear Cleaning Appliance, Capstone Engineering Report" />
  <meta name="author" content="Md. Muqtadir Fuad, Abdullah Al Mazid, Md. Ashiqur Rahman Noor, Md Sadiqul Haque, Ananya Halder, Yashna Noor" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="theme-color" content="#000000" />
  <link rel="canonical" href="https://md-muqtadir-fuad.github.io/blog-semi-automated-shoe-cleaning-machine.html" />

  <!-- Open Graph / Facebook / LinkedIn -->
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://md-muqtadir-fuad.github.io/blog-semi-automated-shoe-cleaning-machine.html" />
  <meta property="og:title" content="Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Report" />
  <meta property="og:description" content="151-Page Capstone Engineering Design, FEA Structural Simulation, and Manufacturing Economics Analysis." />
  <meta property="og:image" content="https://md-muqtadir-fuad.github.io/assets/images/pd-report/page_001_img_1_30.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Semi-Automated Shoe Cleaning Machine 3D CAD Model &amp; Simulation" />
  <meta property="og:site_name" content="Md. Muqtadir Fuad" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:published_time" content="2024-12-15T00:00:00+06:00" />
  <meta property="article:modified_time" content="2024-12-15T00:00:00+06:00" />
  <meta property="article:author" content="Md. Muqtadir Fuad" />
  <meta property="article:section" content="Engineering &amp; Product Design" />
  <meta property="article:tag" content="Mechanical Engineering" />
  <meta property="article:tag" content="Product Design" />
  <meta property="article:tag" content="FEA Simulation" />
  <meta property="article:tag" content="SolidWorks" />
  <meta property="article:tag" content="Manufacturing Economics" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://md-muqtadir-fuad.github.io/blog-semi-automated-shoe-cleaning-machine.html" />
  <meta name="twitter:title" content="Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Report" />
  <meta name="twitter:description" content="Comprehensive 151-page capstone engineering report: 3D CAD modeling, ANSYS FEA simulation, QFD House of Quality, and sensitivity analysis." />
  <meta name="twitter:image" content="https://md-muqtadir-fuad.github.io/assets/images/pd-report/page_001_img_1_30.png" />
  <meta name="twitter:image:alt" content="Semi-Automated Shoe Cleaning Machine 3D CAD Model" />

  <!-- Scholarly & Dublin Core Metadata for Academic Indexing -->
  <meta name="citation_title" content="Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Design, Customer Needs QFD, SolidWorks 3D CAD Modeling, ANSYS FEA Structural Simulation, Material Selection, and Manufacturing Cost Analysis Report" />
  <meta name="citation_author" content="Fuad, Md. Muqtadir" />
  <meta name="citation_author" content="Al Mazid, Abdullah" />
  <meta name="citation_author" content="Noor, Md. Ashiqur Rahman" />
  <meta name="citation_author" content="Haque, Md Sadiqul" />
  <meta name="citation_author" content="Halder, Ananya" />
  <meta name="citation_author" content="Noor, Yashna" />
  <meta name="citation_publication_date" content="2024/12/15" />
  <meta name="citation_technical_report_number" content="BUET-IPE-304-B14-2024" />
  <meta name="citation_technical_report_institution" content="Department of Industrial and Production Engineering, Bangladesh University of Engineering and Technology" />
  <meta name="dc.title" content="Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Report" />
  <meta name="dc.creator" content="Md. Muqtadir Fuad; Abdullah Al Mazid; Md. Ashiqur Rahman Noor; Md Sadiqul Haque; Ananya Halder; Yashna Noor" />
  <meta name="dc.publisher" content="Department of Industrial and Production Engineering, BUET" />
  <meta name="dc.date" content="2024-12-15" />
  <meta name="dc.type" content="Technical Report" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Semi-Automated Shoe Cleaning Machine: Comprehensive Engineering Design & FEA Analysis Report",
    "description": "Comprehensive 151-page capstone engineering design and product development report on a semi-automated shoe cleaning machine: SolidWorks 3D CAD modeling, ANSYS FEA simulation, QFD House of Quality, weighted material selection, and cost & sensitivity analysis.",
    "image": "https://md-muqtadir-fuad.github.io/assets/images/pd-report/page_001_img_1_30.png",
    "datePublished": "2024-12-15T00:00:00+06:00",
    "dateModified": "2024-12-15T00:00:00+06:00",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://md-muqtadir-fuad.github.io/blog-semi-automated-shoe-cleaning-machine.html"
    }},
    "author": [
{json_ld_authors_block}
    ],
    "publisher": {{
      "@type": "Organization",
      "name": "Department of Industrial and Production Engineering, BUET",
      "url": "https://ipe.buet.ac.bd"
    }},
    "inLanguage": "en-US",
    "keywords": "Product Design, CAD, FEA Simulation, QFD, Material Selection, Cost Analysis, BUET, Shoe Cleaning Machine"
  }}
  </script>

  <!-- Favicon -->
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="manifest" href="/site.webmanifest">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- Site Stylesheet -->
  <link rel="stylesheet" href="/style.css">

  <!-- KaTeX for Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
    onload="renderMathInElement(document.body, {{
      delimiters: [
        {{left: '$$', right: '$$', display: true}},
        {{left: '\\\\[', right: '\\\\]', display: true}},
        {{left: '\\\\(', right: '\\\\)', display: false}},
        {{left: '$', right: '$', display: false}}
      ],
      throwOnError : false
    }});"></script>

  <style>
    .overflow-x-auto, .overflow-x-scroll {{
      position: relative !important;
      max-width: 100% !important;
      contain: paint !important;
    }}
    .katex-display {{
      overflow-x: auto !important;
      overflow-y: hidden !important;
      max-width: 100% !important;
    }}
    /* Table styling overrides */
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      padding: 0.5rem 0.75rem;
      border: 1px solid #000;
    }}
    .sidebar-toc a {{
      transition: all 0.15s ease-in-out;
    }}
    .sidebar-toc a:hover {{
      background-color: #000;
      color: #fff;
      padding-left: 0.5rem;
    }}
    #reading-progress {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background-color: #000;
      z-index: 9999;
      width: 0%;
      transition: width 0.1s ease-out;
    }}
  </style>
</head>
<body class="bg-white text-black min-h-screen flex flex-col selection:bg-black selection:text-white">

  <!-- Reading Progress Bar -->
  <div id="reading-progress"></div>

  <!-- Desktop Header -->
  <header class="fixed top-0 w-full bg-white border-b border-black z-50">
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
      <a href="/" class="font-bold text-lg font-mono tracking-tighter">MMF.</a>
      <nav class="hidden md:flex gap-8 font-mono text-sm uppercase">
        <a href="/" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Home</a>
        <a href="/experience.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Experience</a>
        <a href="/projects.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Projects</a>
        <a href="/publications.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Publications</a>
        <a href="/achievements.html" class="px-2 py-1 transition-colors hover:bg-black hover:text-white">Achievements</a>
        <a href="/blogs.html" class="px-2 py-1 bg-black text-white">Blogs</a>
      </nav>
      <button id="menu-btn" class="md:hidden font-mono text-sm border border-black px-3 py-1 uppercase hover:bg-black hover:text-white transition-colors">
        MENU
      </button>
    </div>
  </header>

  <!-- Mobile Nav -->
  <div id="mobile-nav" class="hidden fixed inset-0 top-16 bg-white z-40 border-b border-black p-6 flex flex-col gap-6 font-mono text-2xl uppercase">
    <a href="/" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Home</a>
    <a href="/experience.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Experience</a>
    <a href="/projects.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Projects</a>
    <a href="/publications.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Publications</a>
    <a href="/achievements.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Achievements</a>
    <a href="/blogs.html" class="block border-b border-black pb-2 hover:bg-black hover:text-white transition-colors">Blogs</a>
  </div>

  <!-- Main Container -->
  <main class="flex-grow max-w-7xl mx-auto px-4 md:px-6 pt-28 pb-24 w-full min-w-0">
    
    <!-- Breadcrumb & Back Link -->
    <div class="mb-6 font-mono text-xs flex items-center gap-2 text-gray-600">
      <a href="/blogs.html" class="hover:underline">← Back to All Blogs</a>
      <span>/</span>
      <span class="text-black font-semibold">Semi-Automated Shoe Cleaning Machine</span>
    </div>

    <!-- Article Header Banner -->
    <header class="mb-10 border-b border-black pb-8">
      <div class="flex flex-wrap gap-2 mb-4 font-mono text-xs">
        <span class="border border-black px-2 py-0.5 bg-black text-white font-bold">IPE 304</span>
        <span class="border border-black px-2 py-0.5">Capstone Report</span>
        <span class="border border-black px-2 py-0.5">151 Pages Verbatim</span>
        <span class="border border-black px-2 py-0.5">BUET</span>
        <span class="border border-black px-2 py-0.5">December 15, 2024</span>
      </div>
      <h1 class="text-3xl md:text-5xl font-bold tracking-tight mb-4 font-mono">
        Semi-Automated Shoe Cleaning Machine
      </h1>
      <p class="text-lg md:text-xl text-gray-700 leading-relaxed max-w-4xl font-sans">
        A Comprehensive Engineering Design, Customer QFD, SolidWorks 3D CAD Modeling, ANSYS FEA Structural Simulation, Weighted Decision Material Selection, and Manufacturing Cost Analysis Report.
      </p>
      
      <div class="mt-6 pt-6 border-t border-gray-200 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 font-mono text-xs">
        <div>
          <span class="text-gray-500 block uppercase font-bold mb-1.5">Authors (Group B14)</span>
          <div class="space-y-1">
            {authors_banner_block}
          </div>
        </div>
        <div>
          <span class="text-gray-500 block uppercase font-bold mb-1.5">Faculty Supervisors</span>
          <span class="font-semibold text-black">Dr. Shuva Ghosh</span> (Assoc. Prof.)<br>
          <span class="font-semibold text-black">Dr. A.B.M. Mainul Bari</span> (Assoc. Prof.)<br>
          <span class="text-gray-600">Nafisa Anzum Sristi &amp; Zahin Ar Rafi</span>
        </div>
        <div>
          <span class="text-gray-500 block uppercase font-bold mb-1.5">Institution</span>
          <span class="font-bold text-black">Bangladesh University of Engineering and Technology</span><br>
          <span class="text-gray-600">Dept. of Industrial &amp; Production Engineering</span>
        </div>
      </div>
    </header>

    <!-- Layout: Sticky Sidebar TOC + Content -->
    <div class="flex flex-col lg:flex-row gap-10 items-start min-w-0 max-w-full">
      
      <!-- Sticky Sidebar TOC -->
      <aside class="w-full lg:w-80 shrink-0 lg:sticky lg:top-24 max-h-[calc(100vh-8rem)] overflow-y-auto border border-black p-4 bg-gray-50 sidebar-toc font-mono text-xs">
        <div class="flex items-center justify-between pb-3 border-b border-black mb-3">
          <span class="font-bold uppercase tracking-wider">Table of Contents</span>
          <span class="text-[10px] bg-black text-white px-1.5 py-0.5">151 PAGES</span>
        </div>
        <nav class="space-y-1">
          <a href="#page-1" class="block py-1 border-b border-gray-200 font-semibold">Cover &amp; Faculty Details</a>
          <a href="#copyright-notice" class="block py-1 border-b border-gray-200">Copyright Notice</a>
          <a href="#forwarding-letter" class="block py-1 border-b border-gray-200">Forwarding Letter</a>
          <a href="#preface" class="block py-1 border-b border-gray-200">Preface</a>
          <a href="#abstract" class="block py-1 border-b border-gray-200 font-semibold">Abstract</a>
          <a href="#acknowledgement" class="block py-1 border-b border-gray-200">Acknowledgement</a>
          <a href="#page-8" class="block py-1 border-b border-gray-200 font-semibold">Document TOC Index</a>
          <a href="#page-14" class="block py-1 border-b border-gray-200">Document List of Tables</a>
          <a href="#page-18" class="block py-1 border-b border-gray-200">Document List of Illustrations</a>
          
          <div class="pt-2 pb-1 font-bold text-gray-500 uppercase tracking-widest text-[10px]">Body Chapters</div>
          <a href="#ch-01" class="block py-1 border-b border-gray-200 font-semibold">Ch 01: Introduction &amp; 4 Proposals</a>
          <a href="#ch-02" class="block py-1 border-b border-gray-200 font-semibold">Ch 02: Customer Needs Survey (17 Qs)</a>
          <a href="#ch-03" class="block py-1 border-b border-gray-200 font-semibold">Ch 03: Voice of Customer with QFD</a>
          <a href="#ch-04" class="block py-1 border-b border-gray-200 font-semibold">Ch 04: Functional Decomposition</a>
          <a href="#ch-05" class="block py-1 border-b border-gray-200 font-semibold">Ch 05: CAD &amp; ANSYS FEA Simulation</a>
          <a href="#sec-5-3-1" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 5.3.1 Base Analysis</a>
          <a href="#sec-5-3-2" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 5.3.2 Frame Analysis</a>
          <a href="#sec-5-3-3" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 5.3.3 Shaft Analysis</a>
          <a href="#sec-5-3-4" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 5.3.4 Worm-Gear Connector</a>
          <a href="#sec-5-3-5" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 5.3.5 Side-Brush Support</a>
          <a href="#ch-06" class="block py-1 border-b border-gray-200 font-semibold">Ch 06: Qualitative Material Selection</a>
          <a href="#ch-07" class="block py-1 border-b border-gray-200 font-semibold">Ch 07: Quantitative Weighted Analysis</a>
          <a href="#ch-08" class="block py-1 border-b border-gray-200 font-semibold">Ch 08: Cost &amp; Sensitivity Analysis</a>
          <a href="#sec-8-2" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 8.2 Forecasting Demand</a>
          <a href="#sec-8-3" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 8.3 Manufacturing Cost</a>
          <a href="#sec-8-4" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 8.4 Non-Manufacturing Cost</a>
          <a href="#sec-8-6" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 8.6 Break-Even Analysis</a>
          <a href="#sec-8-7" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 8.7 Sensitivity Analysis</a>
          <a href="#ch-09" class="block py-1 border-b border-gray-200 font-semibold">Ch 09: Future Scope &amp; Limitations</a>
          <a href="#sec-9-1" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 9.1 Introduction</a>
          <a href="#sec-9-2" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 9.2 Future Scope</a>
          <a href="#sec-9-3" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 9.3 Limitations</a>
          <a href="#sec-9-4" class="block py-1 pl-3 text-gray-600 border-b border-gray-100">↳ 9.4 Chapter Conclusion</a>
          <a href="#conclusion" class="block py-1 border-b border-gray-200 font-semibold">Overall Conclusion</a>
          
          <div class="pt-2 pb-1 font-bold text-gray-500 uppercase tracking-widest text-[10px]">Appendices &amp; References</div>
          <a href="#appendix" class="block py-1 border-b border-gray-200 font-semibold">Appendix A: Questionnaire</a>
          <a href="#page-147" class="block py-1 border-b border-gray-200">Appendix B: Material Constants</a>
          <a href="#reference" class="block py-1 border-b border-gray-200 font-semibold">References &amp; Purchase Links</a>
        </nav>
        
        <div class="mt-4 pt-3 border-t border-black">
          <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="w-full text-center border border-black py-1.5 uppercase hover:bg-black hover:text-white transition-colors font-bold">
            ↑ Top of Page
          </button>
        </div>
      </aside>

      <!-- Main Document Content -->
      <article class="flex-grow min-w-0 max-w-4xl w-full text-gray-800">
        {chr(10).join(all_content_html)}
      </article>

    </div>
  </main>

  <!-- Footer -->
  <footer class="border-t border-black bg-white mt-auto">
    <div class="max-w-7xl mx-auto px-6 py-8 flex flex-col md:flex-row justify-between items-center gap-4 font-mono text-sm">
      <p>&copy; 2026 Md. Muqtadir Fuad. All rights reserved.</p>
      <div class="flex gap-6">
        <a href="https://github.com/md-muqtadir-fuad">GitHub</a>
        <a href="https://linkedin.com/in/md-muqtadir-fuad">LinkedIn</a>
        <a href="/blogs.html">All Blogs</a>
      </div>
    </div>
  </footer>

  <script src="/main.js" type="module"></script>
  <script>
    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('reading-progress').style.width = scrolled + '%';
    }});
  </script>
</body>
</html>
"""

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print(f"Successfully wrote {len(full_html)} bytes to {output_html_path}")

if __name__ == '__main__':
    build_clean_html()
