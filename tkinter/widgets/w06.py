# 1.导入tkinter库
import tkinter as tk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')

var = tk.StringVar()

# 3.创建按钮
def print_selection():
    print("your selectin is "+var.get())
    tkinter.messagebox.showinfo(title='结果', message=var.get()) 

b1 = tk.Radiobutton(window, variable=var, text='Option A', value='1', command=print_selection)
b2 = tk.Radiobutton(window, variable=var, text='Option B', value='2', command=print_selection)
b3 = tk.Radiobutton(window, variable=var, text='Option C', value='3', command=print_selection)
b4 = tk.Radiobutton(window, variable=var, text='Option D', value='4', command=print_selection)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
# 5.进入主循环
window.mainloop()