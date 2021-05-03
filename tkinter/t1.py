# 1.导入tkinter库
import tkinter as tk

# 2.创建窗口window
window = tk.Tk()
window.title('Hello')
window.geometry('480x320')
# 3.创建标签
l = tk.Label(window, text='Hello tkinter!', bg='green')
# 4.放置标签
l.pack()
# 5.进入主循环
window.mainloop()
