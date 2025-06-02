from tkinter import ttk
from tkinter import * 


def Change_text():
    username = name.get()
    label.config(text=f"Hi {username}")
root = Tk()
root.title("Hello World App")

label = ttk.Label(text="Data Binaries!")
label.pack()

name = ttk.Entry(root)
name.pack()

button1 = ttk.Button(text='Click Me',command=Change_text)
button1.pack()

button = ttk.Button(text='Quit',command=root.destroy)
button.pack()
root.mainloop()