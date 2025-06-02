import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark the selected task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, task + " (Completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create and place the entry widget
entry_task = tk.Entry(root, width=40)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Create and place the buttons
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.grid(row=0, column=1, padx=10, pady=10)

btn_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete_task.grid(row=1, column=0, padx=10, pady=10)

btn_mark_completed = tk.Button(root, text="Mark as Completed", command=mark_completed)
btn_mark_completed.grid(row=1, column=1, padx=10, pady=10)

# Create and place the listbox widget
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
