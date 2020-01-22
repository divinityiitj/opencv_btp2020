import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #to save the video you have recorded and output.avi is the file name which you want it to save as 

while(cap.isOpened()):
    ret, frame=cap.read()  #ret and frame are variables ret will be either rtrue or false and frame will capture the frame
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #these are all built in functions no need to get scared.

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray is just storing the new frame which has been converted to grayscale using the second argument
    cv2.imshow('frame', frame) #frame is the name of o/p window

    if cv2.waitKey(1) & 0xFF == ord('q'): #0xFF is for 64 bit machine
            break

cap.release() # to remove the allocated memory to cap variable its a good programming practice
cv2.destroyAllWindows() # to close all the windows 