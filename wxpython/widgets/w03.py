import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='button', size=(480, 320))
        panel = wx.Panel(self)
        self.bt = wx.Button(panel, label='Click me', pos=(100, 100))
        self.Bind(wx.EVT_BUTTON, self.say_hello, self.bt)

    def say_hello(self, event):
        dlg = wx.MessageDialog(None, u"消息信息", u"标题", wx.OK | wx.ICON_INFORMATION)
        #dlg = wx.MessageDialog(None, u"消息信息", u"标题", wx.YES_NO | wx.ICON_QUESTION)
        #dlg = wx.MessageDialog(None, u"消息信息", u"标题", wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

