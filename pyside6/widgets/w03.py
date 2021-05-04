import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    QMessageBox.information(None, '标题', '消息信息', QMessageBox.Ok, QMessageBox.Ok)
    #QMessageBox.question(None ,"标题","消息信息？",QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Ok)
    #QMessageBox.warning(None ,"标题","消息信息？", QMessageBox.Reset|QMessageBox.Help|QMessageBox.Cancel,QMessageBox.Reset)

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.setGeometry(0, 0, 480, 320)
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec_()