# 1.导入tkinter库
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')

var = tk.StringVar()

# 3.创建按钮
def print_selection(*args):
    print("your selectin is "+var.get())
    tkinter.messagebox.showinfo(title='结果', message=var.get()) 

cb = ttk.Combobox(window, textvariable=var)
cb['values'] = ('C', 'Java', 'Python', 'Javascript')
cb.current(0)
cb.bind("<<ComboboxSelected>>", print_selection)
cb.pack()

# 5.进入主循环
window.mainloop()