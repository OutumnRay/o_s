import tkinter as tk
import random

def change_color(event):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    root.configure(bg=color)

root = tk.Tk()
root.geometry("300x300")
root.bind("<Motion>", change_color)
root.mainloop()
