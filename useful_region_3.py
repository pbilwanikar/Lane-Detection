import cv2
import numpy as np

def region_of_interest(image, region_points):
    mask = np.zeros_like(image)
    # we are going to replace pixels with 0 black - regions we are not interested

    cv2.fillPoly(mask, region_points, 255)

    masked_image = cv2.bitwise_and(image, mask)

    return masked_image


def get_detected_lanes(image):

    (height, width) = (image.shape[0], image.shape[1])

    # tunn image into grayscale

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Edge detection kernel
    canny_image = cv2.Canny(gray_image, 100, 120)

    # we are interested in the lower region of the image,as there are the driving lanes
    region_of_interest_vertices = [
        (0, height),
        (width/2, height*0.65),
        (width, height)
    ]

    # we can get rid of the unrelevant part of the image
    # we just keep the lower traingle region
    cropped_image = region_of_interest(canny_image,
                                       np.array([region_of_interest_vertices], np.int32))



    return cropped_image




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



