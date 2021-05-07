from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# BoxLayout 箱式布局
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'horizontal' # horizontal | vertical
        self.add_widget(Label(text='C'))
        self.add_widget(Label(text='Java'))
        self.add_widget(Label(text='Python'))
        self.add_widget(Label(text='Javascript'))

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    BoxApp().run()