import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam")

img_counter = 0
while True:
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        #ASCI CODE FOR ESCAPE
        print("Escape pressed, closing app")
        break
    if k%256 == 32:
        #ASCI CODE FOR SPACE
        img_name = "opencv_frame_{}.png".format(img_counter)
        img_counter += 1
        cv2.imwrite(img_name, frame)
        print("Screenshot taken")

cam.release()


cam.destroyAllWindows()