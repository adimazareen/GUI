import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        # Initialize variables
        self.time_left = 0
        self.running = False
        self.update_interval = 1000  # 1 second

        # Create and place widgets
        self.label = tk.Label(root, font=('calibri', 40, 'bold'))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=('calibri', 20, 'bold'), width=10)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=('calibri', 14))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, font=('calibri', 14))
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, font=('calibri', 14))
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                self.time_left -= 1
                self.display_time(self.time_left)
                self.root.after(self.update_interval, self.update_timer)
            else:
                messagebox.showinfo("Time's up!", "The timer has finished.")
                self.running = False

    def display_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.label.config(text=time_str)

    def start_timer(self):
        try:
            minutes = int(self.entry.get())
            self.time_left = minutes * 60
            self.running = True
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.display_time(self.time_left)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
