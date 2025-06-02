import tkinter as tk

# Function to update the expression in the entry widget
def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.pack()
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place the buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, width=4, height=2, command=clear_entry)
    elif button == '=':
        btn = tk.Button(root, text=button, width=4, height=2, command=evaluate_expression)
    else:
        btn = tk.Button(root, text=button, width=4, height=2, command=lambda b=button: click_button(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
