#!/bin/bash

# Créer les dossiers
mkdir output_frame
mkdir input_videos
mkdir output_videos
mkdir models
cd models
mkdir deepsearch
mkdir dlib

# Télécharger les fichiers nécessaires pour Dlib
cd dlib
wget https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2
bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2

# Télécharger les fichiers nécessaires pour DeepSearch
cd ../deepsearch
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

echo "Les dossiers et les fichiers nécessaires ont été créés avec succès."

