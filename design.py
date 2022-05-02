from tkinter import *

import arr_generate
import write_docx


def clicked():
    tsk = arr_generate.F(tasks.get())
    var = variants.get()
    write_docx.F(tsk,int(var))



window = Tk()
window.title("teorver_generator")
window.geometry('400x250')

lbl1 = Label(window, text="Задания")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Количество вариантов")
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="Путь к результату")
lbl3.grid(column=0, row=2)

tasks = Entry(window, width=30)
tasks.grid(column=1, row=0)

variants = Entry(window, width=30)
variants.grid(column=1, row=1)

path = Entry(window, width=30)
path.grid(column=1, row=2)

generate = Button(window, text="сгенерировать", command=clicked)
generate.grid(column=1, row=3)
window.mainloop()