from tkinter import ttk
from tkinter import * 
import wikipedia

def wikisearch():
    data = query.get()
    print(data)
    try:
        summary = wikipedia.summary(data,sentences=2)
        output.delete(2.0,END)
        output.insert(1.0,summary)
    except Exception as e:
        output.delete(2.0,END)
        output.insert(1.0,e)
        

root = Tk()

root.title("wikipedia Search App")

label = ttk.Label(text="wikipedia Search App")
label.pack()

query = ttk.Entry(root)
query.pack()

output = Text(root, height=10, width=50, wrap=WORD)
output.pack()

button1 = ttk.Button(text='Search',command=wikisearch)
button1.pack()

button = ttk.Button(text='Quit',command=root.destroy)
button.pack()

root.mainloop()