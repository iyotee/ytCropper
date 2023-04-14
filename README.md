# 🎞 ytCropper

ytCropper is a program that allows users to crop a specified duration of a YouTube video, while also detecting and tracking faces and/or speakers in the video. This is accomplished using AI-powered algorithms, using Dlib and DeepSearch Deep pre-trained models.

## Installation

### Requirements

Make sure you have the following requirements installed:

- Python 3.7+
- yt_dlp
- moviepy
- dlib
- wget
- pre-trained models for face detection and speaker recognition (see below for instructions)

First, install the requirements by running:

```bash
pip3 install -use-pep517 -r requirements.txt
```

You can install all the necessary by running:

```bash
chmod +x create.sh
./create.sh
```

This bash will create all the necessaries folders and files for the projects as well as download the necessaries models

Pre-trained Models

To download the necessary pre-trained models, run the following commands:

```bash
wget https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```



#### Usage
Run python ytCropper.py to start the program.

```bash
python src/main.py
```

Provide the YouTube video URL when prompted.

Specify the duration of the short video you wish to create. If no duration is provided, the default value of 60 seconds will be used.

Provide the start time for the short video.

The original video and audio will be trimmed to match the specified duration and start time.

Face detection will be performed using Dlib, an open-source library for machine learning, to detect faces in the trimmed video. The number of faces detected in each frame will be monitored.

If a face is detected, the program will track the face and crop the current frame. The crop will be centered on the face and will be equal to the height of the original frame. The width of the crop will be in a 9:16 aspect ratio. If there are no faces detected, the crop will be centered in the middle of the frame and will maintain the 9:16 aspect ratio.

In the case of multiple faces detected per frame, the program will use DeepSearch, a powerful AI tool for speech-to-text transcription and speaker recognition, to detect the speaker. 

Then, the program will track the speaker and crop the frame with the same parameters as before when a face was detected with Dlib.

Once all of the cropping is completed, the frames will be merged with the trimmed audio.

The final video will be exported to a separate folder.

That's it folks ! Enjoy it ! 
