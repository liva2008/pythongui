# QVBoxLayout
import sys
from PySide6.QtWidgets import (QLabel, QApplication,
    QVBoxLayout, QDialog)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.label1 = QLabel("C")
        self.label2 = QLabel("Java")
        self.label3 = QLabel("Python")
        self.label4 = QLabel("Javascript")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
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