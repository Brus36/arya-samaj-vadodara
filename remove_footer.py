import os
import glob
import re

path = 'c:/Users/Tejas/Antigravity files/arya samaj/aryasamaj_mirror/aryasamaj-vadodara.org/**/*.html'
files = glob.glob(path, recursive=True)

pattern = re.compile(r'\s*<p class="rights">\s*<span>Developed By:</span>\s*<a href="https://codeofgrowth\.com"><span>Codeofgrowth Technologies LLP</span></a>\s*</p>', re.MULTILINE)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
