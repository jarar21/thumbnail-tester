import json
import re

data = [
  {
    "title": "Survive 30 Days Chained To A Stranger, Win $250,000",
    "channel": "MrBeast",
    "views": "74M views",
    "duration": "35:04",
    "age": "2 weeks ago",
    "id": "iYlODtkyw_I",
    "desc": "imagine being chained to a random stranger for 30 days lol"
  },
  {
    "title": "Engineers vs Junkyard RC Car Death Match",
    "channel": "Mark Rober",
    "views": "29M views",
    "duration": "18:52",
    "age": "4 months ago",
    "id": "Xg1ro-zG7AM",
    "desc": "Never trust a lemon with a motor... Learn to embrace failure while having tons of fun with CrunchLabs"
  },
  {
    "title": "HOW MANY BALLOONS TO FLY? (Mini Games Battle)",
    "channel": "Dude Perfect",
    "views": "33M views",
    "duration": "18:34",
    "age": "5 months ago",
    "id": "A10M15TdZpI",
    "desc": "How many balloons will float a kid? How much milk can be bench pressed?"
  },
  {
    "title": "The World's Most Important Machine",
    "channel": "Veritasium",
    "views": "33M views",
    "duration": "55:00",
    "age": "6 months ago",
    "id": "MiUHjLxm3V0",
    "desc": "The insane machines that make the most advanced computer chips."
  },
  {
    "title": "SIDEMEN GUESS THE FOOTBALLER ft Erling Haaland",
    "channel": "Sidemen",
    "views": "16M views",
    "duration": "47:28",
    "age": "4 months ago",
    "id": "k6tPeMMUn6A",
    "desc": "This might be the biggest collab we've ever done... Guess the footballer with Erling Haaland"
  },
  {
    "title": "I Bought The Apple Vision Pro!",
    "channel": "Marques Brownlee",
    "views": "20M views",
    "duration": "22:15",
    "age": "5 months ago",
    "id": "86Gy035z_KA",
    "desc": "Apple Vision Pro unboxing and review..."
  },
  {
    "title": "I bought the CHEAPEST Gaming PC on Amazon",
    "channel": "Linus Tech Tips",
    "views": "5M views",
    "duration": "14:20",
    "age": "1 month ago",
    "id": "jNQXAC9IVRw",
    "desc": "This PC was only $150 on Amazon..."
  }
]

with open('index.html', 'r') as f:
    content = f.read()

titles = [d['title'] for d in data]
channels = [{"name": d['channel'], "i": d['channel'][0], "c": ""} for d in data]
colors = ['#1a73e8', '#2e7d32', '#c62828', '#6a1b9a', '#f57f17', '#424242', '#546e7a']
for i, c in enumerate(channels):
    c['c'] = colors[i]
views = [d['views'] for d in data]
ages = [d['age'] for d in data]
durs = [d['duration'] for d in data]
thumbs = [f"https://i.ytimg.com/vi/{d['id']}/hqdefault.jpg" for d in data]
descs = [d['desc'] for d in data]

def replace_array(name, arr_str):
    global content
    content = re.sub(f"const {name}=\\[.*?\\];", f"const {name}={arr_str};", content, flags=re.DOTALL)

replace_array('fakeTitles', json.dumps(titles))
replace_array('fakeChannels', json.dumps(channels))
replace_array('fakeViews', json.dumps(views))
replace_array('fakeAges', json.dumps(ages))
replace_array('fakeDurs', json.dumps(durs))
replace_array('fakeThumbs', json.dumps(thumbs))
replace_array('fakeDescs', json.dumps(descs))

with open('index.html', 'w') as f:
    f.write(content)
