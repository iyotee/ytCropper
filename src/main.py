import glob
import sys
import os
sys.path.append('/usr/local/lib/python3.9/site-packages')


from download_video import download_video
from trim_video import trim_video
from extract_audio import extract_audio
from face_detection import detect_faces
from speaker_detection import detect_speaker
from crop_frames import crop_frames
from merge_audio_video import merge_audio_video
from pathlib import Path

def main():
    video_url = input("Enter the YouTube video URL: ")
    video_path = download_video(video_url)

    start_time = int(input("Enter the start time (in seconds): "))
    duration = int(input("Enter the duration (in seconds, default is 60): ") or "60")
    trimmed_video_path, trimmed_audio_path = trim_video(video_path, start_time, duration)

    wav_audio_path = extract_audio(trimmed_video_path)

    face_info = detect_faces(trimmed_video_path)
    speaker_index = detect_speaker(trimmed_video_path, wav_audio_path, face_info)

    # Add this line to create an output directory for cropped frames
    output_frames_path = "output_frames"
    Path(output_frames_path).mkdir(parents=True, exist_ok=True)

    cropped_frames_path = crop_frames(trimmed_video_path, output_frames_path, face_info, speaker_index)

    output_video_path = merge_audio_video(cropped_frames_path, video_path, wav_audio_path)

    print(f"Output video saved at: {output_video_path}")

def delete_files_in_folder(folder_path):
    files = glob.glob(f"{folder_path}/*")
    for file in files:
        os.remove(file)

if __name__ == "__main__":
    #When the program is lauch, deleted the output_frames folder to avoid conflit with merging.
    output_frames_path = "output_frames"
    delete_files_in_folder(output_frames_path)
    main()
    print("Thanks for using ytCropper ! - 0xSatoshiba")

    