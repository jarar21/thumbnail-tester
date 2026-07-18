import subprocess
import json

channels = [
    "https://www.youtube.com/@MrBeast",
    "https://www.youtube.com/@veritasium",
    "https://www.youtube.com/@MarkRober",
    "https://www.youtube.com/@mkbhd",
    "https://www.youtube.com/@LinusTechTips",
    "https://www.youtube.com/@Fireship",
    "https://www.youtube.com/@freecodecamp",
    "https://www.youtube.com/@theslowmoguys"
]

results = []

for channel in channels:
    print(f"Fetching for {channel}...")
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--playlist-end", "5", # get the top 5 most popular videos
        "--default-search", "ytsearch",
        f"{channel}/videos?view=0&sort=p&flow=grid" # fetch popular videos
    ]
    try:
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        for line in output.strip().split('\n'):
            if line:
                data = json.loads(line)
                if data.get('view_count') and data.get('view_count') > 20000000:
                    results.append(data)
                    break
    except Exception as e:
        print(f"Error fetching {channel}: {e}")

print(json.dumps([{"title": r.get('title'), "channel": r.get('channel'), "views": r.get('view_count'), "duration": r.get('duration_string'), "age": r.get('upload_date'), "id": r.get('id'), "description": r.get('description')} for r in results], indent=2))
