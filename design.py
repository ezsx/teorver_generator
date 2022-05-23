from tkinter import *
from tkinter import filedialog as filedialog, ttk
from tkinter import messagebox as mb
import tkinter.font as tkFont

import main_logic
import arr_generate
import write_docx
import re

def darkstyle(root):
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style

def clicked():
    regex = r"([0-9]{1,2},)|([0-9]{1,2}-[0-9]{1,2},)"
    ss = tasks.get()

    if ss[-1] != ',':
        ss = ss+','
    result = re.sub(regex, "", ss, 0, re.MULTILINE)

    if result:
        m=mb.askokcancel(title="Ошибка", message=("Строка не распознана"))
        return

    if path.get() == "":
        path.insert(0, filedialog.askdirectory())

    tsk = arr_generate.F(tasks.get())
    var = variants.get()
    write_docx.F(tsk, int(var), path.get(),uniq_var.get())
    mb.showinfo(message="успешно")


window = Tk()
window.title("Генератор вариантов")
window.geometry('490x200')
window.maxsize(490, 200)
window.minsize(490, 200)
style = darkstyle(window)

fontEx = tkFont.Font(family="google sans", size=12, weight="bold", slant="italic")
fontEx1 = tkFont.Font(family="google sans", size=12, weight="normal", slant="roman")


lbl1 = Label(window, text="Доступные варианты", font=fontEx)
lbl1.grid(column=0, row=0, pady=8, padx=5)

lbl1 = Label(window, text="Задания", font=fontEx)
lbl1.grid(column=0, row=1, pady=8, padx=5)

lbl2 = Label(window, text="Количество вариантов", font=fontEx)
lbl2.grid(column=0, row=2, pady=8, padx=5)

lbl3 = Label(window, text="Путь к результату", font=fontEx)
lbl3.grid(column=0, row=3, pady=8, padx=5)


uniq_var = Entry(window, width=30, font=fontEx1)
uniq_var.grid(column=1, row=0,)
uniq_var.insert(1,'v4,v5')

tasks = Entry(window, width=30, font=fontEx1)
tasks.grid(column=1, row=1,)


variants = Entry(window, width=30, font=fontEx1)
variants.grid(column=1, row=2)

path = Entry(window, width=30, font=fontEx1)
path.grid(column=1, row=3)

generate = Button(window, text="сгенерировать", font=fontEx, command=clicked)
generate.grid(column=1, row=4)

window.mainloop()