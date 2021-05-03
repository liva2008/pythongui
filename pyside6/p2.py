import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
 print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
button.setGeometry(0, 0, 480, 320)
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec_()