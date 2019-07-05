'''
Made by Yong Jian Xiong. Wanna use this program for commercial use? Email me at jianxiongyong@gmail.com first.
'''
# import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.feature import blob_log
from skimage.color import rgb2gray
from math import sqrt
# above chunk just import the module you need: scikit-image, numpy, matplotlib
print("###################################################################")
print("#                                                                 #")
print("#                 Image blob detection program V2                 #")
print("#                    Produced by Jian Xiong                       #")
print("#                                                                 #")
print("#                     Now with a Queue! ʕ •ᴥ•ʔ                    #")
print("#                                                                 #")
print("###################################################################\n")
print("-> This program need a 1280 X 1280 image from insight3.exe as input.")
print("-> Make sure the image is in the same folder as this .py file.")
print("-> Enter the name of the images without the .png, but same name will be ignored by the queue AKA no repetition.")
print("-> This program will require: numpy, scikit-image to work.\n")
print("-> The output is a .csv file with y, x coordinates of the blob in the image, divided by 5 and rounded accordingly.\n")


class Queue:

    # Constructor creates a list
    def __init__(self):
        self.queue = list()

    # Adding elements to queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    # Removing the last element from the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Queue Empty!"

    # Getting the size of the queue
    def size(self):
        return len(self.queue)

    # printing the elements of the queue
    def printQueue(self):
        return self.queue


queue = Queue()
queueSize = queue.size()

filename = input("\nEnter file name (without the .png, type x if all file have been entered):")
while filename != 'x':
    queue.enqueue(filename)
    queueSize = queue.size()
    print("Size of queue: %i" % queueSize)
    filename = input("\nEnter file name (without the .png, type x if all file have been entered):")

print("- Queue processing started...")
filename = queue.dequeue()
while queueSize != 0:
    imagename = filename + ".png"
    queueSize = queue.size()
    print("- Dequeuing from queue, %i element(s) left" % queueSize)
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

        '''
        This is for debug, it'll draw a red circle
        for i in range(len(blobs_log)):
            plt.scatter(blobs_log[i][1], blobs_log[i][0], c='r', s=1)
            # this draw red dots on the image for us to check
    
        plt.imshow(pix)
        # add image to plot so the graph is not just red dots
        plt.show()
        # show image
        '''
        print("- csv file being produced")
        blobs_log[:, 0] /= 5
        blobs_log[:, 1] /= 5
        blobs_log = np.around(blobs_log)
        np.savetxt(filename+".csv", blobs_log, delimiter=",", fmt='%.2f')
        # save a .csv file with comma separating them
        print("\n- Image processing Completed \n")

    except FileNotFoundError:
        print("\n Error: File not found, skipping to next in queue. \n")
    filename = queue.dequeue()
else:
    quitCondition = input("All images in Queue processed! Press enter to quit! BYE! ʕ •ᴥ•ʔ")
    exit(0)
