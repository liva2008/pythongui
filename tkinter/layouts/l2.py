import tkinter as tk

win = tk.Tk()
win.title('layout')
win.geometry('480x320')

# 相对布局
label1 = tk.Label(win, text='C', bg='red')
label2 = tk.Label(win, text='Java', bg='green')
label3 = tk.Label(win, text='Python', bg='blue')

label1.pack(fill=tk.Y, side=tk.LEFT)
label2.pack(fill=tk.X, side=tk.TOP)
label3.pack()

win.mainloop()