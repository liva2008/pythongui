from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

# StackLayout堆栈布局
class StackLayoutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class StackApp(App):
    def build(self):
        return StackLayoutWidget()

if __name__ == '__main__':
    StackApp().run()