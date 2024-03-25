import tkinter as tk
import ctypes


def my_function():
    print("Функция в библиотеке была вызвана!")


def perform_action():
    print("Действие выполняется!")

    lib = ctypes.CDLL("./library.dll")
    lib.my_function.restype = None
    lib.my_function.argtypes = []
    lib.my_function()


root = tk.Tk()
root.title("DLL Library with GUI")

btn = tk.Button(root, text="Выполнить действие", command=perform_action)
btn.pack()

root.mainloop()


# python -m tkinter f2py -c -m library library_with_gui.py
