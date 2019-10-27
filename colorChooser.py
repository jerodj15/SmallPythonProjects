import tkinter
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog


a = Tk()

def mcolor():
    color = colorchooser.askcolor()
    label = Label(text = "You choosen color", bg = color[1]).pack()
def mfileopen():
    file1 = filedialog.askopenfile()
    #label = Label(text = file1).pack()
    file2 = file1.name
    f = open(file2)
    label2 = Label(text = f.read(),font =("arial", 24,"bold")).pack()
def mfilesave():
    file1 = filedialog.asksaveasfilename()
    

button = Button(text = "choose color",width = 30, command = mcolor).pack()
button = Button(text = "Open File",width = 30, command = mfileopen).pack()
button = Button(text = "Save File",width = 30, command = mfilesave).pack()

a.mainloop()
