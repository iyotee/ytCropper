import dlib
import cv2
import numpy as np
import os

def detect_faces(video_path):
    model_path = "models/dlib/shape_predictor_68_face_landmarks.dat"
    face_detector = dlib.get_frontal_face_detector()
    landmark_predictor = dlib.shape_predictor(model_path)

    cap = cv2.VideoCapture(video_path)

    face_info = []

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray)

        frame_faces = []

        for rect in faces:
            x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()

            landmarks = landmark_predictor(gray, rect)
            # Use the landmarks for further processing if needed

            frame_faces.append((x, y, w, h))

        face_info.append(frame_faces)

        print(f"Frame: {i + 1}/{frame_count}, Faces detected: {len(frame_faces)}")

    cap.release()
    return face_info
