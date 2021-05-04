# QVBoxLayout
import sys
from PySide6.QtWidgets import (QCheckBox, QApplication,
    QVBoxLayout, QDialog)
from PySide6.QtCore import Slot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        #多行文本框
        self.check1 = QCheckBox('Option A')
        self.check2 = QCheckBox('Option B')
        self.check3 = QCheckBox('Option C')
        self.check4 = QCheckBox('Option D')
        self.check1.toggled.connect(self.print_selection)
        self.check2.toggled.connect(self.print_selection)
        self.check3.toggled.connect(self.print_selection)
        self.check4.toggled.connect(self.print_selection)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.check1)
        layout.addWidget(self.check2)
        layout.addWidget(self.check3)
        layout.addWidget(self.check4)
        # Set dialog layout
        self.setLayout(layout)

    @Slot()
    def print_selection(self, event):
        print(f"""your selectin is A({self.check1.isChecked()}) B({self.check2.isChecked()}) C({self.check3.isChecked()}) D({self.check4.isChecked()})""")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 480, 320)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())