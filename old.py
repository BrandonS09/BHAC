import tkinter as tk
from customtkinter import CTkEntry

# Create a Tkinter window
root = tk.Tk()

# Create a CTkEntry widget
entry = CTkEntry(root)
entry.pack()

def check_entry():
    if entry.get() != "":
        print("CTkEntry has data entered")
    else:
        print("CTkEntry is empty")

# Check the entry when a button is clicked
check_button = tk.Button(root, text="Check Entry", command=check_entry)
check_button.pack()

root.mainloop()
