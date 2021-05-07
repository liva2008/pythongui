# 1.导入tkinter库
import tkinter as tk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()

def print_selection():
    print(f"your selectin is A({var1.get()}) B({var2.get()}) C({var3.get()}) D({var4.get()})")
    tkinter.messagebox.showinfo(title='结果', message=f"A({var1.get()}) B({var2.get()}) C({var3.get()}) D({var4.get()})") 

b1 = tk.Checkbutton(window, variable=var1, text='Option A', onvalue=1, offvalue=0, command=print_selection)
b2 = tk.Checkbutton(window, variable=var2, text='Option B', onvalue=1, offvalue=0, command=print_selection)
b3 = tk.Checkbutton(window, variable=var3, text='Option C', onvalue=1, offvalue=0, command=print_selection)
b4 = tk.Checkbutton(window, variable=var4, text='Option D', onvalue=1, offvalue=0, command=print_selection)
b1.pack()
b2.pack()
b3.pack()
b4.pack()

# 5.进入主循环
window.mainloop()