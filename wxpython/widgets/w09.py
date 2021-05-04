import wx
from wx.core import EVT_LISTBOX

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)

        self.choices = ['C', 'Java', 'Python', 'Javascript']

        self.list = wx.ListBox(panel, -1, pos=(50, 170), size=(150, -1), choices=self.choices, style=wx.LB_SINGLE) #单选
        #self.list = wx.ListBox(panel, -1, pos=(50, 170), size=(150, -1), choices=self.choices, style=wx.LB_MULTIPLE) #多选
        self.list.Bind(wx.EVT_LISTBOX, self.print_selection)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.list, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

    def print_selection(self, event):
        print(f"your selectin is {self.list.GetSelection()}") #单选
        #print(f"your selectin is {self.list.GetSelections()}") #多选

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()