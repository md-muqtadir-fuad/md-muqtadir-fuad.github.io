import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check Chapter 3 Heading
assert 'id="ch-03"' in html, "Chapter 3 id missing!"
assert 'Incorporating the Voice of Customer in Product Design with Quality Function Deployment (QFD)' in html

# 2. Check Sections
assert 'id="sec-3-1"' in html, "Section 3.1 id missing!"
assert 'id="sec-3-2"' in html, "Section 3.2 id missing!"
assert 'id="sec-3-3"' in html, "Section 3.3 id missing!"
assert 'id="sec-3-4"' in html, "Section 3.4 id missing!"

# 3. Check Table 3.1
assert 'Table 3. 1: Relationship Explanation' in html
reqs = [
    "Easy to Operate",
    "Portability",
    "Automation",
    "Eco-Friendly",
    "Operating Speed",
    "Effectiveness",
    "Low Cost",
    "Good Stability"
]
for req in reqs:
    assert f'>{req}</td>' in html, f"Requirement '{req}' missing from Table 3.1!"

# Check relationship badges
assert html.count('>Strong<') >= 15
assert html.count('>Moderate<') >= 14
assert html.count('>Weak<') >= 2

# 4. Check that broken fake headers on pages 48-52 are GONE
assert '<th class="border border-black p-2.5 font-bold uppercase">Automation</th>' not in html
assert '<th class="border border-black p-2.5 font-bold uppercase">Cleaning Design</th>' not in html
assert '<th class="border border-black p-2.5 font-bold uppercase">Effectiveness</th>' not in html
assert '<th class="border border-black p-2.5 font-bold uppercase">Good Stability</th>' not in html
assert 'enhance shine and<br>repel dirt</th>' not in html

# 5. Check House of Quality Figure 3.1
assert 'Figure 3. 1: House of Quality' in html
assert 'page_053_img_1_516.png' in html
assert 'View Full-Resolution House of Quality Matrix' in html

# 6. Check QFD Legends
assert 'QFD Matrix Relationships' in html
assert 'Roof Technical Correlations' in html
assert 'Strongly Positive' in html
assert 'Strongly Negative' in html

# 7. Check Section 3.4 Conclusion
assert 'QFD gives a deeper understanding of the problem.' in html
assert 'time utilized at the front end in gathering information saves time further down the process.' in html

print("ALL CHAPTER 3 VERIFICATIONS PASSED 100%!")
