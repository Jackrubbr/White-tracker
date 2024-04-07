import cv2
from math import dist
from math import asin
from math import sqrt
from time import time

cv2.namedWindow("test",cv2.WINDOW_KEEPRATIO)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1920/3)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080/3)



while True:
    points = {}
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        print("failed to load")
        break
    cv2.imshow("test", gray)
    

    start = time()
    height, width, _ = frame.shape
    for y in range(height):
        for x in range(width):
            if gray[y,x] >= 254:

                x_key = x
                y_key = y

                points[(x_key,y_key)] = []
                points[(x_key,y_key)].append(x)
                points[(x_key,y_key)].append(y)
                points[(x_key,y_key)].append(x)
                points[(x_key,y_key)].append(y)
    skippoint = {}
    deletepoint = {}
    for x, y in points:
        xmin,ymin,xmax,ymax = points[(x,y)]
        if((x,y) in skippoint.keys()) or ((x,y) in deletepoint.keys()):
            continue
        skippoint[(x,y)] = []
        for xx, yy in points:

            if ((xx,yy) in skippoint.keys()) or ((xx,yy) in deletepoint.keys()):
                continue

            xmina,ymina,xmaxa,ymaxa = points[(xx,yy)]

            n=10
            if (dist((xmin,ymin),(xmina,ymina)) < n ) or (dist((xmin,ymin),(xmina,ymaxa))<n) or (dist((xmin,ymin),(xmaxa,ymina))<n) or (dist((xmin,ymin),(xmaxa,ymaxa))<n) or (dist((xmin,ymax),(xmina,ymina))<n) or (dist((xmin,ymax),(xmina,ymaxa))<n) or (dist((xmin,ymax),(xmaxa,ymina))<n) or (dist((xmin,ymax),(xmaxa,ymaxa))<n) or (dist((xmax,ymax),(xmina,ymina))<n) or (dist((xmax,ymax),(xmina,ymaxa))<n) or (dist((xmax,ymax),(xmaxa,ymina))<n) or (dist((xmax,ymax),(xmaxa,ymaxa))<n) or (dist((xmax,ymin),(xmina,ymina))<n) or (dist((xmax,ymin),(xmina,ymaxa))<n) or (dist((xmax,ymin),(xmaxa,ymina))<n) or (dist((xmax,ymin),(xmaxa,ymaxa))<n) or ((xmin,ymin)<(xmina,ymina)<(xmax,ymax)) or ((xmin,ymin)<(xmaxa,ymaxa)<(xmax,ymax)):
                xmin = min(xmin, xmina, xmax, xmaxa)
                ymin = min(ymin,ymax,ymina,ymaxa)
                xmax = max(xmin, xmina, xmax, xmaxa)
                ymax = max(ymin,ymax,ymina,ymaxa)
                deletepoint[(xx,yy)] = []
            points[(x,y)] = (xmin,ymin,xmax,ymax)

    


    for x,y in deletepoint:
        del points[(x,y)]

    deletepoint.clear()
    skippoint.clear()
    
    for x, y in points:
        xmin,ymin,xmax,ymax = points[(x,y)]
        if((x,y) in skippoint.keys()) or ((x,y) in deletepoint.keys()):
            continue
        skippoint[(x,y)] = []
        for xx, yy in points:

            if ((xx,yy) in skippoint.keys()) or ((xx,yy) in deletepoint.keys()):
                continue

            xmina,ymina,xmaxa,ymaxa = points[(xx,yy)]

            n=10
            if (dist((xmin,ymin),(xmina,ymina)) < n ) or (dist((xmin,ymin),(xmina,ymaxa))<n) or (dist((xmin,ymin),(xmaxa,ymina))<n) or (dist((xmin,ymin),(xmaxa,ymaxa))<n) or (dist((xmin,ymax),(xmina,ymina))<n) or (dist((xmin,ymax),(xmina,ymaxa))<n) or (dist((xmin,ymax),(xmaxa,ymina))<n) or (dist((xmin,ymax),(xmaxa,ymaxa))<n) or (dist((xmax,ymax),(xmina,ymina))<n) or (dist((xmax,ymax),(xmina,ymaxa))<n) or (dist((xmax,ymax),(xmaxa,ymina))<n) or (dist((xmax,ymax),(xmaxa,ymaxa))<n) or (dist((xmax,ymin),(xmina,ymina))<n) or (dist((xmax,ymin),(xmina,ymaxa))<n) or (dist((xmax,ymin),(xmaxa,ymina))<n) or (dist((xmax,ymin),(xmaxa,ymaxa))<n) or ((xmin,ymin)<(xmina,ymina)<(xmax,ymax)) or ((xmin,ymin)<(xmaxa,ymaxa)<(xmax,ymax)):
                xmin = min(xmin, xmina, xmax, xmaxa)
                ymin = min(ymin,ymax,ymina,ymaxa)
                xmax = max(xmin, xmina, xmax, xmaxa)
                ymax = max(ymin,ymax,ymina,ymaxa)
                deletepoint[(xx,yy)] = []
            points[(x,y)] = (xmin,ymin,xmax,ymax)

    for x,y in deletepoint:
        del points[(x,y)]

    for x,y in points:
        xmin,ymin,xmax,ymax = points[(x,y)]
        
        cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),3)

    cv2.imshow("test", frame)
    print(f'time: {time()-start}')

    cv2.waitKey(1)

cam.release()

cv2.destroyAllWindows()
