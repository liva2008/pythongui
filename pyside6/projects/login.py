# QVBoxLayout
import sys
from PySide6.QtWidgets import (QLabel,QLineEdit,QPushButton, QApplication,
    QVBoxLayout,QHBoxLayout, QDialog, QMessageBox)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        #设置窗口标题
        self.setWindowTitle('登录系统')
        # 标签
        self.label_username = QLabel('用户：')
        self.label_password = QLabel('密码：')

        # 输入
        self.text_username = QLineEdit()
        self.text_username.setEchoMode(QLineEdit.Normal)
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.Password)

        # 按钮
        self.bt_ok = QPushButton('确定')
        self.bt_cancel = QPushButton('取消')

        # 用户横向布局
        layout_username = QHBoxLayout()
        layout_username.addWidget(self.label_username)
        layout_username.addWidget(self.text_username)
        # 密码横向布局
        layout_password = QHBoxLayout()
        layout_password.addWidget(self.label_password)
        layout_password.addWidget(self.text_password)
        # 按钮横向布局
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.bt_ok)
        layout_button.addWidget(self.bt_cancel)

        # Set dialog layout
        layout_all = QVBoxLayout()
        layout_all.addLayout(layout_username)
        layout_all.addLayout(layout_password)
        layout_all.addLayout(layout_button)
        self.setLayout(layout_all)

        # 绑定按钮事件
        self.bt_ok.clicked.connect(self.OnclickSubmit)
        self.bt_cancel.clicked.connect(self.OnclickCancel)

    #确定按钮事件处理
    def OnclickSubmit(self, event):
        username = self.text_username.text()
        password = self.text_password.text()
        message = ''
        if username == '' or password == '':
            message = '用户名或密码不能为空！'
        elif username == 'test' and password == '123456':
            message = '登录成功！'
        else:
            message = '用户名或密码不正确,登录失败！'
        QMessageBox.information(None, '标题', message, QMessageBox.Ok, QMessageBox.Ok)

    #取消按钮事件处理
    def OnclickCancel(self, event):
        self.text_username.setText('')
        self.text_password.setText('') 

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setGeometry(0, 0, 240, 180)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())