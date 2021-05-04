# QVBoxLayout
import sys
from PySide6.QtWidgets import (QRadioButton, QApplication,
    QVBoxLayout, QDialog)
from PySide6.QtCore import Slot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        #多行文本框
        self.radio1 = QRadioButton('Option A')
        self.radio1.toggled.connect(self.print_selection)
        self.radio2 = QRadioButton('Option B')
        self.radio2.toggled.connect(self.print_selection)
        self.radio3 = QRadioButton('Option C')
        self.radio3.toggled.connect(self.print_selection)
        self.radio4 = QRadioButton('Option D')
        self.radio4.toggled.connect(self.print_selection)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        # Set dialog layout
        self.setLayout(layout)

    @Slot()
    def print_selection(self, event):
        print(f"your selectin is A({self.radio1.isChecked()}) B({self.radio2.isChecked()}) C({self.radio3.isChecked()}) D({self.radio4.isChecked()})")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 480, 320)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())