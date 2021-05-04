# QVBoxLayout
import sys
from PySide6.QtWidgets import (QComboBox, QApplication,
    QVBoxLayout, QDialog)
from PySide6.QtCore import Slot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        #多行文本框
        self.choices = ['C', 'Java', 'Python', 'Javascript']
        self.cb = QComboBox()
        self.cb.addItems(self.choices)
        self.cb.currentIndexChanged.connect(self.print_selection)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.cb)
        # Set dialog layout
        self.setLayout(layout)

    @Slot()
    def print_selection(self, event):
        print(f"""your selectin is {self.cb.currentText()}""")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 480, 320)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())