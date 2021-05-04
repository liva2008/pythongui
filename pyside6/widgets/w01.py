# 1.导入pyside6库
import sys
from PySide6.QtWidgets import QApplication,QLabel

# 2.创建QApplication对象
app = QApplication(sys.argv)
# 3.新建顶级widget
label = QLabel('Hello PySide6!')
label.setGeometry(0, 0, 480, 320)
label.show()
# 4.进入主循环
app.exec_()