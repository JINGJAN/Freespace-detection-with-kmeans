import cv2 as cv
import os
from kmeans import kemeans_roi
from Network import getimgfromjson
import time

# without this line the programme can't run in mac
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Two categries
cap = cv.VideoCapture("../RAW_data/Test_video/out.avi")

# get width and height
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# creat video out object
out = cv.VideoWriter('../RAW_data/demo/demo_video.avi',
                     cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# ten frames remove noise
frequency = 20

# create mask
freespacerange = []
empty_out = []
full_out = []

if(cap.isOpened()==False):
    print("can not read video")

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

        #computer time
        start = time.time()

        if(frequency == 20):

            # midfreespace
            freespacerange = kemeans_roi(frame)

            #free space with line
            empty_out,full_out = getimgfromjson(frame)

            #reset frequency
            frequency = 0
        else:
            frequency += 1

        #draw freespace
        for i in range(len(freespacerange)):
            range_left = freespacerange[i][0]
            range_right = freespacerange[i][1]

            #figure out area of freespace
            motor = int((range_right - range_left)/20)
            car = int((range_right - range_left)/50)
            cv.putText(frame, "Parking space at " + str((range_left,290)) + " Area is : "+ str(range_right - range_left) + " engouh for " + str(motor) + " Motorcycle " + str(car)+ " Car", (0, 580 +i*10), cv.FONT_HERSHEY_SIMPLEX, 0.4,
                        (0, 255, 255), 1)

            #draw the freespace
            frame[285:320, range_left:range_right,1] = 255
            frame[285:320, range_left:range_right, 0] = 0
            frame[285:320, range_left:range_right, 2] = 0

        for i in range(len(empty_out)):
            cv.polylines(frame, [empty_out[i]], True, (0, 255, 0))
        for i in range(len(full_out)):
            cv.polylines(frame, [full_out[i]], True, (0, 0, 255))

        #put text in image
        cv.putText(frame,"Parking_space_with_line: "+str(len(empty_out)),(1050,580),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

        #endtime
        end = time.time()
        print("used:",end-start)

        cv.imshow("frame", frame)
        cv.waitKey(25)
        out.write(frame)

    # Break the loop
    else:
        break
