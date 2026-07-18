import re

html_file = 'index.html'
with open(html_file, 'r') as f:
    content = f.read()

# Replace fakeBgs fallback in makeDesktopCard, makeMobileCard, makeSearchCard with fakeThumbs
content = re.sub(
    r'const thumbContent=src\?`<img src="\$\{src\}" alt="thumbnail">`:`<div class="th-ph" style="background:\$\{rnd\(fakeBgs,fakeIdx\)\}"></div>`;',
    r'const thumbContent=src?`<img src="${src}" alt="thumbnail">`:`<img src="${rnd(fakeThumbs,fakeIdx)}" alt="thumbnail" style="width:100%;height:100%;object-fit:cover">`;',
    content
)

content = re.sub(
    r'const thumbContent=src\?`<img src="\$\{src\}" alt="thumbnail">`:`<div class="th-ph" style="background:\$\{rnd\(fakeBgs,fakeIdx\)\};width:100%;height:100%"></div>`;',
    r'const thumbContent=src?`<img src="${src}" alt="thumbnail">`:`<img src="${rnd(fakeThumbs,fakeIdx)}" alt="thumbnail" style="width:100%;height:100%;object-fit:cover">`;',
    content
)

with open(html_file, 'w') as f:
    f.write(content)
