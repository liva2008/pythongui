#引入库
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        # 创建容器panel
        panel = wx.Panel(self)
        self.label1 = wx.StaticText(panel, label='C')
        self.label2 = wx.StaticText(panel, label='Java')
        self.label3 = wx.StaticText(panel, label='Python')
        self.label4 = wx.StaticText(panel, label='Javascript')
        # 创建布局VRETICAL或HORIZONTAL
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.label1, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.label2, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.label3, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.label4, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

if __name__ == '__main__':
    # 创建App
    app = wx.App()
    # 创建Frame窗体
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    # 进入主循环
    app.MainLoop()