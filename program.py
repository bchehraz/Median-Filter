# github.com/bchehraz

# Title: Median Filter (Project 1)
# Author: Babak Chehraz
# Abstract: This program takes images
# and outputs a median image

from PIL import Image
import glob, os

#Load 9 images into array of images
images = []
for i in range(1,10):
    #images.append(Image.open("Project1Images/" + str(i) + ".png"))
    images.append(Image.open("BIT_photos_by_Josh_Kling/" + str(i) + ".png").convert('RGB'))
#Load red, green, and blue pixel values
rPixels = []
gPixels = []
bPixels = []
for i in range(0,9):    
    rPixels.append([])
    gPixels.append([])
    bPixels.append([])

#loop through and store all r, g, and b pixels
width,height = images[i].size
for i in range(0,9):
    for x in range(0,width):
        for y in range(0,height):
            
            r,g,b = images[i].getpixel((x,y))
            
            rPixels[i].append(r)
            gPixels[i].append(g)
            bPixels[i].append(b)

#function to get median in a list
#the return value of a sorted() function will be passed in
def median(inList):
    size = len(inList)

    inList = sorted(inList)

    if size % 2 == 0: 
        midIndex = size / 2
    else:
        midIndex = ((size + 1)/2)-1
    return inList[midIndex]

#these first 3 arrays will be responsible for holding all r g b values for each image and get the median
pixelsR = []
pixelsG = []
pixelsB = []
#matrix
medianR = [[0 for y in range(height)] for x in range(width)]
medianG = [[0 for y in range(height)] for x in range(width)]
medianB = [[0 for y in range(height)] for x in range(width)]

newImage = Image.new("RGB", (width,height))
k = 0
for x in range(0,width):
    for y in range(0,height):
        for i in range(0,9): #Take median of every pixel in order
            
            pixelsR.append(rPixels[i][k])
            pixelsG.append(gPixels[i][k])
            pixelsB.append(bPixels[i][k])
        #store the output of the median function to get the rgb values needed
        newImage.putpixel((x,y),(int(round(median(pixelsR))), int(round(median(pixelsG))), int(round(median(pixelsB)))))
        del pixelsR[:]
        del pixelsG[:]
        del pixelsB[:]
        k += 1

#save image
newImage.save("output.png")

#take out the trash. Necessary?
for i in range(0,9):
    rPixels[i][:] = []
    gPixels[i][:] = []
    bPixels[i][:] = []
rPixels[:] = []
gPixels[:] = []
bPixels[:] = []
medianR[:] = []
medianG[:] = []
medianB[:] = []
