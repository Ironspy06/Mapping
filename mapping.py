import cv2 as cv
import numpy as np
import KeyPressModule as kp
from time import sleep
import random
config = {
  "apiKey": "AIzaSyCjULZ1FxzQHvMji5OR-OZnyOxY9KwV_GA",
  "authDomain": "robot-68d4d.firebaseapp.com",
  "databaseURL": "https://robot-68d4d-default-rtdb.firebaseio.com",
  "projectId": "robot-68d4d",
  "storageBucket": "robot-68d4d.appspot.com",
  "messagingSenderId": "1071151697658",
  "appId": "1:1071151697658:web:635787e41378b95fa54343",
  "measurementId": "G-42522D1CWQ"
}

firebase=pyrebase.initialize_app(config)

db=firebase.database()
#parameters
#parameters
fspeed=117/10 #forward speed in cm/s  (15 cm/s)
aspeed=360/10
interval=0.25

dInterval=fspeed*interval
aInterval=aspeed*interval
kp.init()
x = 500
y = 500
points=[(0,0),(0,0)]
# a=0
def automaticMovement():
    global x,y
    x+=random.randint(0,1)
    y+=random.randint(-1,1)



    return [x,y]
def getKeyboardInput():
    global x,y
    # d=0
    if kp.getKey("LEFT"):
        x-=1
        # d=dInterval
        # a=-180
    elif kp.getKey("RIGHT"):
        x+=1
        # d = -dInterval
        # a = 180
    if kp.getKey("UP"):
        y-=1

        # a = 270
    elif kp.getKey("DOWN"):
        y+=1
        # d = -dInterval
        # a = -90

    return [x,y]

def drawPoints(img, points):
    for point in points:
        cv.circle(img, point, 5, (0, 0, 255), cv.FILLED)
    cv.circle(img,points[-1],8,(0,255,0),cv.FILLED)
    cv.putText(img,f'({(points[-1][0]-500)/100},{-(points[-1][1]-500)/100})m',(points[-1][0]+10,points[-1][1]+30),cv.FONT_HERSHEY_PLAIN,1,(255,0,255),1)





while True:



    vals=getKeyboardInput()
    print(vals[0],vals[1])

    # vals2 = automaticMovement()  # automatic motion mapping code
    # img = np.zeros((1000, 1000, 3), np.uint8)
    # if (points[-1][0] != vals2[0] or points[-1][1] != vals2[1]):
    #     points.append((vals2[0], vals2[1]))



    img = np.zeros((1000, 1000, 3), np.uint8)
    if(points[-1][0]!=vals[0] or points[-1][1]!=vals[1]):
        points.append((vals[0], vals[1]))
    drawPoints(img, points)
    cv.imshow("Output", img)
    cv.waitKey(1)
