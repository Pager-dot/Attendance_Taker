from tkinter import *
from tkinter import filedialog
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\MY PC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read() )
    file.close()

window = Tk()

button =Button(text = "Open" , command = openFile)
button.pack()
window.mainloop()
