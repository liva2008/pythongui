# 1.导入wxPython库
import wx

# 2.创建Application对象
app = wx.App()

# 3.创建顶级widget
frm = wx.Frame(None, title='Hello')
# 4.创建容器panel
panel = wx.Panel(frm)
# 5.创建组件
label = wx.StaticText(panel, label = "Hello wxPython!", pos = (100,50))
frm.Show()

# 6. 进入主循环
app.MainLoop()