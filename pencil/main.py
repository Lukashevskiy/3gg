import cv2
import os
import numpy as np 

images_dir = './images'
os.chdir(images_dir)
images_name = os.listdir()
# print(images_name[0])
# cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
ans = 0
for image_name in images_name:
    pencil_count = 0
    # image_name = images_name[11]
    # print(f'image: {image_name}')
    img = cv2.imread('./'+image_name)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_filtered = filter(lambda x: cv2.contourArea(x) > 10000, contours)

    for contour in contours_filtered:
        min_area_rect = cv2.minAreaRect(contour)
        w, h = min_area_rect[1]
        if w > h:
            w, h = h, w

        dd = h / w
        if dd <= 9:
            continue
        pencil_count += 1
        # print(cv2.contourArea(contour))
        # print(min_area_rect)
        # box = np.int0(cv2.boxPoints(min_area_rect))
        # print(box)
        # cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    print(f'image - {image_name}, penciles - {pencil_count}')
    ans += pencil_count
    # cv2.imshow(f'img', img)

print(ans)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

