import tkinter as tk
from tkinter import messagebox
import os


def schedule_shutdown():
    time = entry.get().strip()
    if not time:
        messagebox.showerror("Error", "Time is empty.")
        return
    if not time.isdigit():
        messagebox.showerror("Error", "Just numbers allowed.")
        return
    minutes = int(time)
    if minutes <= 0:
        messagebox.showerror("Error", "Time must be greater than 0.")
        return

    seconds = minutes * 60
    os.system(f"shutdown /s /t {seconds}")
    messagebox.showerror(
        "Set up", f"Your computer will Shut Down on {minutes} minutes.")


def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showerror("Cancel", "Shut Down will not happend.")


root = tk.Tk()
root.title("Shut Down")
root.geometry("300x200")

label = tk.Label(root, text="Time on minutes:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_set = tk.Button(root, text="Shut Down", command=schedule_shutdown)
btn_set.pack(pady=5)

btn_cancel = tk.Button(root, text="Cancel Action", command=cancel_shutdown)
btn_cancel.pack(pady=5)

root.mainloop()
