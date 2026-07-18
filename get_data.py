import subprocess
import json

channels = [
    "https://www.youtube.com/@MrBeast",
    "https://www.youtube.com/@MarkRober",
    "https://www.youtube.com/@dudeperfect",
    "https://www.youtube.com/@kurzgesagt",
    "https://www.youtube.com/@veritasium",
    "https://www.youtube.com/@mkbhd",
    "https://www.youtube.com/@Sidemen"
]

results = []

for channel in channels:
    print(f"Fetching for {channel}...")
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--playlist-items", "1-20", # Look at the last 20 videos
        "--match-filter", "view_count > 20000000", # Filter for >20M views
        "--default-search", "ytsearch",
        f"{channel}/videos"
    ]
    try:
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        for line in output.strip().split('\n'):
            if line:
                data = json.loads(line)
                results.append(data)
                break # Just need the latest one that matches
    except Exception as e:
        print(f"Error fetching {channel}: {e}")

print(json.dumps([{"title": r.get('title'), "channel": r.get('channel'), "views": r.get('view_count'), "duration": r.get('duration_string'), "age": r.get('upload_date'), "id": r.get('id'), "description": r.get('description')} for r in results], indent=2))
