import wx
from wx.core import EVT_COMBOBOX

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)

        self.choices = ['C', 'Java', 'Python', 'Javascript']

        self.cb = wx.ComboBox(panel, -1, pos=(50, 170), size=(150, -1), choices=self.choices, style=wx.CB_READONLY) 
        self.cb.Bind(wx.EVT_COMBOBOX, self.print_selection)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.cb, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

    def print_selection(self, event):
        print(f"your selectin is {self.cb.GetSelection()}") 

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()