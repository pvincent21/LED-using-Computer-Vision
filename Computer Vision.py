
import cv2
import serial
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

ser = serial.Serial(port="COM5", baudrate=115200)
time.sleep(2)

while True:
    
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame) 

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]  # List of 21 Landmark points
        bbox = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint = hand1['center']  # center of the hand cx,cy
        handType = hand1["type"]  # Handtype Left or Right

        lmlist = hands[0]
        if lmList:
            fingers = detector.fingersUp(lmlist)
            #print(fingers)
            #ser.sendData(fingers)
            
            if fingers == [0, 0, 0, 0, 0]:
                ser.write(bytes('0', encoding='utf-8'))
                cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
                #print(0)
            if fingers == [0, 1, 0, 0, 0]:
                ser.write(bytes('1', 'utf-8'))
                cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

            if fingers == [0, 1, 1, 0, 0]:
                ser.write(bytes('2', 'utf-8'))
                cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

            if fingers == [0, 1, 1, 1, 0]:
                ser.write(bytes('3', 'utf-8'))
                cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

            if fingers == [0, 1, 1, 1, 1]:
                ser.write(bytes('4', 'utf-8'))
                cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

            if fingers == [1, 1, 1, 1, 1]:
                ser.write(bytes('5', 'utf-8'))
                cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            
    
    # Display
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()

