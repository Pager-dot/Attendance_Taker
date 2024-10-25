from tkinter import *
import os
main_window = Tk()

fopener = open("fname.txt" , 'r')
Label(main_window, text = " Enter full roll no ").grid(row = 0, column = 1)

#text input
Input_text =Entry(main_window, width = 50, borderwidth= 5)
Input_text.grid(row = 1, column = 1)
def Apply():
    roll = (f"{Input_text.get()} ")
    for line in fopener :
        if line.startswith(roll) == True:
            Label(main_window, text = line).grid(row = 2, column = 3)
            Label(main_window, text = "This student was present").grid(row = 3, column = 3)
            Label(main_window, text = "Thank you").grid(row = 4, column = 3)
            break
    else:
        Label(main_window, text = "This student was absent or you enter wrong input").grid(row = 5, column = 3)
def refresh():
    main_window.destroy()
    os.popen("GUI for shaarav.py")
Button(main_window, text="refresh", command = refresh ).grid(row = 221,column =3)




#button 
Button(main_window, text="Apply", command = Apply ).grid(row = 221,column =1)


main_window.mainloop()





#    print(f"you Entered {Input_text.get()} ")
