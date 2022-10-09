import cv2 as cv

# Define video capture
vid = cv.VideoCapture(0)
#Check if camera can be opened
if not vid.isOpened():
    print("Camera cannot be opened..")
    exit()
while True:
    ret, frame = vid.read()
    if not ret:
        print("Cannot read frame of the capture")
        break
    cv.imshow('recognision', frame)
    print("FPS: ", cv.CAP_PROP_FPS)
    #break loop
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
#Printing FPS
#print("FPS: ", cv.CAP_PROP_FPS)
