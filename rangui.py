import tkinter as tk
from tkinter import ttk
import random

def generate_random_number():
    random_number = random.randint(1, 100)
    result_label.config(text=f"Generated Number: {random_number}")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create and place a button to generate a random number
generate_button = ttk.Button(root, text="Generate Random Number", command=generate_random_number)
generate_button.pack(pady=10)

# Create and place a label to display the result
result_label = ttk.Label(root, text="Generated Number: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()

