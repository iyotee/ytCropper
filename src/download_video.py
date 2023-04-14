import yt_dlp
import os

def download_video(video_url):
    output_path = os.path.join("input_videos", "%(title)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_path,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "keepvideo": True,
        "quiet": False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    info = yt_dlp.YoutubeDL(ydl_opts).extract_info(video_url, download=False)
    video_path = ydl.prepare_filename(info)
    return video_path
