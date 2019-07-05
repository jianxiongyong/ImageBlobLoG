'''
Made by Yong Jian Xiong. Wanna use this program for commercial use? Email me at jianxiongyong@gmail.com first.
'''
import numpy as np
from skimage import io
from skimage.feature import blob_log
from skimage.color import rgb2gray
from math import sqrt
# above chunk just import the module you need: scikit-image, numpy, matplotlib
print("###################################################################")
print("#                                                                 #")
print("#                 Image blob detection program                    #")
print("#                    Produced by Jian Xiong                       #")
print("#                                                                 #")
print("#              for 4 AU, Pass/Fail, Send halp (´-_-`)             #")
print("#                                                                 #")
print("###################################################################\n")
print("-> This program need a 1280 X 1280 image from insight3.exe as input.")
print("-> Make sure the image is in the same folder as this .py file.")
print("-> This program will require: numpy, scikit-image to work.\n")
print("-> The output is a .csv file in: y, x coordinates of the blob in the image, divided by 5 and rounded accordingly.\n")
print("This program will loop at the end. Enter 'x' to quit.")
while True:
    filename = input("\nEnter file name (without the .png):")
    imagename = filename + ".png"
    try:
        pix = io.imread(imagename)[0:1280][0:1280]
        print("- Image found and read")
        # grab the image (must be same folder) into the .py
        image = np.array(pix, dtype=np.uint8)
        # make the image into an array
        image_gray = rgb2gray(image)
        print("- Image grayscaled")
        # grayscale the image

        # was min_sigma=0.25, overlap=0.5, threshold=1.56
        print("- Processing using LOG")
        blobs_log = blob_log(image_gray, min_sigma=0.25, overlap=0.5, threshold=1)
        print("- Array from LOG processed")
        # this is the magical algo that return an array of y, x, sigma to blobs_log

        # array is in y, x, radius
        print("- Element in array LOG:" + str(len(blobs_log)))

        print("- csv file being produced")
        blobs_log[:, 0] /= 5
        blobs_log[:, 1] /= 5
        blobs_log = np.around(blobs_log)
        np.savetxt(filename+".csv", blobs_log, delimiter=",", fmt='%.2f')
        # save a .csv file with comma separating them
        print("\n- Image processing Completed \n")
        quitCondition = input("Enter x to quit else just enter something else to loop:")
        if quitCondition == "x":
            exit(0)
    except FileNotFoundError:
        print("\n Error: File not found, Try typing it in again. \n")