from tkinter import *
from tkinter import filedialog as filedialog
from tkinter import messagebox as mb

import arr_generate
import write_docx
import re
# You can manually specify the number of replacements by changing the 4th argument



def choose_dir():
    path.insert(0,filedialog.askdirectory())

def clicked():
    regex = r"([0-9]{1,2},)|([0-9]{1,2}-[0-9]{1,2},)"
    ss = tasks.get()

    if ss[-1] != ',':
        ss = ss+','
    result = re.sub(regex, "", ss, 0, re.MULTILINE)

    if result:
        mb.askokcancel(title="Ошибка",message=("Строка не распознана"))
        return

    if path.get() == "":
        path.insert(0, filedialog.askdirectory())

    tsk = arr_generate.F(tasks.get())
    var = variants.get()
    write_docx.F(tsk, int(var), path.get())
    mb.showinfo(message="успешно")


window = Tk()
window.title("teorver_generator")
window.configure(bg="#808080")
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


# choose_dir_button = Button(window, text="выберите путь", command=choose_dir)
# choose_dir_button.grid(column=1, row=4)

window.mainloop()