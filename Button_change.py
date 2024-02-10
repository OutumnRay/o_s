import tkinter as tk

def enter_button1(event):
    button1.config(text="Пришел")
    button2.config(text="Ушел")

def leave_button1(event):
    button1.config(text="Ушел")

def enter_button2(event):
    button1.config(text="Ушел")
    button2.config(text="Пришел")

def leave_button2(event):
    button2.config(text="Ушел")

root = tk.Tk()

button1 = tk.Button(root, text="Ушел")
button1.bind("<Enter>", enter_button1)
button1.bind("<Leave>", leave_button1)
button1.pack()

button2 = tk.Button(root, text="Ушел")
button2.bind("<Enter>", enter_button2)
button2.bind("<Leave>", leave_button2)
button2.pack()

root.mainloop()
