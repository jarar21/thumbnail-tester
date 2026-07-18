import re

html_file = 'index.html'
with open(html_file, 'r') as f:
    content = f.read()

fake_channels = "[{name:'MrBeast',i:'M',c:'#1a73e8'},{name:'Veritasium',i:'V',c:'#6a1b9a'},{name:'Mark Rober',i:'M',c:'#2e7d32'},{name:'MKBHD',i:'M',c:'#424242'},{name:'Linus Tech Tips',i:'L',c:'#546e7a'},{name:'Fireship',i:'F',c:'#e65100'},{name:'freeCodeCamp.org',i:'C',c:'#c62828'}]"
fake_titles = "['$456,000 Squid Game In Real Life!','The Absurdity of Detecting Gravitational Waves','Backyard Squirrel Maze 1.0- Ninja Warrior Course','I Bought The Apple Vision Pro!','I bought the CHEAPEST Gaming PC on Amazon','I Built a Startup in 24 Hours','Python for Beginners - Full Course']"
fake_views = "['500M views','20M views','110M views','15M views','5M views','2M views','40M views']"
fake_ages = "['2 years ago','1 year ago','3 years ago','3 months ago','1 month ago','1 year ago','2 years ago']"
fake_durs = "['25:41','15:08','21:40','22:15','14:20','8:10','4:20:10']"
fake_bgs = "['#b71c1c','#6a1b9a','#2e7d32','#424242','#546e7a','#e65100','#c62828']"
fake_descs = "['I recreated every single set from Squid Game in real life...','Here is how we detected gravitational waves for the first time...','I built an insane obstacle course for the squirrels in my backyard...','Apple Vision Pro unboxing and review...','This PC was only $150 on Amazon...','Watch me build a real startup in just one day...','Learn Python in this complete course for beginners...']"
fake_thumbs = "['https://i.ytimg.com/vi/0e3GPea1Tyg/maxresdefault.jpg','https://i.ytimg.com/vi/iphcyNWFDsM/maxresdefault.jpg','https://i.ytimg.com/vi/hFZFjoX2cGg/maxresdefault.jpg','https://i.ytimg.com/vi/86Gy035z_KA/maxresdefault.jpg','https://i.ytimg.com/vi/8U331_a2mRk/maxresdefault.jpg','https://i.ytimg.com/vi/7mCbF6vXFzo/maxresdefault.jpg','https://i.ytimg.com/vi/rfscVS0vtbw/maxresdefault.jpg']"

content = re.sub(r'const fakeChannels=\[.*?\];', f'const fakeChannels={fake_channels};', content)
content = re.sub(r'const fakeTitles=\[.*?\];', f'const fakeTitles={fake_titles};', content)
content = re.sub(r'const fakeViews=\[.*?\];', f'const fakeViews={fake_views};', content)
content = re.sub(r'const fakeAges=\[.*?\];', f'const fakeAges={fake_ages};', content)
content = re.sub(r'const fakeDurs=\[.*?\];', f'const fakeDurs={fake_durs};', content)
content = re.sub(r'const fakeBgs=\[.*?\];', f'const fakeBgs={fake_bgs};', content)
content = re.sub(r'const fakeDescs=\[.*?\];', f'const fakeDescs={fake_descs};', content)

content = content.replace("const fakeDescs=", f"const fakeThumbs={fake_thumbs};\nconst fakeDescs=")

with open(html_file, 'w') as f:
    f.write(content)
