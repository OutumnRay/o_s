from tkinter import *
from tkinter import messagebox


def calculate():
    x = int(x_tf.get())
    y = x**2 - 3 + x
    messagebox.showinfo('y-pythonguides', f'Значение x = {y}')


window = Tk()
window.title('Math_Cal')
window.geometry('1080x720')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

x_lb = Label(
    frame,
    text="Введите значение x  "
)
x_lb.grid(row=3, column=1)

x_tf = Entry(
    frame,
)
x_tf.grid(row=3, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Рассчитать уравнение',
    command=calculate
)
cal_btn.grid(row=5, column=2)

window.mainloop()
