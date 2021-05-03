from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

# PageLayout页面布局
class PageLayoutWidget(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PageApp(App):
    def build(self):
        return PageLayoutWidget()

if __name__ == '__main__':
    PageApp().run()