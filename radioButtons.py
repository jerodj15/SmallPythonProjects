from tkinter import *
root = Tk()
root.title("radio buttons")

"""Radiobutton(root,text="radio1", pady = 40).pack()
Radiobutton(root,text="radio2", padx = 40).pack()
Radiobutton(root,text="radio3", padx = 40).pack()
Radiobutton(root,text="radio4", padx = 40).pack()
"""
def mmm():
    a = v.get()
    if (a == 1):
        a1 = Tk()
        a1.title("Python")
        l1 = Label(a1, text = "Welcome to Python Programming", font=("arial", 20, "italic"))
        l1.pack()
    elif(a == 2):
        a1 = Tk()
        a1.title("Perl")
        l1=Label(a1, text = "Welcome to Perl Programming", font=("arial",20,"italic"))
        l1.pack()
    elif(a==3):
        a1 = Tk()
        a1.title("C Language")
        l1=Label(a1, text = "Welcome to C Language Programming", font=("arial", 20, "italic"))
        l1.pack()
    elif(a==4):
        a1 = Tk()
        a1.title("C Language")
        l1=Label(a1, text = "Welcome to Ruby Programming", font=("arial", 20, "italic"))
        l1.pack()



v = IntVar()
v.set(3)
languages = [("Python",1),("Perl",2),("C Language", 3), ("Ruby",4)]
Label(root, text = "Choose a Programming \nLanguage", padx = 25, justify = LEFT).pack(anchor = "w")
#Radiobutton(root, text = "Python", padx = 25, variable = v, value = 1, command = mmm).pack(anchor = "w")
#Radiobutton(root, text = "Perl", padx = 25, variable = v, value = 2,command = mmm).pack(anchor = "w")
#Radiobutton(root, text = "C Language", padx = 25, variable = v, value = 3,command = mmm).pack(anchor = "w")
#Radiobutton(root, text = "Ruby", padx = 25, variable = v, value = 4,command = mmm).pack(anchor = "w")
for txt, val in languages:
    Radiobutton(root,text = txt, padx = 25,indicator=0,width = 25, variable = v, command = mmm, value = val).pack(anchor = "w")

root.mainloop()
