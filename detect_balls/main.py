import cv2
import numpy as np
 
blue = [97, 208, 135]
blue_lower = np.array([blue[0] - 15, blue[1] - 20, 0])
blue_higher = np.array([blue[0] + 15, blue[1] + 20, 255])
 
red = [1, 243, 127]
red_lower = np.array([red[0] - 5, red[1] - 20, 0])
red_higher = np.array([red[0] + 5, red[1] + 20, 255])
 
green = [55, 176, 113]
green_lower = np.array([green[0] - 15, green[1] - 20, 0])
green_higher = np.array([green[0] + 15, green[1] + 20, 255])
 
yellow = [22, 193, 161]
yellow_lower = np.array([yellow[0] - 15, yellow[1] - 20, 0])
yellow_higher = np.array([yellow[0] + 15, yellow[1] + 20, 255])

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, 500)
 
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
 

def detect_ball(hsv, lower, higher, mask_name):
    mask = cv2.inRange(hsv, lower, higher)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    is_detected = False
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        x, y = map(int, (x, y))
        radius = int(radius)
        if radius > 30:
            is_detected = True
            cv2.circle(frame, (x, y), radius, (255, 0, 0), 2)
    cv2.imshow(f"Mask: {mask_name}", mask)
    return is_detected

is_detected = {'Blue':False, 'Red':False, 'Green':False, 'Yellow':False }
bgr_colors = {'Blue':[0, 0, 255], 'Red':[255, 0, 0], 'Green':[0, 255, 0], 'Yellow':[255, 191, 0]}
while cam.isOpened():
    ret,frame = cam.read()
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
    
    is_detected['Blue'] = detect_ball(hsv, blue_lower, blue_higher, "Blue")
    is_detected['Red'] = detect_ball(hsv, red_lower, red_higher, "Red")
    is_detected['Green'] = detect_ball(hsv, green_lower, green_higher, "Green")
    is_detected['Yellow'] = detect_ball(hsv, yellow_lower, yellow_higher, "Yellow")
    for i, (color, is_detect) in enumerate(is_detected.items()):
        if is_detect:
            cv2.circle(frame, (10, 30+20*i), 10, bgr_colors[color], 2)
    cv2.imshow("Camera", frame)
 
    key = cv2.waitKey(1)
    if key == ord('d'):
        break