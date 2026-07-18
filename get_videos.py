import urllib.request
import re

channels = ['mrbeast', 'veritasium', 'markrober', 'mkbhd', 'linustechtips', 'fireship', 'freecodecamp']
for ch in channels:
    try:
        url = f"https://www.youtube.com/@{ch}/videos"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        title_match = re.search(r'"title":\{"runs":\[\{"text":"([^"]+)"\}\]', html)
        id_match = re.search(r'"videoId":"([^"]+)"', html)
        if title_match and id_match:
            print(f"{ch}: {id_match.group(1)} - {title_match.group(1)}")
    except Exception as e:
        print(f"Error {ch}: {e}")
