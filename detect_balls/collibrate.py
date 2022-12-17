import cv2
import numpy as np
 
# blue 98 232 120
# orange 7 230 236
# green 58 135 127
# yellow 21 218 184
 

balls_color = []

cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cam = cv2.VideoCapture(0)
position = [0, 0]
 
 
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        position = [y, x]
 
 
cv2.setMouseCallback("Camera", on_mouse_click)
 
measures = []
hsv = [[[255,0,0]]]
 
while cam.isOpened():
    ret, frame = cam.read()
    pixel = frame[position[0], position[1], :]
    measures.append(pixel)
    if len(measures) == 10:
        bgr = np.uint8([[np.mean(measures, 0)]])
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        measures.clear()

    # print(hsv)
    cv2.putText(frame, f"HSV = {hsv}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,0,0])
    for i, ball_color in enumerate(balls_color):
        cv2.putText(frame, f"HSV = {ball_color}", (10, 60+20*i), cv2.FONT_HERSHEY_COMPLEX, 0.7, [0,0,0])

    cv2.circle(frame, position[::-1], 5, (255,0,0), 2)
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('a'):
        balls_color.append(hsv)
    if key == ord('d'):
        balls_color.clear()

 
cam.release()
 