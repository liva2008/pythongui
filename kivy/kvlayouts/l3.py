from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

# AnchorLayout
class AnchorLayoutWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class AnchorApp(App):
    def build(self):
        return AnchorLayoutWidget()

if __name__ == '__main__':
    AnchorApp().run()