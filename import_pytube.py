"""Imports the pytube module to allow downloading YouTube videos."""

import pytube

# Download video
yt = pytube.YouTube("https://www.youtube.com/watch?v=6yQEA18C-XI")
video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path="./")

# Copy file to iPhone 
#iphone_music_folder = "/path/to/iphone/music/folder"
#filename = Path(out_file).name
#shutil.copy(out_file, iphone_music_folder + "/" + filename)

print(f"Downloaded {video.title}")
