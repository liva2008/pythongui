# QVBoxLayout
import sys
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QApplication,
    QVBoxLayout, QDialog)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        
        self.table = QTableWidget(10, 4)
        self.table.setHorizontalHeaderLabels(['姓名','年龄','身高','体重'])

        self.table.setItem(0, 0, QTableWidgetItem('卡恩'))
        self.table.setItem(0, 1, QTableWidgetItem('18'))
        self.table.setItem(0, 2, QTableWidgetItem('180'))
        self.table.setItem(0, 3, QTableWidgetItem('65'))

        self.table.setItem(1, 0, QTableWidgetItem('范冰冰'))
        self.table.setItem(1, 1, QTableWidgetItem('38'))
        self.table.setItem(1, 2, QTableWidgetItem('170'))
        self.table.setItem(1, 3, QTableWidgetItem('55'))

        self.table.setItem(2, 0, QTableWidgetItem('戚薇'))
        self.table.setItem(2, 1, QTableWidgetItem('28'))
        self.table.setItem(2, 2, QTableWidgetItem('169'))
        self.table.setItem(2, 3, QTableWidgetItem('50'))

        self.table.setItem(3, 0, QTableWidgetItem('杨霞'))
        self.table.setItem(3, 1, QTableWidgetItem('30'))
        self.table.setItem(3, 2, QTableWidgetItem('172'))
        self.table.setItem(3, 3, QTableWidgetItem('63'))
        

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        # Set dialog layout
        self.setLayout(layout)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 480, 320)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())