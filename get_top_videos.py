import subprocess
import json

channels = [
    "mkbhd",
    "LinusTechTips",
    "kurzgesagt"
]

results = []

for channel in channels:
    print(f"Fetching for {channel}...")
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--playlist-end", "5",
        "--default-search", "ytsearch",
        f"https://www.youtube.com/@{channel}/videos"
    ]
    try:
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        for line in output.strip().split('\n'):
            if line:
                data = json.loads(line)
                results.append({
                    "title": data.get('title'),
                    "channel": data.get('channel'),
                    "views": data.get('view_count'),
                    "id": data.get('id'),
                    "duration": data.get('duration_string'),
                    "age": data.get('upload_date')
                })
    except Exception as e:
        print(f"Error fetching {channel}: {e}")

print(json.dumps(results, indent=2))
