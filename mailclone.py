import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_email():
    sender_email = entry_sender.get()
    receiver_email = entry_receiver.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)

    if not sender_email or not receiver_email or not subject or not body.strip():
        messagebox.showwarning("Warning", "All fields must be filled in.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, entry_password.get())
            server.send_message(msg)

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Mail Clone")

#fvfn emks vnar klzx
# Create and place widgets
tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=10)
entry_sender = tk.Entry(root, width=50)
entry_sender.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*', width=50)
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Receiver Email:").grid(row=2, column=0, padx=10, pady=10)
entry_receiver = tk.Entry(root, width=50)
entry_receiver.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=10)
entry_subject = tk.Entry(root, width=50)
entry_subject.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Body:").grid(row=4, column=0, padx=10, pady=10)
text_body = tk.Text(root, width=50, height=10)
text_body.grid(row=4, column=1, padx=10, pady=10)

btn_send = tk.Button(root, text="Send Email", command=send_email)
btn_send.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
