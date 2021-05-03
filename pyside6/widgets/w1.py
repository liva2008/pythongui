# QVBoxLayout
import sys
from PySide6.QtWidgets import (QLineEdit, QApplication,
    QVBoxLayout, QDialog)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        #文本框
        self.text1 = QLineEdit()
        self.text1.setEchoMode(QLineEdit.Normal)
        #密码框
        self.text2 = QLineEdit()
        self.text2.setEchoMode(QLineEdit.Password)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
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