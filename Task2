import numpy as np
import cv2

capture= cv2.VideoCapture("C:\\Users\\Ananya\\video_task.mp4")
frame_width = 500
frame_height = 568
fps = int(capture.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for .mp4
out_red = cv2.VideoWriter('red_output.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)
out_blue = cv2.VideoWriter('blue_output.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)
out_green = cv2.VideoWriter('green_output.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)
out_sharpened = cv2.VideoWriter('sharpened_output.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)
out_blurred = cv2.VideoWriter('blurred_output.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)
while True:
    ret,frame=capture.read()
    frame=cv2.resize(frame,(500,568))
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_red=np.array([60,0,0])
    high_red=np.array([179,255,255])
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    out_red.write(red_mask)

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    out_blue.write(blue_mask)

    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    out_green.write(green_mask)

    blurred = cv2.GaussianBlur(frame, (9, 9), 3)
    out_blurred.write(blurred)

    sharpen_kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
  ])
    sharpened = cv2.filter2D(frame, -1, sharpen_kernel)
    out_sharpened.write(sharpened)

    #frame=cv2.flip(frame,1) use 1 and -1 to mirror
    cv2.imshow('frame',frame)
    cv2.imshow('red',red_mask)
    cv2.imshow('blue',blue_mask)
    cv2.imshow('green',green_mask)
    cv2.imshow('blurred',blurred)
    cv2.imshow('sharpened',sharpened)
    k=cv2.waitKey(25)
    if k==ord('k'):
        break
    

capture.release()
cv2.destroyAllWindows()