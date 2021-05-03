from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# FloatLayout绝对布局
class FloatLayoutWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class FloatApp(App):
    def build(self):
        return FloatLayoutWidget()

if __name__ == '__main__':
    FloatApp().run()