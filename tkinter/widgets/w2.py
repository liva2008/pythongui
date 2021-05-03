import tkinter as tk

window = tk.Tk()
window.title('多行文本框')
window.geometry('480x320')

e1 = tk.Text(window, height=25)
e1.pack()

window.mainloop()