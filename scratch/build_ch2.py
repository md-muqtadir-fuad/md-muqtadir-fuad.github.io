# -*- coding: utf-8 -*-
import html


SURVEY_QUESTIONS = [
    {
        "question": "How often do you clean your shoes?",
        "caption": "Time period of cleaning shoes",
        "rows": [("Daily", 6, 18), ("Weekly", 13, 38), ("Monthly", 10, 29), ("Quarterly", 5, 15)],
        "image": "/assets/images/pd-report/page_027_img_1_419.png",
    },
    {
        "question": "How do you currently clean your shoes?",
        "caption": "Current cleaning methods",
        "rows": [("Hand wash", 16, 47), ("Wet wipes", 14, 41), ("Professional cleaning", 4, 12)],
        "image": "/assets/images/pd-report/page_028_img_1_423.png",
    },
    {
        "question": "How much do you spend on a single shoe cleaning?",
        "caption": "Cost of single shoe cleaning",
        "rows": [("Under 50/=", 27, 79), ("50-100/=", 5, 15), ("100-150/=", 1, 3), ("150-200/=", 1, 3), ("Over 200/=", 0, 0)],
        "image": "/assets/images/pd-report/page_029_img_1_427.png",
    },
    {
        "question": "What challenges do you face when cleaning your shoes?",
        "caption": "Challenges of cleaning shoes",
        "rows": [("Time-consuming", 21, 62), ("Ineffective", 9, 26), ("Unavailability", 4, 12)],
        "image": "/assets/images/pd-report/page_030_img_1_431.png",
    },
    {
        "question": "How satisfied are you with your current shoe cleaning method?",
        "caption": "Satisfaction with current cleaning method",
        "rows": [("Very satisfied", 1, 3), ("Satisfied", 5, 15), ("Neutral", 22, 64), ("Dissatisfied", 4, 12), ("Very dissatisfied", 2, 6)],
        "image": "/assets/images/pd-report/page_031_img_1_435.png",
    },
    {
        "question": "Would you be interested in a machine that cleans your shoes automatically?",
        "caption": "Interest in an automatic cleaning machine",
        "rows": [("Yes", 21, 62), ("No", 1, 3), ("Maybe", 12, 35)],
        "image": "/assets/images/pd-report/page_032_img_1_439.png",
    },
    {
        "question": "What features would be most important to you in a shoe cleaning machine?",
        "caption": "Important machine features",
        "rows": [("Speed of cleaning", 9, 27), ("Effectiveness", 10, 29), ("Ease of use", 9, 26), ("Eco-friendliness", 6, 18)],
        "image": "/assets/images/pd-report/page_033_img_1_443.png",
    },
    {
        "question": "Would you prefer a portable machine or one that stays in one place?",
        "caption": "Portability preference",
        "rows": [("Portable", 26, 76), ("Stationary", 4, 12), ("No preference", 4, 12)],
        "image": "/assets/images/pd-report/page_034_img_1_447.png",
    },
    {
        "question": "What factors influence your decision to purchase a new cleaning device?",
        "caption": "Factors influencing a purchase decision",
        "rows": [("Reviews", 22, 65), ("Brand reputation", 5, 15), ("Recommendations", 7, 20)],
        "image": "/assets/images/pd-report/page_035_img_1_451.png",
    },
    {
        "question": "Have you seen similar products on the market?",
        "caption": "Availability of similar products",
        "rows": [("Yes", 7, 21), ("No", 27, 79)],
        "image": "/assets/images/pd-report/page_036_img_1_459.png",
    },
    {
        "question": "What additional features would make a shoe cleaning machine more appealing to you?",
        "caption": "Additional features that increase product appeal",
        "rows": [("Automation", 11, 32), ("Disinfectant", 7, 21), ("Shiner", 0, 0), ("Easy to operate", 16, 47)],
        "image": "/assets/images/pd-report/page_037_img_1_463.png",
    },
    {
        "question": "In which workplace environment would the shoe cleaning machine be used most?",
        "caption": "Likely workplace environment",
        "rows": [("Office lobby", 14, 41), ("Staff changing rooms", 17, 50), ("Warehouse/factory", 1, 3), ("Hospital entryway", 2, 6)],
        "image": "/assets/images/pd-report/page_038_img_1_467.png",
    },
    {
        "question": "How often would you expect to perform maintenance on such a machine?",
        "caption": "Expected maintenance period",
        "rows": [("Weekly", 6, 18), ("Monthly", 8, 23), ("Quarterly", 12, 35), ("Yearly", 8, 24)],
        "image": "/assets/images/pd-report/page_039_img_1_471.png",
    },
    {
        "question": "How concerned are you about cross-contamination and hygiene in common areas where the machine might be placed?",
        "caption": "Concern about cross-contamination and hygiene",
        "rows": [("Very concerned", 18, 53), ("Somewhat concerned", 13, 38), ("Not concerned", 3, 9)],
        "image": "/assets/images/pd-report/page_040_img_1_475.png",
    },
    {
        "question": "How important are environmentally friendly features such as energy efficiency or low water consumption?",
        "caption": "Importance of environmentally friendly features",
        "rows": [("Extremely important", 13, 38), ("Important", 18, 53), ("Neutral", 3, 9), ("Not important", 0, 0)],
        "image": "/assets/images/pd-report/page_041_img_1_479.png",
    },
    {
        "question": "Would noise levels be a concern in an area with frequent foot traffic?",
        "caption": "Concern about noise level",
        "rows": [("Yes, it should be quiet", 23, 68), ("Noise is acceptable if it is efficient", 9, 26), ("No preference", 2, 6)],
        "image": "/assets/images/pd-report/page_042_img_1_483.png",
    },
    {
        "question": "How likely are you to recommend such a machine to other organizations if it meets your expectations?",
        "caption": "Likelihood of recommending the machine",
        "rows": [("Very likely", 16, 47), ("Likely", 16, 47), ("Neutral", 2, 6), ("Unlikely", 0, 0)],
        "image": "/assets/images/pd-report/page_043_img_1_487.png",
    },
]


