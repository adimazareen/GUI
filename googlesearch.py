import tkinter as tk
from tkinter import ttk
import webbrowser

def perform_search():
    query = search_entry.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

# Create the main window
root = tk.Tk()
root.title("Google Search GUI")

# Create and place a label
search_label = ttk.Label(root, text="Enter search query:")
search_label.pack(pady=10)

# Create and place a text entry box
search_entry = ttk.Entry(root, width=50)
search_entry.pack(pady=5)

# Create and place a button to perform the search
search_button = ttk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=10)

# Run the application
root.mainloop()
