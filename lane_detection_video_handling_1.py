import cv2
import numpy as np

# Video = several frames
video = cv2.VideoCapture('lane_detection_video.mp4')

while video.isOpened():
    is_grabbed, frame = video.read() # read function returns to values, the frame and if the frame was grbeed successfully

    if not is_grabbed:
        break

    cv2.imshow("Lane Detection", frame)
    cv2.waitKey(100)


video.release()
cv2.destroyAllWindows()



