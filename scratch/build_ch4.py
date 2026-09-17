# -*- coding: utf-8 -*-


FIGURES = [
    (
        "4.1",
        "Black Box Model of the Semi-Automated Shoe Cleaning Machine",
        "/assets/images/pd-report/page_056_img_1_523.png",
        "The black box model summarizes the machine's energy input and its dust and kinetic-energy outputs.",
    ),
    (
        "4.2",
        "Component Hierarchy of the Semi-Automated Shoe Cleaning Machine",
        "/assets/images/pd-report/page_057_img_1_526.png",
        "The hierarchy groups the machine into brush-cleaning, shining, and shoe-sole-cleaning subassemblies.",
    ),
    (
        "4.3",
        "Energy Flow for the Brush-Cleaning Assembly",
        "/assets/images/pd-report/page_058_img_1_529.png",
        "Electrical energy drives the upper motor and produces the linear and rotary motion used by the brush fibers.",
    ),
    (
        "4.4",
        "Energy and Material Flow for the Shining Assembly",
        "/assets/images/pd-report/page_058_img_2_530.png",
        "Mechanical and electrical inputs coordinate the mold sponge, vibrating plate, and shiner dispenser.",
    ),
    (
        "4.5",
        "Energy Flow for the Shoe-Sole-Cleaning Assembly",
        "/assets/images/pd-report/page_059_img_1_533.png",
        "Electrical energy is converted into the roller-brush motion used to clean the shoe sole.",
    ),
]


def _figure_html(number, title, image, summary):
    return f'''<figure class="my-8 mx-auto max-w-5xl border-2 border-black bg-white p-3 shadow-sm sm:p-5">
  <div class="overflow-x-auto bg-gray-50 p-2 sm:p-4">
    <img src="{image}" alt="Figure {number}: {title}" class="mx-auto h-auto min-w-[560px] max-w-full object-contain" loading="lazy" />
  </div>
  <figcaption class="mt-3 border-t border-black pt-3">
    <span class="block font-mono text-xs font-bold text-black">Figure {number}: {title}</span>
    <span class="mt-1 block text-sm leading-relaxed text-gray-600">{summary}</span>
    <a href="{image}" target="_blank" rel="noopener" class="mt-2 inline-block font-mono text-[11px] font-bold uppercase tracking-wide text-gray-600 underline decoration-gray-300 underline-offset-4 hover:text-black">Open full-resolution diagram</a>
  </figcaption>
</figure>'''


def get_ch4_html():
    steps = [
        (
            "01",
            "Identify the primary function",
            "Distill the design's core purpose into a simple statement. Represent the system as a black box whose boundary is defined by energy, material, and information inputs and outputs.",
        ),
        (
            "02",
            "Develop sub-functions",
            "Break the primary function into the specific sub-functions needed to support the system's purpose, ensuring that each component contributes to the main goal.",
        ),
        (
            "03",
            "Organize sub-functions",
            "Arrange the sub-functions in a logical sequence so that the process flow remains clear, especially when several elements interact.",
        ),
        (
            "04",
            "Refine sub-functions",
            "Examine each sub-function for further decomposition so every aspect of the function is addressed and the overall system remains coherent.",
        ),
    ]

    out = []
    out.append('<div class="mt-14 mb-8 border-t-2 border-black pt-6" id="ch-04">')
    out.append('  <span class="mb-3 inline-block bg-black px-2.5 py-1 font-mono text-xs uppercase tracking-widest text-white">Chapter 04</span>')
    out.append('  <h2 class="font-mono text-2xl font-bold tracking-tight text-black md:text-4xl">Functional Decomposition</h2>')
    out.append('  <p class="mt-3 max-w-3xl text-base leading-relaxed text-gray-600">From a single system boundary to three coordinated machine assemblies.</p>')
    out.append('</div>')

    out.append('<h3 class="mt-10 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-4-1"><span class="mr-2 text-gray-400">4.1</span>Introduction</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">Functional decomposition is an analytical approach that breaks a complex system into manageable component functions and processes. It provides a top-down view of increasingly detailed functionality, helping designers understand how each part contributes to the product\'s overall purpose.</p>')
    out.append('<div class="my-7 grid grid-cols-1 gap-4 md:grid-cols-2">')
    for number, title, description in steps:
        out.append('  <section class="border border-gray-300 bg-white p-5">')
        out.append('    <div class="flex items-start gap-4">')
        out.append(f'      <span class="inline-flex h-9 w-9 shrink-0 items-center justify-center bg-black font-mono text-xs font-bold text-white">{number}</span>')
        out.append('      <div>')
        out.append(f'        <h4 class="font-mono text-sm font-bold uppercase tracking-wide text-black">{title}</h4>')
        out.append(f'        <p class="mt-2 text-sm leading-relaxed text-gray-700">{description}</p>')
        out.append('      </div>')
        out.append('    </div>')
        out.append('  </section>')
    out.append('</div>')

    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-4-2"><span class="mr-2 text-gray-400">4.2</span>Black Box Model</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">A black box model represents a system through its energy, material, and information inputs and outputs without exposing internal details. It gives a high-level account of what the machine does before the design is decomposed into individual mechanisms.</p>')
    out.append(_figure_html(*FIGURES[0]))

    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-4-3"><span class="mr-2 text-gray-400">4.3</span>Component Hierarchy</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">A component hierarchy separates the product into major subassemblies and then lists the components within each one. When the functions of the subassemblies are satisfied, the primary system function is satisfied. Repeating this process creates a function tree that is quick to understand, although it does not fully describe interactions among subassemblies.</p>')
    out.append(_figure_html(*FIGURES[1]))

    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-4-4"><span class="mr-2 text-gray-400">4.4</span>Cluster Function Structure</h3>')
    out.append('<p class="text-base leading-relaxed text-gray-800">The cluster function structure expands the hierarchy into functional flows. The diagrams below trace how energy and material pass through the brush-cleaning, shining, and shoe-sole-cleaning assemblies.</p>')
    out.append('<div class="mt-6 border-l-4 border-black bg-gray-100 px-4 py-3 font-mono text-xs leading-relaxed text-gray-700"><strong class="text-black">Flow legend:</strong> thin arrows show energy; bold arrows show material.</div>')
    for figure in FIGURES[2:]:
        out.append(_figure_html(*figure))

    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-4-5"><span class="mr-2 text-gray-400">4.5</span>Conclusion</h3>')
    out.append('<div class="border-2 border-black bg-gray-50 p-5 md:p-6">')
    out.append('  <p class="text-base leading-relaxed text-gray-800">Together, the black box model, component hierarchy, and cluster function structure provide a complete functional view of the semi-automated shoe cleaning machine. The black box defines the system boundary, the hierarchy identifies each part\'s role, and the cluster diagrams show how material and energy move through the assemblies.</p>')
    out.append('  <p class="mt-4 text-base leading-relaxed text-gray-800">This progression from system-level purpose to component-level flow supports a well-structured, efficient, functional, and user-friendly design.</p>')
    out.append('</div>')
    return '\n'.join(out)
