from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout

# 散点布局
class ScatterLayoutWidget(ScatterLayout):
    pass

class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scatter_layout = ScatterLayoutWidget()
        image = AsyncImage(source='https://www.baidu.com/img/flexible/logo/pc/result.png')
        scatter_layout.add_widget(image)
        self.add_widget(scatter_layout)

class ScatterApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    ScatterApp().run()