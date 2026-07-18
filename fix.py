with open('index.html', 'r') as f:
    content = f.read()
import re

content = re.sub(r'let thumbnails=\[\], activeIdx=0, currentView=\'desktop\';', 'let thumbnails=[], activeIdx=0, currentView=\'desktop\';\nrefreshAll();', content)
with open('index.html', 'w') as f:
    f.write(content)
