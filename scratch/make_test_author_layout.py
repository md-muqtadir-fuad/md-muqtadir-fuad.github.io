html_content = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Author Layout Comparison</title>
</head>
<body style="background:#ffffff; padding: 30px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; color: #111;">
  
  <div style="max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
    
    <!-- Option 1: Right after Name -->
    <div style="border: 1px solid #e5e7eb; padding: 20px;">
      <h4 style="font-size: 11px; text-transform: uppercase; color: #6b7280; margin: 0 0 12px 0;">Layout 1: Logo right after Name</h4>
      <div style="font-size: 12px; line-height: 1.8;">
        <div>
          <span style="font-weight: bold; color: #000;">Md. Muqtadir Fuad</span>
          <a href="https://www.linkedin.com/in/md-muqtadir-fuad/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 4px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
          <span style="color: #6b7280; margin-left: 4px;">(2008079)</span>
        </div>
        <div>
          <span>Abdullah Al Mazid</span>
          <a href="https://www.linkedin.com/in/abdullahalmazid/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 4px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
          <span style="color: #6b7280; margin-left: 4px;">(2008080)</span>
        </div>
        <div>
          <span>Md. Ashiqur Rahman Noor</span>
          <a href="https://www.linkedin.com/in/ashiqur-rahman-noor/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 4px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
          <span style="color: #6b7280; margin-left: 4px;">(2008081)</span>
        </div>
      </div>
    </div>

    <!-- Option 2: After Student ID -->
    <div style="border: 1px solid #e5e7eb; padding: 20px;">
      <h4 style="font-size: 11px; text-transform: uppercase; color: #6b7280; margin: 0 0 12px 0;">Layout 2: Logo after Student ID</h4>
      <div style="font-size: 12px; line-height: 1.8;">
        <div>
          <span style="font-weight: bold; color: #000;">Md. Muqtadir Fuad</span>
          <span style="color: #6b7280; margin-left: 4px;">(2008079)</span>
          <a href="https://www.linkedin.com/in/md-muqtadir-fuad/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 6px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
        </div>
        <div>
          <span>Abdullah Al Mazid</span>
          <span style="color: #6b7280; margin-left: 4px;">(2008080)</span>
          <a href="https://www.linkedin.com/in/abdullahalmazid/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 6px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
        </div>
        <div>
          <span>Md. Ashiqur Rahman Noor</span>
          <span style="color: #6b7280; margin-left: 4px;">(2008081)</span>
          <a href="https://www.linkedin.com/in/ashiqur-rahman-noor/" style="display: inline-flex; align-items: center; vertical-align: middle; margin-left: 6px; text-decoration: none;">
            <svg style="width: 14px; height: 14px; border-radius: 2px;" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="4" fill="#0A66C2"/>
              <path d="M7 9.5h2.6v8H7v-8zm1.3-4.3c-.85 0-1.4.55-1.4 1.3 0 .7.55 1.3 1.35 1.3.85 0 1.4-.6 1.4-1.3 0-.75-.55-1.3-1.35-1.3zm4.5 4.3h2.5v1.15h.05c.35-.65 1.2-1.35 2.45-1.35 2.65 0 3.15 1.75 3.15 4v4.2h-2.6v-3.7c0-.9-.3-1.5-1.15-1.5-.65 0-1.05.45-1.2.9-.05.15-.05.4-.05.65v3.65h-2.6v-8z" fill="#ffffff"/>
            </svg>
          </a>
        </div>
      </div>
    </div>

  </div>
</body>
</html>
'''

with open('scratch/test_author_layout.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print('Generated scratch/test_author_layout.html')
