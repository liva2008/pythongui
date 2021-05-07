from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

# AnchorLayout 锚点布局
class AnchorLayoutWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.anchor_x = 'right' # left|center|right
        self.anchor_y = 'top'   # top|center|bottom
        self.add_widget(Label(text='Python', size_hint=(None,None)))

class AnchorApp(App):
    def build(self):
        return AnchorLayoutWidget()

if __name__ == '__main__':
    AnchorApp().run()