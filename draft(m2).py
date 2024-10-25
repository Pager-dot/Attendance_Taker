from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog

window = Tk()
window.title("Crop the selected image")

window.filename = filedialog.askopenfilename(initialdir="\CS project", title="select a file")
label1 = Label(window, text = window.filename).pack()
img = ImageTk.PhotoImage(Image.open(window.filename))
label_img_2 = label1(image = img)



window.mainloop()