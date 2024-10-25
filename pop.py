#import cv2
#
#import numpy as np
#import pytesseract as tess
#tess.pytesseract.tesseract_cmd = r'C:\Users\MY PC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#from PIL import Image
#
#
#if __name__ == '__main__' :
#
#   # Read image
#   im = cv2.imread("popsjp[.png")
#
#   # Select ROI
#
#   r = cv2.selectROI(im)
#
#
#
#   # Crop image
#
#   imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
#
#
#
#   # Display cropped image
#
#   cv2.imshow("Image", imCrop)
#
#   text = tess.image_to_string(imCrop)
#
# 
# 
#   print(text)
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
img = ImageTk(Image.open("03.png"))
panel = Label(root, image = img)
panel.grid()
root.mainloop()