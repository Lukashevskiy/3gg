import cv2
import numpy as np
import sys

arrow = cv2.imread('arrow.png')
gray_arrow = cv2.cvtColor(arrow, cv2.COLOR_BGR2GRAY)

rect, thresh_arrow = cv2.threshold(gray_arrow, 10, 255, 0)

contours = cv2.findContours(thresh_arrow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

arrow_countour = contours[0]
# video = 0
# video = int(sys.argv[1])

# videos = ['./videos/video2.mp4', './videos/video.mp4']
# capture = cv2.VideoCapture(videos[video])


# while capture.isOpened():
#     rect, image = capture.read()
#     img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     rect_binary, binary_image = cv2.threshold(img_hsv, 150, 255, cv2.THRESH_BINARY)
#     cv2.imshow('frame_image_binary', binary_image)

#     if cv2.waitKey(25) == ord('q'):
#         break

cv2.namedWindow('Arrow', cv2.WINDOW_KEEPRATIO)
cv2.drawContours(arrow, [arrow_countour], 0, (255, 0, 0), 4)

moments = cv2.moments(arrow_countour)
centroid = tuple(map(int, (moments['m10'] / moments['m00'], moments['m01'] / moments['m00']))) 

eps = 0.01 * cv2.arcLength(arrow_countour, True)
approx = cv2.approxPolyDP(arrow_countour, eps, True)

for p in approx:
    cv2.circle(arrow, tuple(*p), 6, (0, 255, 0), 2)

cv2.circle(arrow, centroid, 4, (0, 255, 4), 4)

cv2.imshow("Arrow", arrow)

print(f'Area = {cv2.contourArea(arrow_countour)}, Perimeter = {cv2.arcLength(arrow_countour, closed=True)}')
print(f'moments = {moments}')


# capture.release
cv2.waitKey()
cv2.destroyAllWindows()
