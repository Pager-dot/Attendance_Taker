from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import cv2
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = \
r'C:\Users\MY PC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

main_window = Tk()
main_window.geometry("350x398")
notebook = ttk.Notebook(main_window)
Window_title = "Image Extractor and Text Compiler"
main_window.title(Window_title)

#Tabs
tab1 = Frame(notebook)
tab2 = Frame(notebook,bg="#0191c8")
tab3 = Frame(notebook,bg="#0191c8")
notebook.add(tab1, text="Extraction")
notebook.add(tab2, text="Search")
notebook.add(tab3, text="Text File")
notebook.grid()

# BG for tab1
tab1_BG = Image.open('may.png')
render = ImageTk.PhotoImage(tab1_BG)
img09 = Label(tab1 , image= render)
img09.place(x = -2,y = -2)

#labels
# select the file(guidlines)
Label(tab1, text = "Select the file: ", fg = "white" \
    ,bg="#0191c8").grid(row = 1, column = 0)
Label(tab1, text = "jpeg,jpg,png only accepted",\
     fg="white" ,bg="#0191c8").grid(row = 2, column = 0)
Label(tab1, text = "This program make the user\
choose the image to crop",\
fg="white" ,bg="#0191c8").grid(row = 3, column = 0)

#image input
# tell the user to only select the jpeg or png file
def openFile():
    filepath = filedialog.askopenfilename()
    config = \
    ('-c preserve_interword_spaces=1 -l eng --oem 1 --psm 3')
    im = cv2.imread(filepath)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Select ROI 
    r = cv2.selectROI(im)
# Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3])\
        , int(r[0]):int(r[0]+r[2])]
# Display cropped image
    cv2.imshow("Enter any key to Exit", imCrop)
    text = tess.image_to_string(imCrop, \
        config=config)
    fh = open('Demo.txt', 'w')
    fh.write(text.strip())
    fh.close()
    
##jeremey
# for refining raw data
    with open ('Demo.txt','r') as file:
        filedata = file.read()
    filedata = filedata.replace('.','_')
    filedata = filedata.replace('_',' ')
    filedata = filedata.replace('X!','11')
    filedata = filedata.replace('Xl','11')
    filedata = filedata.replace('XI','11')
    filedata = filedata.replace('O1','01')
    filedata = filedata.replace('82','B2')
    filedata = filedata.replace('1141','11A1')
    filedata = filedata.replace('11 A-1','11A1')
    filedata = filedata.replace('11 A2','11A2')
    filedata = filedata.replace('11th A2','11A2')
    filedata = filedata.replace('11th AZ','11A2')
    filedata = filedata.replace('11-A2','11A2')
    filedata = filedata.replace('Xl A2','11A2')
    filedata = filedata.replace('XI A2','11A2')
    filedata = filedata.replace('1142','11A2')
    filedata = filedata.replace('XI A2','11A2')
    filedata = filedata.replace('11 AZ','11A2')
    filedata = filedata.replace('X A2','11A2')
    filedata = filedata.replace('11thA2','11A2')
    filedata = filedata.replace('11A 2','11A2')
    filedata = filedata.replace('114 2','11A2')
    filedata = filedata.replace('X A2','11A2')
    filedata = filedata.replace('X\ A2','11A2')
    filedata = filedata.replace('(me)',' ')
    filedata = filedata.replace('(Host)',' ')
    filedata = filedata.replace('|','')
    filedata = filedata.replace('‘','')
    with open ('Demo.txt','w') as file:
        file.write(filedata.lower())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read image
button =Button(tab1,text = "Open" , command = openFile)
button.grid(row = 10, column = 10 ,pady= 100, padx= 10)

##shaarav
#Seach tab 
fopener = open("Demo.txt" , 'r')
Label(tab2, text = " Enter full roll\
 no ",fg = "white",bg="#0191c8" ).grid(row = 0, column = 1)

#text input
Input_text = StringVar()
Input_text =Entry(tab2) 
Input_text.grid(row = 1, column = 2)

# take the user input as roll no and seacrh in file
def Apply():
    roll = Input_text.get()
    for line in fopener :
        if line.startswith(roll) == True:
            Label(tab2, text = line ,fg = "white"\
            ,bg="#0191c8").grid(row = 22, column = 2)
            Label(tab2, text = "This student was\
 present",fg = "white",\
            bg="#0191c8").grid(row = 23, column = 2)
            Label(tab2, text = "Thank\
 you", fg = "white"\
            ,bg="#0191c8").grid(row = 24, column = 2)
            break
        END
    else:
        Label(tab2, text = "Student was\
 absent or you enter wrong input",fg = "white"\
        ,bg="#0191c8").grid(row = 25, column = 2)

Button(tab2, text="Apply",\
command = Apply).grid(row = 10,column =2)

#text output on text file tab
txtarea = Text(tab3, width=40, height=20)
Label(tab3 , text= 'Scroll to see the complete \
paticipants list:',fg = "white",\
bg="#0191c8").grid(row = 0, column = 0)
txtarea.grid()

# show the output
def out_put():
    opened_file = open('Demo.txt')
    file_cont = opened_file.read()
    txtarea.insert(END, file_cont)
    opened_file.close()
out_put()

# To refresh the entire program
def refresh():
    main_window.destroy()
    os.popen("Project.py")
Button(main_window, text="refresh", command = refresh\
 , width= 20, height= 0).grid(row = 1,column =0)

main_window.mainloop()