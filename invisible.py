import numpy as np
import cv2
import time



capture = cv2.VideoCapture("video.mp4")

time.sleep(2)
count = 0
background = 0

for i in range(60):
    ret , background = capture.read()
    if ret == False : 
        continue 
  
background = np.flip(background, axis = 1)
    

while (capture.isOpened()): 
    ret, img = capture.read() 
    if not ret : 
        break 
    count = count + 1
    
  
    img = np.flip(img, axis = 1) 

    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

    lower_red = np.array([100, 30, 30])
    upper_red = np.array([100, 255, 255])
    mask1 =cv2.inRange(hsv, lower_red, upper_red)


    lower_red = np.array([155, 70, 70])
    upper_red = np.array([180, 255, 255])
    mask2 =cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
    mask2 = cv2.bitwise_not(mask1) 
  

    result1 = cv2.bitwise_and(background, background , mask = mask1)
    result2 = cv2.bitwise_and(img, img , mask = mask2)
    final_output = cv2.addWeighted(result1 , 1 , result2 , 1 , 0)

    cv2.imshow("Invisible Cloak!",final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break



