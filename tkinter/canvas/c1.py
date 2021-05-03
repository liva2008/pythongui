import tkinter as tk

window = tk.Tk()
window.title('Canvas')
window.geometry('640x480')

# 创建画布
canvas = tk.Canvas(window, bg='green', height=480, width=640)

# 画图像
image_file = tk.PhotoImage(file='.//tkinter//canvas//python.png')
image = canvas.create_image(300, 300, anchor='n', image=image_file)

x0,y0,x1,y1 = 100, 100, 150, 150

#画直线
line = canvas.create_line(x0-50, y0-50,x1-50,y1-50,fill='blue',width=10)
#画矩形
rect = canvas.create_rectangle(330, 30, 330+20, 30+20,fill='red')
#画椭圆
oval = canvas.create_oval(100, 200, 300, 240, fill='pink')
#画扇形
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=90)
#画多边形
poly = canvas.create_polygon(20,20, 50, 50, 80, 80, 100,200, 20,20,outline='blue', fill='yellow')
#画文本
text = canvas.create_text(300, 300, text = "Python")

canvas.pack()

window.mainloop()
