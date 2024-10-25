from tkinter import *
from tkinter import filedialog
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\MY PC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

main_window = Tk()








#background image
bg = PhotoImage(file = "CS project\pop.jpg")
bg_lable = Label(main_window, image=bg)
bg_lable.place(x=0, y=0, relheight=1, relwidth=1)
