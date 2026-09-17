import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 0. Check cleaned Chapter 1 structure
chapter_1 = html_content.split('id="ch-01"', 1)[1].split('id="ch-02"', 1)[0]
for anchor in (
    'sec-1-1', 'sec-1-2', 'sec-1-2-1', 'sec-1-2-2',
    'sec-1-2-3', 'sec-1-2-4', 'sec-1-3', 'sec-1-3-1'
):
    assert f'id="{anchor}"' in chapter_1, f"Missing Chapter 1 anchor: {anchor}"
assert chapter_1.count('<section ') == 4, "Expected four Chapter 1 proposal cards"
assert chapter_1.count('<li ') == chapter_1.count('</li>') == 39, "Chapter 1 lists are incomplete"
assert 'â†’' not in chapter_1 and 'â€™' not in chapter_1, "Chapter 1 contains mojibake"
print("Chapter 1 structure and text cleanup verified!")

# Check consolidated Chapter 2 survey presentation
chapter_2 = html_content.split('id="ch-02"', 1)[1].split('id="ch-03"', 1)[0]
for anchor in ('sec-2-1', 'sec-2-2', 'sec-2-3', 'sec-2-4', 'sec-2-5'):
    assert f'id="{anchor}"' in chapter_2, f"Missing Chapter 2 anchor: {anchor}"
for question in range(1, 18):
    assert f'id="survey-q-{question}"' in chapter_2, f"Missing survey question card: {question}"
assert chapter_2.count('<table ') == 18, "Expected 17 survey tables and one requirements table"
assert chapter_2.count('<figure ') == 17, "Expected 17 semantic survey figures"
assert chapter_2.count('<figcaption ') == 17, "Expected 17 survey figure captions"
assert 'Table 2. 18: Relative importance of customer requirements' in chapter_2
assert 'â†’' not in chapter_2 and 'â€™' not in chapter_2, "Chapter 2 contains mojibake"
print("Chapter 2 survey structure, tables, and figures verified!")

# Check consolidated Chapter 4 functional-decomposition presentation
chapter_4 = html_content.split('id="ch-04"', 1)[1].split('id="ch-05"', 1)[0]
for anchor in ('sec-4-1', 'sec-4-2', 'sec-4-3', 'sec-4-4', 'sec-4-5'):
    assert f'id="{anchor}"' in chapter_4, f"Missing Chapter 4 anchor: {anchor}"
for figure in range(1, 6):
    assert f'Figure 4.{figure}:' in chapter_4, f"Missing Chapter 4 figure: {figure}"
assert chapter_4.count('<figure ') == 5, "Expected five Chapter 4 figures"
assert chapter_4.count('Open full-resolution diagram') == 5, "Expected a full-resolution link for every Chapter 4 diagram"
assert chapter_4.count('<section ') == 4, "Expected four functional-decomposition step cards"
assert 'PDF Pages 55-59 / 151' in html_content, "Missing consolidated Chapter 4 page marker"
assert 'Figure 4. 1:' not in chapter_4, "Chapter 4 still contains broken figure numbering"
assert 'Ã¢' not in chapter_4 and 'â€' not in chapter_4, "Chapter 4 contains mojibake"
print("Chapter 4 functional decomposition and diagrams verified!")

# 1. Check Chapter 6 tables
assert 'Qualitative Analysis of Material Selection for Different Sections' in html_content
assert 'Qualitative Analysis of Manufacturing Process Selection' in html_content
assert 'Qualitative Analysis of Parts Joining Method Selection' in html_content

# Check that Table 6.2 has Make/Outsource badges
assert '>Make<' in html_content
assert '>Outsource<' in html_content

# Check that Table 6.3 has Permanent/Temporary badges
assert '>Permanent<' in html_content
assert '>Temporary<' in html_content

# 2. Check Digital Logic tables
dl_headers = re.findall(r'Number of Positive Decisions,\s*\$N = \\frac\{n\(n-1\)\}\{2\}', html_content)
print(f"Found {len(dl_headers)} Digital Logic two-tier headers with KaTeX formula!")
assert len(dl_headers) == 10, f"Expected 10 DL headers, found {len(dl_headers)}"

# Check Table 7.4 has 45 decision columns
assert '>45</th>' in html_content
assert 'Relative Emphasis ($\\alpha$)' in html_content

# 3. Check Performance Index tables
pi_headers = re.findall(r'Weighting Factor \(\$\\alpha\$\)', html_content)
print(f"Found {len(pi_headers)} Performance Index two-tier headers with KaTeX formula!")
assert len(pi_headers) == 10, f"Expected 10 PI headers, found {len(pi_headers)}"

# Check Table 7.5 candidate materials
assert 'AISI 316 Stainless Steel' in html_content
assert 'AISI 347 Annealed Stainless Steel' in html_content
assert '1045 Carbon Steel' in html_content

# Check Scaled (beta) and Score (alphabeta)
assert r'Scaled ($\beta$)' in html_content
assert r'Score ($\alpha\beta$)' in html_content
assert r'Performance Index ($\gamma = \sum \alpha\beta$)' in html_content

# Check Table 7.12 has both parts merged
assert 'Abrasion Resistance' in html_content
assert 'Flexibility' in html_content
assert 'Water Resistance' in html_content
assert 'Durability' in html_content

# Check no bell \x07 or backspace \x08
assert '\x07' not in html_content
assert '\x08' not in html_content

print("ALL VERIFICATIONS PASSED IN GENERATED HTML!")
