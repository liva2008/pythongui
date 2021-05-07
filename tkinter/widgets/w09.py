# 1.导入tkinter库
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')

var = tk.StringVar()
var.set(('C', 'Java', 'Python', 'Javascript'))

# 3.创建按钮
def print_selection(*args):
    print(f"your selectin is {list.curselection()}")
    tkinter.messagebox.showinfo(title='结果', message=f"{list.curselection()}") 

#list = tk.Listbox(window, listvariable=var,selectmode=tk.MULTIPLE) # 多选
list = tk.Listbox(window, listvariable=var) #单选
list.bind("<<ListboxSelect>>", print_selection)
list.pack()

# 5.进入主循环
window.mainloop()