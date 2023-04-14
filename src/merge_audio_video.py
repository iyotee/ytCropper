import cv2
import os
from moviepy.editor import ImageSequenceClip, AudioFileClip

def merge_audio_video(frames_path, video_path, audio_path):
    frame_files = [os.path.join(frames_path, f) for f in sorted(os.listdir(frames_path))]

    # Read the fps from the original video
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()

    if fps == 0:
        raise ValueError("The fps value is 0. Please check the video file.")

    audio = AudioFileClip(audio_path)
    clip = ImageSequenceClip(frame_files, fps=fps)
    clip = clip.set_audio(audio)

    output_video_path = os.path.join(os.path.dirname(frames_path), "output.mp4")
    clip.write_videofile(output_video_path, codec="libx264", audio_codec='aac')

    return output_video_path
