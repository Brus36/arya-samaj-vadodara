import os, glob, re
html_files = glob.glob("**/*.html", recursive=True)
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'(<span>Arya Samaj Varodara</span>\. All rights reserved\s*</p>)'
    replacement = r'\1\n                          <div style="margin-top: 15px;"><a href="https://visitorbadge.io/status?path=https%3A%2F%2Fbrus36.github.io%2Farya-samaj-vadodara"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fbrus36.github.io%2Farya-samaj-vadodara&label=VISITORS&countColor=%23ff7000" alt="visitor badge"/></a></div>'
    
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
