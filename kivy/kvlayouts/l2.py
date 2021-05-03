from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# BoxLayout
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    BoxApp().run()