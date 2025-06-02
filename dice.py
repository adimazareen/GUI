from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
import random

def dice_roll():
    num = random.randint(1,6)
    diceimg = f'{num}.png'
    output.config(text=f'Your number is {num}')
    img = Image.open(diceimg)
    img = ImageTk.PhotoImage(img)

    imgoutput.config(image=img)
    imgoutput.image=img
    

root = Tk()

root.title("Dice App")

label = Label(text="Dice App")
label.pack()

output = Label(text="Click on a roll for a number")
output.pack()

imgoutput = Label()
imgoutput.pack()

button = Button(text="Roll",command=dice_roll)
button.pack()

root.mainloop()