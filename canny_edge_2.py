import cv2
import numpy as np
def get_detected_lanes(image):

    (height, width) = (image.shape[0], image.shape[1])

    # tunn image into grayscale

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Edge detection kernel
    canny_edge = cv2.Canny(gray_image, 100, 120)

    return canny_edge




# Video = several frames
video = cv2.VideoCapture('lane_detection_video.mp4')

while video.isOpened():
    is_grabbed, frame = video.read() # read function returns to values, the frame and if the frame was grbeed successfully

    if not is_grabbed:
        break

    frame = get_detected_lanes(frame)
    cv2.imshow("Lane Detection", frame)
    cv2.waitKey(20)


video.release()
cv2.destroyAllWindows()



