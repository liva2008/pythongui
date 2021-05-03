from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

# FloatLayout绝对布局
class FloatLayoutWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 通过绝对属性size和pos,相对属性size_hint和pos_hint设置组件大小和位置
        self.add_widget(Label(text='C', size=(100, 30), pos= (10, 10)))
        self.add_widget(Label(text='Java', size=(100, 30), pos= (50, 50)))
        self.add_widget(Label(text='Python', size=(100, 30), pos= (100, 100)))
        self.add_widget(Label(text='Javascript', size=(100, 30), pos= (150, 150)))

class FloatApp(App):
    def build(self):
        return FloatLayoutWidget()

if __name__ == '__main__':
    FloatApp().run()