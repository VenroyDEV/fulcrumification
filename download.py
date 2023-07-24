import yt_dlp
# help(yt_dlp.YoutubeDL)




video_url = input("add a link to the video : ") 
start_time = int(input("start time of video in seconds: "))
end_time = int(input("end time of video in seconds: "))

ydl_opts = {
    'external_downloader': 'ffmpeg',
    'format': 'bestvideo+bestaudio',
    'download_archive': 'downloaded.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'download_ranges': [f"{start_time}-{end_time}"],
}

video = yt_dlp.YoutubeDL(ydl_opts).download([video_url])
print(video)