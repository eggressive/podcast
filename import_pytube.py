"""
Imports the pytube module to allow downloading YouTube videos.

To run this:
python program.py https://www.youtube.com/watch?v=VIDEO_ID
"""

import sys
import pytube

if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments")
    print(f"Usage: python {sys.argv[0]} <video_url>")
    sys.exit(1)

# Download video
VIDEO_URL = sys.argv[1]
try:
    yt = pytube.YouTube(VIDEO_URL)
except Exception as e:
    print(f"Error: Video unavailable or invalid URL - {VIDEO_URL}", e)
    sys.exit(1)

video = yt.streams.filter(only_audio=False).first()
# for high-res video:
#video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
out_file = video.download(output_path="./")

print(f"Downloaded {video.title}")
