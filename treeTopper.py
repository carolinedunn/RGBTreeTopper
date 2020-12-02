#!/usr/bin/env python3
import time
import sys
import board
import neopixel
from PIL import Image

pixel_pin = board.D21
num_pixels = 256
display_width = 32
display_height = 8
matrixbrightness = 0.4
pauseTime = 0.2 # amount of time to pause between displaying images -> smaller number=faster

ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=matrixbrightness, auto_write=False, pixel_order=ORDER)
rotation = 0

#This maps pixel coordinates from the image to the NeoPixel
def getIndex2(x, y):
    x = display_width-x-1
    if x % 2 != 0:
        return (x*8)+y
    else:
        return (x*8)+(7-y)
        
#create an array with the open images
image_list = []
j=1
while j<11:
    im = Image.open('/home/pi/RGBTreeTopper/fire/{}.jpg'.format(j)) #Open images 1-10.jpg in the 'fire' folder
    image_list.append(im)
    j+=1

while True:
    for i in image_list: #for each image in the "fire" folder
        for x in range(display_width): #go through each pixel in the image
            for y in range(display_height):
                color = i.getpixel((x, y)) #get the color by coordinate
                pixels[getIndex2(x,y)] = color #map the image pixel to the matrix coordinate                                      
        pixels.show() #display image
        time.sleep(pauseTime) #pause before displaying the next image
    
