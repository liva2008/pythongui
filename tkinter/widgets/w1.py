import tkinter as tk

window = tk.Tk()
window.title('单行文本框')
window.geometry('480x320')

e1 = tk.Entry(window, show=None)#文本输入框
e2 = tk.Entry(window, show='*')#密码输入框
e1.pack()
e2.pack()

window.mainloop()