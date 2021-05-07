import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='多行文本框', size=(480, 320))
        panel = wx.Panel(self)
        #多行文本框
        self.text2 = wx.TextCtrl(panel, pos=(10, 10), size=(440,260),style=wx.TE_MULTILINE)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()