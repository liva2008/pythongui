# 1.导入tkinter库
import tkinter as tk
import tkinter.messagebox

# 2.创建窗口window
window = tk.Tk()
window.title('登录系统')
window.geometry('240x180')

#用户标簦
tk.Label(window, text='用户：').place(x=30, y=10)
#密码标签
tk.Label(window, text='密码：').place(x=30, y=50)

#用户输入
var_username = tk.StringVar()
entry_username = tk.Entry(window, textvariable=var_username)
entry_username.place(x=70, y=10)

#密码输入
var_password = tk.StringVar()
entry_password = tk.Entry(window, textvariable=var_password, show='*')
entry_password.place(x=70, y=50)

#确定按钮事件处理
def OnclickSubmit():
    username = var_username.get()
    password = var_password.get()
    message = ''
    if username == '' or password == '':
        message = '用户名或密码不能为空！'
    elif username == 'test' and password == '123456':
        message = '登录成功！'
    else:
        message = '用户名或密码不正确,登录失败！'
    tkinter.messagebox.showinfo(title='标题', message=message)

#取消按钮事件处理
def OnclickCancel():
    var_username.set('')
    var_password.set('') 

#确定按钮
bt_ok = tk.Button(window, text='确定', command=OnclickSubmit)
bt_ok.place(x=80, y=100)
#取消按钮
bt_cancel = tk.Button(window, text='取消', command=OnclickCancel)
bt_cancel.place(x=120, y=100)

# 5.进入主循环
window.mainloop()