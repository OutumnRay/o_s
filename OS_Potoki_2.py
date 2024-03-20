import threading
import time
import tkinter as tk


def thread_with_priority():
    for i in range(5):
        time.sleep(1)
        result = f'Приоритетный поток: итерация {i + 1}'
        update_gui(result)


def normal_thread():
    for i in range(5):
        time.sleep(2)
        result = f'Обычный поток: итерация {i + 1}'
        update_gui(result)


def update_gui(result):
    label.config(text=label.cget("text") + '\n' + result)


root = tk.Tk()
root.title("Пример работы двух потоков с приоритетом")

label = tk.Label(root, text="")
label.pack()

thread1 = threading.Thread(target=thread_with_priority)
thread2 = threading.Thread(target=normal_thread)

thread1.start()
thread2.start()

root.mainloop()