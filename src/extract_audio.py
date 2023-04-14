import os
from pydub import AudioSegment

def extract_audio(video_path):
    audio = AudioSegment.from_file(video_path, format="mp4")
    wav_audio_path = os.path.join("output_videos", "audio.wav")
    audio.export(wav_audio_path, format="wav")
    return wav_audio_path
