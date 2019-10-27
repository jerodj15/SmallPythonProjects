from tkinter import *

def mcal():
    var2 = var1.get()
    var3 = var2 * 3.785
    e2.delete(0, END)
    e2.insert(0, var3)

a = Tk()
var1 = IntVar()

n = "arial",14,"italic"
Label(a, text = "Gallons", padx = 25,font = (n)).grid(row = 0, sticky = "w")
e1 = Entry(a, width = 25, font = (n), textvariable = var1)
e1.grid(row = 0, column = 1)
Label(a, text = "Liters", padx = 25,font = (n)).grid(row = 1, sticky = "w")
e2 = Entry(a, width = 25, font = (n))
e2.grid(row = 1, column = 1)
Button(a, text = "Calculate", padx = 25, font = (n), command = mcal).grid(row = 2, column = 1)

a.mainloop()
