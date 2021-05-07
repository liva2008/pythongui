import tkinter as tk

win = tk.Tk()
win.title('layout')
win.geometry('480x320')

# ! 绝对布局
label1 = tk.Label(win, text='C', bg='red')
label2 = tk.Label(win, text='Java', bg='green')
label3 = tk.Label(win, text='Python', bg='blue')

label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

win.mainloop()