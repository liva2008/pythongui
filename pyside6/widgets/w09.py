# QVBoxLayout
import sys
from PySide6.QtWidgets import (QListWidget, QApplication,
    QVBoxLayout, QDialog, QAbstractItemView)
from PySide6.QtCore import Slot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        #多行文本框
        self.choices = ['C', 'Java', 'Python', 'Javascript']
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SingleSelection) #单选
        #self.list.setSelectionMode(QAbstractItemView.MultiSelection)  #多选
        self.list.addItems(self.choices)
        self.list.itemClicked.connect(self.print_selection)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.list)
        # Set dialog layout
        self.setLayout(layout)

    @Slot()
    def print_selection(self, event):
        print(f"""your selectin is {event.text()}""")#单选
        #print(f'your selection is {[item.text() for item in self.list.selectedItems()]}')#多选

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 480, 320)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())