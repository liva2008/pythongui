import tkinter as tk

win = tk.Tk()
win.title('layout')
win.geometry('480x320')

# ! 网格布局
label1 = tk.Label(win, text='C', bg='red')
label2 = tk.Label(win, text='Java', bg='green')
label3 = tk.Label(win, text='Python', bg='blue')
label4 = tk.Label(win, text='Javascript', bg='yellow')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

win.mainloop()