SURVEY_LOCATIONS = [
    ("Bangladesh University of Engineering and Technology (BUET)", "Palashi, Dhaka-1000, Bangladesh"),
    ("Bright River Bangladesh Ltd.", "Al-Razi Complex, 3rd Floor, Purana Paltan, Dhaka-1000, Bangladesh"),
    ("Rural Development Project of Jamalpur", "Level 03, REDC Building, LGED Headquarters, Agargaon, Dhaka-1207, Bangladesh"),
    ("BRAC Bank PLC, Anik Tower", "220/B, Tejgaon-Gulshan Link Road, Tejgaon, Dhaka-1208, Bangladesh"),
    ("University of Dhaka", "Nilkhet Road, Dhaka-1000, Bangladesh"),
    ("Pridesys IT Ltd.", "R&D Center, Level 11, Software Technology Park, Vision 2021 Tower, Dhaka-1215, Bangladesh"),
]


REQUIREMENTS = [
    ("Easy to operate", 10),
    ("Portability", 8),
    ("Automation", 7),
    ("Eco-friendly", 8),
    ("Operating speed", 9),
    ("Effectiveness", 8),
    ("Low cost", 9),
    ("Good stability", 8),
]


def _leading_response(rows):
    highest = max(row[2] for row in rows)
    leaders = [row[0] for row in rows if row[2] == highest]
    return " / ".join(leaders), highest


