from moviepy.editor import *

def trim_video(video_path, start_time, duration):
    video = VideoFileClip(video_path)

    end_time = start_time + duration
    trimmed_video = video.subclip(start_time, end_time)

    output_video_path = os.path.join("output_videos", "trimmed_video.mp4")
    trimmed_video.write_videofile(output_video_path, codec="libx264")

    output_audio_path = os.path.join("output_videos", "trimmed_audio.mp3")
    trimmed_video.audio.write_audiofile(output_audio_path)

    return output_video_path, output_audio_path
