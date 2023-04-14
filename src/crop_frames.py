import cv2
import os

def crop_frames(video_path, output_frames_path, face_info, speaker_index):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    height, width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    crop_x_start = None
    speaker_change_count = 0
    confirmed_speaker_index = speaker_index

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_info[i]

        if len(faces) == 0:
            crop = crop_center(frame, height, width)
        elif len(faces) == 1 or confirmed_speaker_index is None:
            crop, crop_x_start = crop_face(frame, faces[0], height, width, crop_x_start)
        else:
            if speaker_index != confirmed_speaker_index:
                speaker_change_count += 1
                if speaker_change_count >= 3:
                    confirmed_speaker_index = speaker_index
                    speaker_change_count = 0
            else:
                speaker_change_count = 0

            crop, crop_x_start = crop_face(frame, faces[confirmed_speaker_index], height, width, crop_x_start)

        cv2.imwrite(os.path.join(output_frames_path, f"frame_{i:04d}.png"), crop)

    cap.release()
    return output_frames_path

def crop_center(frame, height, width):
    crop_height = height
    crop_width = int(height * 9 / 16)
    x = (width - crop_width) // 2
    y = 0
    crop = frame[y:y+crop_height, x:x+crop_width]
    return crop

def crop_face(frame, face_rect, height, width, crop_x_start):
    x, y, w, h = face_rect
    crop_height = height
    crop_width = int(height * 9 / 16)

    x_center = x + w // 2

    threshold = 50
    if crop_x_start is None or abs(x_center - (crop_x_start + crop_width // 2)) > threshold:
        crop_x_start = max(0, x_center - crop_width // 2)

    x_end = min(width, crop_x_start + crop_width)

    if x_end - crop_x_start < crop_width:
        crop_x_start = x_end - crop_width

    crop = frame[0:crop_height, crop_x_start:x_end]
    return crop, crop_x_start
