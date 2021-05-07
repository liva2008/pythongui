import wx
from wx.core import EVT_RADIOBOX

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)
        
        options = ['Option A', 'Option B', 'Option C', 'Option D']
        self.radiobox = wx.RadioBox(panel, -1, 'Options',(10,10), (200, 200), options, 4, wx.RA_VERTICAL)
        self.radiobox.Bind(wx.EVT_RADIOBOX, self.print_selection)

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.radiobox, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

    def print_selection(self, event):
        print(f"your selectin is {self.radiobox.GetSelection()}")
        wx.MessageBox(f"your selectin is {self.radiobox.GetSelection()}")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()