def _render_question_card(number, question):
    title = html.escape(question["question"])
    caption = html.escape(question["caption"])
    leaders, highest = _leading_response(question["rows"])
    figure_caption = f"Figure 2. {number}: {question['caption']}"
    table_caption = f"Table 2. {number}: {question['caption']}"

    out = [f'<section class="survey-card my-7 border border-gray-300 bg-white shadow-2xs" id="survey-q-{number}">']
    out.append('  <div class="border-b border-black bg-gray-50 p-4 md:p-5">')
    out.append('    <div class="flex items-start gap-3">')
    out.append(f'      <span class="inline-flex h-8 min-w-8 shrink-0 items-center justify-center bg-black px-2 font-mono text-xs font-bold text-white">Q{number}</span>')
    out.append('      <div class="min-w-0 flex-1">')
    out.append(f'        <h4 class="text-base font-bold leading-snug text-black md:text-lg">{title}</h4>')
    out.append(f'        <p class="mt-2 font-mono text-[10px] uppercase tracking-wider text-gray-500">Leading response: <strong class="text-black">{html.escape(leaders)}</strong> - {highest}%</p>')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </div>')
    out.append('  <div class="p-4 md:p-5">')
    out.append('    <div class="mb-5 flex flex-wrap gap-2 font-mono text-[10px] text-gray-700">')
    out.append('      <span class="self-center font-bold uppercase tracking-wider text-gray-400">Response options</span>')
    for label, _, _ in question["rows"]:
        out.append(f'      <span class="border border-gray-300 bg-gray-50 px-2 py-1">{html.escape(label)}</span>')
    out.append('    </div>')
    out.append('    <div class="grid grid-cols-1 items-center gap-6 lg:grid-cols-12">')
    out.append('      <div class="min-w-0 lg:col-span-7">')
    out.append(f'        <div class="mb-2 flex items-center gap-2 font-mono text-xs font-bold uppercase text-gray-800"><span class="h-2 w-2 bg-black"></span>{table_caption}</div>')
    out.append('        <div class="max-w-full overflow-x-auto border border-black">')
    out.append('          <table class="w-full min-w-[430px] border-collapse bg-white font-mono text-xs text-left">')
    out.append(f'            <caption class="sr-only">{table_caption}</caption>')
    out.append('            <thead><tr class="border-b border-black bg-gray-100 text-black">')
    out.append('              <th class="border border-black p-2 font-bold uppercase">Option</th>')
    out.append('              <th class="border border-black p-2 text-right font-bold uppercase">Responses</th>')
    out.append('              <th class="border border-black p-2 text-right font-bold uppercase">Percent</th>')
    out.append('            </tr></thead>')
    out.append('            <tbody>')
    for row_index, (label, count, percent) in enumerate(question["rows"]):
        background = 'bg-gray-50/70' if row_index % 2 else 'bg-white'
        out.append(f'              <tr class="{background} border-b border-gray-200">')
        out.append(f'                <td class="border border-black p-2 text-gray-800">{html.escape(label)}</td>')
        out.append(f'                <td class="border border-black p-2 text-right font-medium text-gray-800">{count}</td>')
        out.append(f'                <td class="border border-black p-2 text-right font-medium text-gray-800">{percent}%</td>')
        out.append('              </tr>')
    out.append('            </tbody>')
    out.append('          </table>')
    out.append('        </div>')
    out.append('      </div>')
    out.append('      <figure class="flex min-w-0 flex-col items-center justify-center border border-gray-200 bg-gray-50/60 p-3 lg:col-span-5">')
    out.append(f'        <img src="{question["image"]}" alt="Pie chart for survey question {number}: {caption}" class="h-auto max-h-[230px] w-auto max-w-full object-contain" loading="lazy" />')
    out.append(f'        <figcaption class="mt-2 text-center font-mono text-[10px] font-semibold text-gray-600">{html.escape(figure_caption)}</figcaption>')
    out.append('      </figure>')
    out.append('    </div>')
    out.append('  </div>')
    out.append('</section>')
    return '\n'.join(out)


def _render_requirements_table():
    out = ['<div class="my-6 overflow-hidden border border-black bg-white">']
    out.append('  <div class="border-b border-black bg-gray-100 px-4 py-3 font-mono text-xs font-bold uppercase tracking-wider">Table 2. 18: Relative importance of customer requirements</div>')
    out.append('  <div class="overflow-x-auto">')
    out.append('    <table class="w-full min-w-[520px] border-collapse font-mono text-xs">')
    out.append('      <caption class="sr-only">Table 2. 18: Relative importance of customer requirements</caption>')
    out.append('      <thead><tr class="border-b border-black bg-gray-50">')
    out.append('        <th class="border-r border-black p-3 text-left font-bold uppercase">Customer requirement</th>')
    out.append('        <th class="w-24 border-r border-black p-3 text-center font-bold uppercase">Score / 10</th>')
    out.append('        <th class="w-2/5 p-3 text-left font-bold uppercase">Relative importance</th>')
    out.append('      </tr></thead>')
    out.append('      <tbody>')
    for index, (name, score) in enumerate(REQUIREMENTS):
        background = 'bg-gray-50/60' if index % 2 else 'bg-white'
        out.append(f'        <tr class="{background} border-b border-gray-200">')
        out.append(f'          <td class="border-r border-black p-3 font-semibold text-gray-900">{html.escape(name)}</td>')
        out.append(f'          <td class="border-r border-black p-3 text-center text-sm font-bold text-black">{score}</td>')
        out.append('          <td class="p-3">')
        out.append('            <div class="h-2.5 w-full bg-gray-200">')
        out.append(f'              <div class="h-2.5 bg-black" style="width: {score * 10}%"></div>')
        out.append('            </div>')
        out.append('          </td>')
        out.append('        </tr>')
    out.append('      </tbody>')
    out.append('    </table>')
    out.append('  </div>')
    out.append('</div>')
    return '\n'.join(out)


