
import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

# Function to check login
def login():
    username = entry_user.get()
    password = entry_pass.get()

    # Dummy credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Title
title = tk.Label(root, text="Login System", font=("Arial", 16))
title.pack(pady=10)

# Username
label_user = tk.Label(root, text="Username")
label_user.pack()
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

# Password
label_pass = tk.Label(root, text="Password")
label_pass.pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

# Login button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=10)

# Run app
root.mainloop()