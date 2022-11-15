import cv2 as cv
import numpy as np
import pyrebase
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

firebase = pyrebase.initialize_app(config)

db = firebase.database()

x = 500
y = 500
points = [(0, 0), (0, 0)]

points1 = [(0, 0), (0, 0)]
points2 = [(0, 0), (0, 0)]
points3 = [(0, 0), (0, 0)]
# a=0
movement = [0]
flag = -1
flag1 = -1
flag2 = -1
flag3 = -1
flag4 = -1
flag5 = -1
x1 = 0
y1 = 0
x2, y2, x3, y3 = 0, 0, 0, 0


def Movement():
    global x, y, x1, y1, x2, y2, flag1, flag, flag2, flag3, flag4, flag5
    global x3, y3
    orient1 = db.child('Motion').child('Orientation').get()
    #UltraSonic = db.child('Motion').child('US').get()
    if orient1.val() == 1:  # forward

        if orient1.val() != flag1:
            movement.append(orient1.val())
            flag1 = orient1.val()
        print(movement)

        if movement[-2] == 3:
            x2 = x - 10
            y2 = y
            movement.pop(1)
            flag = -1
        if movement[-2] == 4:
            x2 = x + 10
            y2 = y
            movement.pop(1)
            flag3 = -1
        if movement[-2] == 2:
            x2 = x
            y2 = y + 10
            movement.pop(1)
            flag5 = -1
        y -= 10
    if orient1.val() == 2:  # backward
        if orient1.val() != flag5:
            movement.append(orient1.val())
            flag5 = orient1.val()
            if movement[-2] == 3:
                x3 = x - 10
                y3 = y
                movement.pop(1)
                flag = -1
            if movement[-2] == 4:
                x3 = x + 10
                y3 = y
                movement.pop(1)
                flag3 = -1
            if movement[-2] == 1:
                x3 = x
                y3 = y - 10
                movement.pop(1)
                flag1 = -1
        y += 10
    if orient1.val() == 3:  # left

        if orient1.val() != flag:
            movement.append(orient1.val())
            flag = orient1.val()
        print(movement)
        if movement[-2] == 1:
            x1 = x
            y1 = y - 10
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag1 = -1
        if movement[-2] == 2:
            x1 = x
            y1 = y + 10
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag5 = -1
        if movement[-2] == 4:
            x1 = x + 10
            y1 = y
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag3 = -1
        x -= 10

    if orient1.val() == 4:  # right
        if orient1.val() != flag3:
            movement.append(orient1.val())
            flag3 = orient1.val()
        print(movement)
        if movement[-2] == 1:
            x1 = x
            y1 = y - 10
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag1 = -1
        if movement[-2] == 2:
            x1 = x
            y1 = y + 10
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag5 = -1
        if movement[-2] == 3:
            x1 = x - 10
            y1 = y
            print("X and y values")
            print(x1, y1)
            movement.pop(1)
            flag = -1

        x += 10
    else:
        x += 0
        y += 0

    return [x, y, x1, y1, x2, y2, x3, y3]


def automaticMovement():
    global x, y
    x += random.randint(0, 1)
    y += random.randint(-1, 1)

    return [x, y]


def drawObj(img2, points2):
    # if x!=0 and y!=0:
    for point in points2:
        cv.circle(img2, point, 8, (255, 0, 0), cv.FILLED)


def drawPoints(img1, Points1):
    for point in Points1:
        cv.circle(img1, point, 5, (0, 0, 255), cv.FILLED)
    cv.circle(img1, Points1[-1], 8, (0, 255, 0), cv.FILLED)

    cv.putText(img1, f'({(Points1[-1][0] - 500) / 100},{-(Points1[-1][1] - 500) / 100})m',
               (Points1[-1][0] + 10, Points1[-1][1] + 30), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


while True:

    vals2 = Movement()  # automatic motion mapping code
    # print(vals2[0],vals2[1])
    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] != vals2[0] or points[-1][1] != vals2[1]:
        points.append((vals2[0], vals2[1]))
    # img = np.zeros((1000, 1000, 3), np.uint8)
    # if(points[-1][0]!=vals[0] or points[-1][1]!=vals[1]):
    #     points.append((vals[0], vals[1]))
    if (points1[-1][0] != vals2[2] or points1[-1][1] != vals2[3]):
        points1.append((vals2[2], vals2[3]))
    if (points2[-1][0] != vals2[4] or points2[-1][1] != vals2[5]):
        points2.append((vals2[4], vals2[5]))
    if (points3[-1][0] != vals2[6] or points3[-1][1] != vals2[7]):
        points3.append((vals2[6], vals2[7]))
    drawPoints(img, points)
    drawObj(img, points1)
    drawObj(img, points2)
    drawObj(img, points3)

    print(points1)
    print(points2)
    print(points3)
    cv.imshow("Output", img)
    cv.waitKey(1)
