import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)
        self.label1 = wx.StaticText(panel, label='C')
        self.label2 = wx.StaticText(panel, label='Java')
        self.label3 = wx.StaticText(panel, label='Python')
        self.label4 = wx.StaticText(panel, label='Javascript')
        # 创建水平布局
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.label1, proportion=0, flag=wx.LEFT, border=15)
        layout.Add(self.label2, proportion=0, flag=wx.LEFT, border=15)
        layout.Add(self.label3, proportion=0, flag=wx.LEFT, border=15)
        layout.Add(self.label4, proportion=0, flag=wx.LEFT, border=15)
        panel.SetSizer(layout)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()