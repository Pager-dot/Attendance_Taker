#file = open("Demo.txt","r") 
#lines = file.readline()
#file.close()
##opening the file in the write mode by "w"
#file = open("Demo.txt","w") 
#file1 = open("second.txt","w")
#for line in lines:
#    if 'A' in line or 'a' in line :
#        file1.write(line)
#    else:
#        file.write(line)
#for line in lines:
#    if '2' in line or '02' in line :
#        file1.write(line)
#    else:
#        file.write(line)
#for line in lines:
#    if '1' in line or '01' in line :
#        file1.write(line)
#    else:
#        file.write(line)
#file.close()
#file1.close()

#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#
#my_str = '''01_Aaryan Pratap 11A1
#
#02 Aaryan Singh Chauhan 11 A-1
#
#03_Aryan Patel 11A1
#
#04.11B2_Aditya Nevatia
#
#05.11B2_Jeel Markana
#
#05_Akshat Tiwari 11B2
#
#06 Aryan Tiwari_Xl A2'''
#
## To take input from the user
##my_str = input("Enter a string: ")
#
## remove punctuation from the string
#no_punct = ""
#for char in my_str:
#   if char not in punctuations:
#       no_punct = no_punct + char
#
## display the unpunctuated string
#print(no_punct.lower())


#import string
#from tkinter import filedialog
#from typing import Text
#
#with open ('first.txt','r') as f:
#    text = f.read()
#    words = text.split()
#    table = str.maketrans("","", string.punctuation)
#    stripped = [w.translate(table) for w in words]
#    #print(stripped)
#    assembled = " ".join(stripped)
#    print(assembled.lower())
#
#with open ('first.txt','r') as file:
#    filedata = file.read()
#filedata = filedata.replace('.','_')
#filedata = filedata.replace('_',' ')
#
#with open ('first.txt','w') as file:
#    file.write(filedata)


#    
## Import the required library
#from tkinter import *
#from tkinter import ttk
#
## Create an instance of tkinter frame
#win=Tk()
#
#def get_input():
#   label.config(text=""+text.get(1.0, "end-1c"))
#
## Add a text widget
#text=Text(win)
#text.insert(END, "")
#text.pack()
#
## Create a button to get the text input
#b=ttk.Button(win, text="Print", command=get_input)
#b.pack()
#
## Create a Label widget
#label=Label(win, text="", font=('Calibri 15'))
#label.pack()
#
#win.mainloop()










# Program to make a simple
# login screen 
 
 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()