from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Калькулятор")


def calc(key):
    if key == "=":
        result = eval(calc_entry.get())
        calc_entry.insert(END, "=" + str(result))
    elif key == "C":
        calc_entry.delete(0, END)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


btn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "=", "",
    "0", ".", "C", "", ""
]

r = 1
c = 0
for i in btn_list:
    cmd=lambda x=i: calc(x)                                         # возможность нажатия кнопки
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r+=1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()