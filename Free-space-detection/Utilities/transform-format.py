import cv2
import os

path = "/Users/nebel/Desktop/Two-Categories"
dir_file = os.listdir(path)
print(dir_file)

#transform the data into mnist(28,28) maxmalsize
for i ,n in enumerate(dir_file):

    if(n!=".DS_Store"):
        path_img = path + "/" + n
        dir_img = os.listdir(path_img)
        # print(dir_img)
        for d in dir_img:

            if (d != ".DS_Store"):
                img = cv2.imread(path_img + "/" + d)
                # print(path_img + "/" + d)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img, (28, 28))
                # print(img.shape)
                cv2.imwrite(path_img + "/" + d, img)
