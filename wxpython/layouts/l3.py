import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)
        self.label1 = wx.StaticText(panel, label='C')
        self.label2 = wx.StaticText(panel, label='Java')
        self.label3 = wx.StaticText(panel, label='Python')
        self.label4 = wx.StaticText(panel, label='Javascript')

        layout = wx.GridSizer(2,2,10, 10)
        layout.Add(self.label1, 0, 0)
        layout.Add(self.label2, 0, 1)
        layout.Add(self.label3, 1, 0)
        layout.Add(self.label4, 1, 1)
        panel.SetSizer(layout)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()