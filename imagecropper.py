#!/usr/bin/python

# ImageCropper 1.0
# (c) Tony K. Tan
# ImageCropper may be freely distributed under the MIT license.

# Script crops all images in a directory into squares, regardless of initial size
# Version 1.0 crops to the center of the picture
# To run script, fill in path to folder and then run "python imagecropper.py" in Terminal

import os, sys
from PIL import Image

def process(filename):
  def centercrop(image):
    width, height = image.size

    if width < height: 
      new_width = width 
    else: 
      new_width = height

    left = (width - new_width) / 2
    top = (height - new_width) / 2
    right = (width + new_width) / 2
    bottom = (height + new_width) / 2

    img = image.crop((left, top, right, bottom))
    return img
  try:
    im = Image.open(filename)
    im = centercrop(im)
    im.save(filename)
    print "cropped", filename
  except IOError:
    pass

path = "***/path/foldername***" #replace this with path and foldername
dirs = os.listdir(path)

for file in dirs:
  process(path + "/" + file)

## TEST FUNCTION - WORKED GREAT ##
# filename = "***/path/filename***" #replace this with path and filename
# process(filename)