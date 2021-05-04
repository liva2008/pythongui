import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(240, 180))
        #创建面板
        panel = wx.Panel(self)

        #创建用户提示及输入组件
        self.label_username = wx.StaticText(panel, label='用户：')
        self.text_username = wx.TextCtrl(panel, style=wx.TE_LEFT)
        #创建密码提示及输入组件
        self.label_password = wx.StaticText(panel, label='密码：') 
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        #创建确定和取消按钮
        self.bt_ok = wx.Button(panel, label='确定')
        self.bt_cancel = wx.Button(panel, label='取消')
        #用户及输入组件横向排列
        layout_username = wx.BoxSizer(wx.HORIZONTAL)
        layout_username.Add(self.label_username, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)
        layout_username.Add(self.text_username,proportion=1,flag=wx.ALL|wx.EXPAND,border=5)
        #密码及输入组件横向排列
        layout_password = wx.BoxSizer(wx.HORIZONTAL)
        layout_password.Add(self.label_password, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)
        layout_password.Add(self.text_password,proportion=1,flag=wx.ALL|wx.EXPAND,border=5)
        #确定和取消按钮横向排列
        layout_button = wx.BoxSizer(wx.HORIZONTAL)
        layout_button.Add(self.bt_ok, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        layout_button.Add(self.bt_cancel,proportion=0,flag=wx.ALIGN_CENTER,border=5)

        #用户，密码，按钮容器纵向排列
        layout_all = wx.BoxSizer(wx.VERTICAL)
        layout_all.Add(layout_username,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)
        layout_all.Add(layout_password,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)
        layout_all.Add(layout_button,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=5)
        panel.SetSizer(layout_all)

        # 绑定确定和取消按钮事件
        self.bt_ok.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)

    #确定按钮事件处理
    def OnclickSubmit(self, event):
        username = self.text_username.GetValue()
        password = self.text_password.GetValue()
        message = ''
        if username == '' or password == '':
            message = '用户名或密码不能为空！'
        elif username == 'test' and password == '123456':
            message = '登录成功！'
        else:
            message = '用户名或密码不正确,登录失败！'
        wx.MessageBox(message)

    #取消按钮事件处理
    def OnclickCancel(self, event):
        self.text_username.SetValue('')
        self.text_password.SetValue('')    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()