def get_ch2_html():
    out = []
    out.append('<div class="mt-14 mb-8 border-t-2 border-black pt-6" id="ch-02">')
    out.append('  <span class="mb-3 inline-block bg-black px-2.5 py-1 font-mono text-xs uppercase tracking-widest text-white">Chapter 02</span>')
    out.append('  <h2 class="font-mono text-2xl font-bold tracking-tight text-black md:text-4xl">Understanding Customer Needs Through Survey</h2>')
    out.append('</div>')
    out.append('<h3 class="mt-10 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-2-1"><span class="mr-2 text-gray-400">2.1</span>Introduction</h3>')
    out.append('<div class="border border-gray-300 bg-white p-5 md:p-6">')
    out.append('  <p class="text-base leading-relaxed text-gray-800">Clean shoes support a professional appearance, but manual cleaning can be inconvenient during a busy day and difficult to arrange at short notice. Rain, dust, and daily travel can soil footwear quickly, creating demand for a fast and accessible cleaning solution.</p>')
    out.append('  <p class="mt-4 text-base leading-relaxed text-gray-800">The survey explored cleaning habits, pain points, desired product features, workplace placement, maintenance expectations, hygiene, sustainability, noise, and willingness to recommend a semi-automated shoe-cleaning machine.</p>')
    out.append('  <div class="mt-5 flex flex-wrap gap-2 font-mono text-xs">')
    for audience in ('Corporate officers', 'Teachers, doctors, and busy professionals', 'Bank and transport-station personnel'):
        out.append(f'    <span class="border border-black bg-gray-50 px-3 py-2 font-semibold">{html.escape(audience)}</span>')
    out.append('  </div>')
    out.append('</div>')
    out.append('<h3 class="mt-10 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-2-2"><span class="mr-2 text-gray-400">2.2</span>Survey Locations</h3>')
    out.append('<div class="grid grid-cols-1 gap-3 md:grid-cols-2">')
    for number, (name, address) in enumerate(SURVEY_LOCATIONS, 1):
        out.append('  <article class="flex gap-3 border border-gray-300 bg-white p-4">')
        out.append(f'    <span class="inline-flex h-7 w-7 shrink-0 items-center justify-center bg-black font-mono text-[10px] font-bold text-white">{number:02d}</span>')
        out.append('    <div>')
        out.append(f'      <h4 class="text-sm font-bold text-black">{html.escape(name)}</h4>')
        out.append(f'      <address class="mt-1 text-xs not-italic leading-relaxed text-gray-600">{html.escape(address)}</address>')
        out.append('    </div>')
        out.append('  </article>')
    out.append('</div>')
    out.append('<h3 class="mt-12 mb-3 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-2-3"><span class="mr-2 text-gray-400">2.3</span>Survey Results</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">The survey collected responses from <strong>34 participants</strong>. Each question below includes the original response table and the corresponding chart from the report.</p>')
    out.append('<div class="my-6 grid grid-cols-2 gap-3 md:grid-cols-3">')
    snapshots = [
        ("34", "Participants"), ("62%", "Interested in automatic cleaning"), ("76%", "Prefer a portable machine"),
        ("79%", "Have not seen a similar product"), ("68%", "Want quiet operation"), ("94%", "Likely to recommend"),
    ]
    for value, label in snapshots:
        out.append('  <div class="border border-black bg-gray-50 p-4">')
        out.append(f'    <p class="font-mono text-2xl font-bold text-black">{value}</p>')
        out.append(f'    <p class="mt-1 text-xs leading-snug text-gray-600">{html.escape(label)}</p>')
        out.append('  </div>')
    out.append('</div>')

    group_labels = {
        1: ("A", "Current behavior and pain points"),
        6: ("B", "Product interest and purchase preferences"),
        12: ("C", "Workplace deployment and advocacy"),
    }
    for number, question in enumerate(SURVEY_QUESTIONS, 1):
        if number in group_labels:
            code, title = group_labels[number]
            out.append('<div class="mt-10 mb-4 flex items-center gap-3 border-b border-black pb-2">')
            out.append(f'  <span class="bg-black px-2 py-1 font-mono text-[10px] font-bold text-white">{code}</span>')
            out.append(f'  <p class="font-mono text-xs font-bold uppercase tracking-wider text-gray-700">{html.escape(title)}</p>')
            out.append('</div>')
        out.append(_render_question_card(number, question))

    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-2-4"><span class="mr-2 text-gray-400">2.4</span>Customer Requirement Evaluation</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">The survey findings were consolidated into eight customer requirements and evaluated on a ten-point importance scale.</p>')
    out.append(_render_requirements_table())
    out.append('<div class="border-l-4 border-black bg-gray-100 px-4 py-3 text-sm leading-relaxed text-gray-800"><strong>Priority signal:</strong> Easy operation received the maximum score of 10, followed by operating speed and low cost at 9. Portability, eco-friendliness, effectiveness, and stability each scored 8, while automation scored 7.</div>')
    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-2-5"><span class="mr-2 text-gray-400">2.5</span>Conclusion</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">The Google Forms survey produced a varied but consistent set of customer priorities. Respondents favored an easy-to-operate, portable, quiet, hygienic, and affordable machine with effective cleaning performance. These findings establish the customer requirements that guide the product design and the quality-function-deployment analysis in the following chapter.</p>')
    return '\n'.join(out)
