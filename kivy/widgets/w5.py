from typing import Text
from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

# BoxLayout
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'horizontal' # horizontal | vertical
        self.spinner = Spinner(text='C', values=('C', 'Java', 'Python', 'Javascript'), size_hint=(None, None),size=(100, 44))
        self.spinner.bind(text=self.print_selection)

        self.add_widget(self.spinner)

    def print_selection(self, spinner, text):
        print(spinner, text)

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    BoxApp().run()