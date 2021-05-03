import wx
import wx.grid

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '布局',size=(480,320))
        panel = wx.Panel(self)

        self.grid = wx.grid.Grid(panel, -1)

        self.grid.CreateGrid(12, 4)
        self.grid.SetRowSize(2, 60)
        self.grid.SetColSize(0, 120)
        self.grid.SetColLabelValue(0, '姓名')
        self.grid.SetColLabelValue(1, '年龄')
        self.grid.SetColLabelValue(2, '身高')
        self.grid.SetColLabelValue(3, '体重')

        #self.grid.SetRowLabelValue(0, '1')
        self.grid.SetCellValue(0, 0, '卡恩')
        self.grid.SetCellValue(0, 1, '18')
        self.grid.SetCellValue(0, 2, '180')
        self.grid.SetCellValue(0, 3, '65')

        self.grid.SetCellValue(1, 0, '范冰冰')
        self.grid.SetCellValue(1, 1, '38')
        self.grid.SetCellValue(1, 2, '170')
        self.grid.SetCellValue(1, 3, '55')

        self.grid.SetCellValue(2, 0, '戚薇')
        self.grid.SetCellValue(2, 1, '28')
        self.grid.SetCellValue(2, 2, '169')
        self.grid.SetCellValue(2, 3, '50')

        self.grid.SetCellValue(3, 0, '杨霞')
        self.grid.SetCellValue(3, 1, '30')
        self.grid.SetCellValue(3, 2, '172')
        self.grid.SetCellValue(3, 3, '63')

        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.grid, proportion=0, flag=wx.BOTTOM|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(layout)

    def print_selection(self, event):
        print(f"your selectin is {self.list.GetSelection()}") #单选
        #print(f"your selectin is {self.list.GetSelections()}") #多选

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()