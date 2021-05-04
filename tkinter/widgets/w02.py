# 1.导入tkinter库
import tkinter as tk

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')
# 3.创建按钮
def say_hello():
    print("Button clicked, Hello!")

b = tk.Button(window, text='Click me', command=say_hello)
b.pack()
# 5.进入主循环
window.mainloop()