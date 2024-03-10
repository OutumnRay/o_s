import threading
import time
import tkinter as tk

def thread_function(thread_name, result_label):
    for i in range(1, 11):
        time.sleep(1)
        result_label.config(text=f'{thread_name}: {i}')
    result_label.config(text=f'{thread_name} завершил выполнение.')

def main():
    root = tk.Tk()
    root.title("Пример работы с потоками")

    label1 = tk.Label(root, text="Поток 1:")
    label1.pack()

    result_label1 = tk.Label(root, text="")
    result_label1.pack()

    label2 = tk.Label(root, text="Поток 2:")
    label2.pack()

    result_label2 = tk.Label(root, text="")
    result_label2.pack()

    thread1 = threading.Thread(target=thread_function, args=("Поток 1", result_label1))
    thread2 = threading.Thread(target=thread_function, args=("Поток 2", result_label2))

    thread1.start()
    thread2.start()

    root.mainloop()

if __name__ == "__main__":
    main()