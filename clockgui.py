import tkinter as tk
from time import strftime

# Function to update the time
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update the time every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the background color and size
root.configure(bg='black')
root.geometry("250x100")

# Create and place the time label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Initialize the time update
update_time()

# Run the application
root.mainloop()
