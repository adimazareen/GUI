import tkinter as tk
from tkinter import ttk, messagebox

# Helper functions
def convert_number():
    try:
        number = entry_input.get()
        base = combo_base.get()

        if base == "Binary":
            decimal = int(number, 2)
        elif base == "Octal":
            decimal = int(number, 8)
        elif base == "Decimal":
            decimal = int(number, 10)
        elif base == "Hexadecimal":
            decimal = int(number, 16)
        else:
            raise ValueError("Invalid base selected")

        label_bin.config(text=f"Binary: {bin(decimal)[2:]}")
        label_oct.config(text=f"Octal: {oct(decimal)[2:]}")
        label_dec.config(text=f"Decimal: {decimal}")
        label_hex.config(text=f"Hexadecimal: {hex(decimal)[2:].upper()}")
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

def calculate():
    try:
        num1 = entry_num1.get()
        num2 = entry_num2.get()
        base = combo_op_base.get()
        op = combo_op.get()

        if base == "Binary":
            n1 = int(num1, 2)
            n2 = int(num2, 2)
        elif base == "Octal":
            n1 = int(num1, 8)
            n2 = int(num2, 8)
        elif base == "Decimal":
            n1 = int(num1, 10)
            n2 = int(num2, 10)
        elif base == "Hexadecimal":
            n1 = int(num1, 16)
            n2 = int(num2, 16)
        else:
            raise ValueError("Invalid base selected")

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            if n2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = n1 // n2
        else:
            raise ValueError("Invalid operation")

        label_res_bin.config(text=f"Binary: {bin(result)[2:]}")
        label_res_oct.config(text=f"Octal: {oct(result)[2:]}")
        label_res_dec.config(text=f"Decimal: {result}")
        label_res_hex.config(text=f"Hexadecimal: {hex(result)[2:].upper()}")

    except Exception as e:
        messagebox.showerror("Calculation Error", str(e))

# GUI
root = tk.Tk()
root.title("Digital Electronics Calculator")
root.geometry("500x600")
root.resizable(False, False)

# Title
tk.Label(root, text="Digital Electronics Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Conversion Section
frame_convert = tk.LabelFrame(root, text="Number System Converter", padx=10, pady=10)
frame_convert.pack(padx=10, pady=10, fill="x")

tk.Label(frame_convert, text="Enter Number:").grid(row=0, column=0, sticky="w")
entry_input = tk.Entry(frame_convert, width=30)
entry_input.grid(row=0, column=1, padx=5)

tk.Label(frame_convert, text="Select Base:").grid(row=1, column=0, sticky="w")
combo_base = ttk.Combobox(frame_convert, values=["Binary", "Octal", "Decimal", "Hexadecimal"], state="readonly")
combo_base.grid(row=1, column=1, padx=5)
combo_base.current(2)

tk.Button(frame_convert, text="Convert", command=convert_number).grid(row=2, column=0, columnspan=2, pady=5)

label_bin = tk.Label(frame_convert, text="Binary: ")
label_oct = tk.Label(frame_convert, text="Octal: ")
label_dec = tk.Label(frame_convert, text="Decimal: ")
label_hex = tk.Label(frame_convert, text="Hexadecimal: ")

label_bin.grid(row=3, column=0, columnspan=2, sticky="w")
label_oct.grid(row=4, column=0, columnspan=2, sticky="w")
label_dec.grid(row=5, column=0, columnspan=2, sticky="w")
label_hex.grid(row=6, column=0, columnspan=2, sticky="w")

# Arithmetic Section
frame_calc = tk.LabelFrame(root, text="Arithmetic Operations", padx=10, pady=10)
frame_calc.pack(padx=10, pady=10, fill="x")

tk.Label(frame_calc, text="Number 1:").grid(row=0, column=0, sticky="w")
entry_num1 = tk.Entry(frame_calc, width=20)
entry_num1.grid(row=0, column=1)

tk.Label(frame_calc, text="Number 2:").grid(row=1, column=0, sticky="w")
entry_num2 = tk.Entry(frame_calc, width=20)
entry_num2.grid(row=1, column=1)

tk.Label(frame_calc, text="Select Base:").grid(row=2, column=0, sticky="w")
combo_op_base = ttk.Combobox(frame_calc, values=["Binary", "Octal", "Decimal", "Hexadecimal"], state="readonly")
combo_op_base.grid(row=2, column=1)
combo_op_base.current(2)

tk.Label(frame_calc, text="Operation:").grid(row=3, column=0, sticky="w")
combo_op = ttk.Combobox(frame_calc, values=["+", "-", "*", "/"], state="readonly", width=5)
combo_op.grid(row=3, column=1, sticky="w")
combo_op.current(0)

tk.Button(frame_calc, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2, pady=5)

label_res_bin = tk.Label(frame_calc, text="Binary: ")
label_res_oct = tk.Label(frame_calc, text="Octal: ")
label_res_dec = tk.Label(frame_calc, text="Decimal: ")
label_res_hex = tk.Label(frame_calc, text="Hexadecimal: ")

label_res_bin.grid(row=5, column=0, columnspan=2, sticky="w")
label_res_oct.grid(row=6, column=0, columnspan=2, sticky="w")
label_res_dec.grid(row=7, column=0, columnspan=2, sticky="w")
label_res_hex.grid(row=8, column=0, columnspan=2, sticky="w")

# Run App
root.mainloop()
