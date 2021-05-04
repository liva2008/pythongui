from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window

# GridLayout网格布局
class RegisterWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RegisterApp(App):
    def build(self):
        self.title = "用户注册"
        return RegisterWidget()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', 0)
    Window.size = (800, 600)
    RegisterApp().run()
