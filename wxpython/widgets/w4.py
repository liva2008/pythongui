import wx
from wx.core import EVT_RADIOBOX

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)

        self.checkbox1 = wx.CheckBox(panel, -1, 'Option A')
        self.checkbox1.Bind(wx.EVT_CHECKBOX, self.print_selection)
        self.checkbox2 = wx.CheckBox(panel, -1, 'Option B')
        self.checkbox2.Bind(wx.EVT_CHECKBOX, self.print_selection)
        self.checkbox3 = wx.CheckBox(panel, -1, 'Option C')
        self.checkbox3.Bind(wx.EVT_CHECKBOX, self.print_selection)
        self.checkbox4 = wx.CheckBox(panel, -1, 'Option D')
        self.checkbox4.Bind(wx.EVT_CHECKBOX, self.print_selection)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.checkbox1, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.checkbox2, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.checkbox3, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        layout.Add(self.checkbox4, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

    def print_selection(self, event):
        print(f"your selectin is A({self.checkbox1.GetValue()}) B({self.checkbox2.GetValue()}) C({self.checkbox3.GetValue()}) D({self.checkbox4.GetValue()})")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()