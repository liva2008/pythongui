import sys
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QPainter,QPen,QBrush,QPixmap
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setWindowTitle('Canvas')
        self.resize(640, 480)

    def paintEvent(self, event):
        #创建绘图对象
        painter = QPainter(self)
        #创建画笔
        pen = QPen()
        #设置画笔颜色
        pen.setColor(Qt.red)
        #设置画笔宽度
        pen.setWidth(3)
        #设置画笔样式
        pen.setStyle(Qt.SolidLine)
        #设置画笔
        painter.setPen(pen)

        #画直线
        painter.drawLine(30, 30, 200, 200)
        #画椭圆
        painter.drawEllipse(80, 10, 50, 30)
        #画矩形
        painter.drawRect(400, 10, 100, 150)

        brush = QBrush()
        brush.setColor(Qt.green)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        #画填充矩形
        painter.drawRect(300, 300, 50, 100)

        #画文本
        painter.drawText(400, 400, "Python")

        #画图像
        painter.drawPixmap(200, 160, QPixmap('.//pyside6//canvas//python.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec_()