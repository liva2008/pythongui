from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window

class CanvasLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CanvasApp(App):
    def build(self):
        self.title = "Canvas"
        return CanvasLayoutWidget()

if __name__ == '__main__':
    Config.set('graphics', 'resizable', 0)
    Window.size = (640, 480)
    CanvasApp().run()