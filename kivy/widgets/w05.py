from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

# BoxLayout
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical' # horizontal | vertical
        self.add_widget(TextInput(multiline=True)) # 多行文本框

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    BoxApp().run()