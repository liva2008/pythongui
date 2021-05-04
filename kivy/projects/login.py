from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.core.window import Window

# BoxLayout
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 标签
        self.label_username = Label(text='username:')
        self.label_password = Label(text='password:')

        # 输入
        self.text_username = TextInput()
        self.text_password = TextInput(password=True)

        # 按钮
        self.bt_ok = Button(text='OK')
        self.bt_cancel = Button(text='Cancel')

        # 用户横向布局
        layout_username = BoxLayout()
        layout_username.orientation = 'horizontal'
        layout_username.add_widget(self.label_username)
        layout_username.add_widget(self.text_username)

        # 密码横向布局
        layout_password = BoxLayout()
        layout_password.orientation = 'horizontal'
        layout_password.add_widget(self.label_password)
        layout_password.add_widget(self.text_password)

        # 按钮横向布局
        layout_button = BoxLayout()
        layout_button.orientation = 'horizontal'
        layout_button.add_widget(self.bt_ok)
        layout_button.add_widget(self.bt_cancel)

        self.orientation = 'vertical' # horizontal | vertical
        self.add_widget(layout_username)
        self.add_widget(layout_password)
        self.add_widget(layout_button)

        #绑定事件
        self.bt_ok.bind(on_press=self.OnclickSubmit)
        self.bt_cancel.bind(on_press=self.OnclickCancel)
        
    #确定按钮事件处理
    def OnclickSubmit(self, event):
        username = self.text_username.text
        password = self.text_password.text
        message = ''
        if username == '' or password == '':
            #message = '用户名或密码不能为空！'
            message = 'Username or Password can not be empty!'
        elif username == 'test' and password == '123456':
            #message = '登录成功！'
            message = 'Succfully!'
        else:
            #message = '用户名或密码不正确,登录失败！'
            message = 'Username or Password may be error!'
        popup = Popup(title='Result',content=Label(text=message),size_hint=(None, None), size=(400, 400))
        popup.open()

    #取消按钮事件处理
    def OnclickCancel(self, event):
        self.text_username.text = ''
        self.text_password.text = ''


class BoxApp(App):
    def build(self):
        self.title = "登录系统"
        return BoxLayoutWidget()

if __name__ == '__main__':
    Config.set('graphics', 'resizable', 0)
    Window.size = (240, 100)
    BoxApp().run()