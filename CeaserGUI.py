# some changes
import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    lw = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
          'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    bw = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
          'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.encrypt = ttk.Entry()
        self.encrypt.place(x=400, y=100)
        self.encrypt.pack()

        self.key = ttk.Entry()
        self.key.place(x=400, y=100)
        self.key.pack()

        self.relult = ttk.Entry()
        self.relult.place(x=400, y=100)
        self.relult.pack()

        btn = ttk.Button(text='зашифровать', command=self.encryption)
        btn1 = ttk.Button(text='расшифровать', command=self.decryption)
        btn_clear = ttk.Button(text='очистить', command=self.clear)
        btn.pack()
        btn1.pack()
        btn_clear.pack()

    def clear(self):
        self.encrypt.delete(0, 'end')
        self.key.delete(0, 'end')
        self.relult.delete(0, 'end')

    def encryption(self):
        text = self.encrypt.get()
        key = int(self.key.get())

        shift = " "
        for i in text:
            if i in self.lw:
                ind = self.lw.index(i) % len(self.lw)
                shift += self.lw[(ind + key) % len(self.lw)]
            elif i in self.bw:
                ind = self.bw.index(i) % len(self.bw)
                shift += self.bw[(ind + key) % len(self.bw)]
            else:
                shift += i
        self.relult.insert(0, shift)

    def decryption(self):
        text = self.encrypt.get()
        key = int(self.key.get())

        shift = " "
        for i in text:
            if i in self.lw:
                ind = self.lw.index(i)
                shift += self.lw[ind - key]
            elif i in self.bw:
                ind = self.bw.index(i)
                shift += self.bw[ind - key]
            else:
                shift += i
        self.relult.insert(0, shift)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Шифр Цезаря")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
root.mainloop()
