import cv2
print("enter q to exit when videocam opens ")

cap = cv2.VideoCapture(0) #can also be -1 



while(True):
        ret, frame=cap.read()  #ret and frame are variables ret will be eithe rtrue or false and frame will capture the frame

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame) #frame is the name of o/p window

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

