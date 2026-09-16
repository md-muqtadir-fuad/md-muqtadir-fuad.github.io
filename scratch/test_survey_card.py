import fitz
import re
import html

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

def render_survey_card(pno):
    page = doc[pno]
    txt = page.get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    
    # 1. Prompt
    prompt = None
    for l in lines:
        if re.match(r'^\d+\.\s+', l):
            prompt = l
            break
            
    # 2. Options
    options = []
    for l in lines:
        if l.startswith('o ') or l == 'o':
            opt = l[2:].strip() if l.startswith('o ') else l
            if opt:
                options.append(opt)
                
    # 3. Table caption & Figure caption
    tab_cap = ""
    fig_cap = ""
    for l in lines:
        if l.startswith('Table 2.'):
            tab_cap = ' '.join(l.split())
        elif l.startswith('Figure 2.'):
            fig_cap = ' '.join(l.split())
            
    # 4. Table data
    tabs = page.find_tables().tables
    tab_rows = []
    if tabs:
        raw_rows = tabs[0].extract()
        for r in raw_rows:
            r_clean = [c.strip() if c else "" for c in r if c is not None]
            # Ignore row if it contains chart legend or empty
            if any(r_clean) and not any('Daily Weekly' in c or 'Time consuming\nIneffective' in c for c in r_clean):
                tab_rows.append(r_clean)
                
    # 5. Image path
    imgs = page.get_images()
    img_path = f"/assets/images/pd-report/page_{pno+1:03d}_img_1_{imgs[0][0]}.png" if imgs else ""
    
    # Build HTML
    card = []
    card.append(f'<div class="survey-card my-8 border border-black p-5 bg-white shadow-xs">')
    if prompt:
        card.append(f'  <h4 class="text-base md:text-lg font-bold font-mono text-black mb-3">{html.escape(prompt)}</h4>')
        
    if options:
        card.append('  <div class="flex flex-wrap gap-2 mb-5 font-mono text-xs text-gray-700">')
        for opt in options:
            card.append(f'    <div class="flex items-center gap-2 border border-gray-300 px-2.5 py-1 bg-gray-50"><span class="w-2.5 h-2.5 rounded-full border border-black inline-block bg-white shrink-0"></span><span>{html.escape(opt)}</span></div>')
        card.append('  </div>')
        
    card.append('  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">')
    
    # Table column
    card.append('    <div>')
    if tab_cap:
        card.append(f'      <div class="font-mono text-xs uppercase font-bold text-black mb-2 flex items-center gap-1.5"><span class="w-2 h-2 bg-black inline-block"></span>{html.escape(tab_cap)}</div>')
    if tab_rows:
        card.append('      <div class="overflow-x-auto border border-black">')
        card.append('        <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white">')
        header = tab_rows[0]
        card.append('          <thead><tr class="bg-gray-100 text-black border-b border-black">')
        for idx, col in enumerate(header):
            align = 'text-right' if idx > 0 else 'text-left'
            card.append(f'            <th class="border border-black p-2 font-bold uppercase {align}">{html.escape(col).replace(chr(10), "<br>")}</th>')
        card.append('          </tr></thead>')
        card.append('          <tbody>')
        for r_idx, r in enumerate(tab_rows[1:]):
            bg = 'bg-gray-50/60' if r_idx % 2 == 1 else 'bg-white'
            card.append(f'            <tr class="{bg} border-b border-gray-200 hover:bg-yellow-50/30 transition-colors">')
            for idx, c in enumerate(r):
                align = 'text-right font-medium' if idx > 0 else 'text-left'
                card.append(f'              <td class="border border-black p-2 {align} text-gray-800">{html.escape(c).replace(chr(10), "<br>")}</td>')
            card.append('            </tr>')
        card.append('          </tbody>')
        card.append('        </table>')
        card.append('      </div>')
    card.append('    </div>')
    
    # Chart column
    card.append('    <div class="flex flex-col items-center">')
    if img_path:
        card.append(f'      <div class="p-2 border border-gray-200 bg-white flex justify-center max-w-xs w-full shadow-2xs">')
        card.append(f'        <img src="{img_path}" alt="{html.escape(fig_cap)}" class="w-full h-auto max-h-[220px] object-contain" loading="lazy" />')
        card.append('      </div>')
    if fig_cap:
        card.append(f'      <figcaption class="text-center font-mono text-xs font-bold text-gray-700 mt-2">{html.escape(fig_cap)}</figcaption>')
    card.append('    </div>')
    
    card.append('  </div>')
    card.append('</div>')
    return '\n'.join(card)

print("Generated sample card for Q1 (Page 27):")
print(render_survey_card(26)[:500])
