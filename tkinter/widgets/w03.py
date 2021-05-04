# 1.导入tkinter库
import tkinter as tk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('MessageBox')
window.geometry('480x320')
# 3.创建按钮
def say_hello():
    tkinter.messagebox.showinfo(title='标题', message='消息信息')              # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='标题', message='消息信息！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='标题', message='消息信息！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='标题', message='消息信息！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='标题', message='消息信息！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='标题', message='消息信息！'))  # return 'True', 'False'

b = tk.Button(window, text='MessageBox', command=say_hello)
b.pack()
# 5.进入主循环
window.mainloop()