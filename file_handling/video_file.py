import cv2
# pip install opencv-python
import os

if os.path.exists(r'D:\guitar.mp4'):
    cap = cv2.VideoCapture(r'D:\guitar.mp4')

    if not cap.isOpened():
        print("Error opening video file.")
    else:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video Playback', frame)

            # Quit on 'q' key
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
else:
    print("Video file doesn't exist!")
