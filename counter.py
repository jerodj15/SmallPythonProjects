import tkinter as tk

counter = 0
def counter_label(label):
    counter = 0.00
    def count():
        global counter
        counter += .01
        label.config(text=str(counter))
        label.after(10,count)
    count()

root = tk.Tk()
root.title("Counter")
label = tk.Label(root, fg = "dark green")
label.pack()
counter_label(label)

button = tk.Button(root, text = "Stop", width = 40, command = root.destroy)
button.pack()
root.mainloop()
