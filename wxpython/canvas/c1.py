import wx 
 
class MyFrame(wx.Frame): 
   def __init__(self, parent, title): 
      super(MyFrame, self).__init__(parent, title = title,size = (640,480))  
      self.Bind(wx.EVT_PAINT, self.OnPaint) 
      self.Centre() 
                
   def OnPaint(self, e): 
      dc = wx.PaintDC(self) 
      brush = wx.Brush("white")  
      dc.SetBackground(brush)  
      dc.Clear() 
        
      dc.DrawBitmap(wx.Bitmap(".//wxpython//canvas//python.png"),10,10,True) 
      color = wx.Colour(255,0,0)
      b = wx.Brush(color) 
                
      dc.SetBrush(b) 
      dc.DrawCircle(300,125,50) 
      dc.SetBrush(wx.Brush(wx.Colour(255,255,255))) 
      dc.DrawCircle(300,125,30) 
                
      font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
      dc.SetFont(font) 
      dc.DrawText("Hello wxPython",200,10) 
                
      pen = wx.Pen(wx.Colour(0,0,255)) 
      dc.SetPen(pen) 
      dc.DrawLine(200,50,350,50) 
      dc.SetBrush(wx.Brush(wx.Colour(0,255,0), wx.CROSS_HATCH)) 
      dc.DrawRectangle(380, 15, 90, 60) 

if __name__ == '__main__':         
    app = wx.App() 
    frame = MyFrame(None,"Canvas") 
    frame.Show()
    app.MainLoop()