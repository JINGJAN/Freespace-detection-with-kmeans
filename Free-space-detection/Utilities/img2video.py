import cv2
import os



imgarray = []
# path = "/Users/nebel/Desktop/20200611_1/20200611_1c"
path = "../RAW_data/josn_file_foto"
listofimg = os.listdir(path)
sampleimg = cv2.imread(path + "/"+ listofimg[0])

#get the w h c from sampleimage
width,height,channel = sampleimg.shape
size = (height,width)
print(width,height,channel)
out = cv2.VideoWriter("../RAW_data/Test_video/out.avi",cv2.VideoWriter_fourcc('M','J','P','G'),30,size)

#loop the image in range 1000,store the image
for i in range(399):
    imgpath = path + "/c" + str(i+1)+".jpg"
    print(imgpath)
    cv2.imshow("show",cv2.imread(imgpath))
    cv2.waitKey(10)
    out.write(cv2.imread(imgpath))
# print(len(imgarray))
out.release()