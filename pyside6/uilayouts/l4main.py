import sys
from PySide6.QtWidgets import QApplication,QDialog
from l4 import Ui_Dialog

class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    app.exec_()
