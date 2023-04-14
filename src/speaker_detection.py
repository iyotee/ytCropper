import deepspeech
import numpy as np
import wave
import os
from python_speech_features import mfcc
from sklearn.cluster import KMeans
from collections import Counter

def read_wav_file(wav_audio_path):
    with wave.open(wav_audio_path, 'rb') as wav_file:
        rate = wav_file.getframerate()
        frames = wav_file.getnframes()
        audio = np.frombuffer(wav_file.readframes(frames), dtype=np.int16)

    return audio, rate

def compute_mfcc(audio, rate):
    features = mfcc(audio, rate)
    return features

def detect_speaker(video_path, wav_audio_path, face_info, n_clusters=2):
    print("Starting speaker detection...")
    
    model_path = "models/deepspeech/deepspeech-0.9.3-models.pbmm"
    scorer_path = "models/deepspeech/deepspeech-0.9.3-models.scorer"

    model = deepspeech.Model(model_path)
    model.enableExternalScorer(scorer_path)

    audio, rate = read_wav_file(wav_audio_path)
    mfcc_features = compute_mfcc(audio, rate)

    if len(mfcc_features) == 0:
        print("No features were extracted. Please ensure there are speakers in the video.")
        return None

    # Adjusting KMeans parameters
    kmeans = KMeans(n_clusters=2, random_state=42, tol=1e-4, max_iter=300)
    kmeans.fit(mfcc_features)

    speaker_labels = kmeans.labels_
    
    # Monitoring: Print the number of frames for each speaker
    speaker_count = Counter(speaker_labels)
    print("Speaker frame count:", speaker_count)

    # Find the most frequent speaker.
    most_frequent_speaker = speaker_count.most_common(1)[0][0]

    print(f"Most frequent speaker: {most_frequent_speaker}")
    print("Speaker detection completed. wait few seconds ...")

    return most_frequent_speaker
