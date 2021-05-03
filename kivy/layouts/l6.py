from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

# PageLayout页面布局
class PageLayoutWidget(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Button(text='C', background_color=[.1, .2, .3, 1]))
        self.add_widget(Button(text='Java', background_color=[.2, .3, .3, 1]))
        self.add_widget(Button(text='Python', background_color=[.3, .4, .3, 1]))
        self.add_widget(Button(text='Javascript', background_color=[.4, .5, .3, 1]))

class PageApp(App):
    def build(self):
        return PageLayoutWidget()

if __name__ == '__main__':
    PageApp().run()