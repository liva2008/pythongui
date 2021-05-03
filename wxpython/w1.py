# 1.导入wxPython库
import wx

# 2.创建Application对象
app = wx.App()

# 3.创建顶级widget
frm = wx.Frame(None, title='Hello')
panel = wx.Panel(frm)
label = wx.StaticText(panel, label = "Hello wxPython!", pos = (100,50))
frm.Show()

# 4. 进入主循环
app.MainLoop()