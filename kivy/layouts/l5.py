from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

# StackLayout堆栈布局
class StackLayoutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        '''
        l:left, r:right,t:top, b:bottom
        按行排列：lr-tb, lr-bt, rl-tb, rl-bt
        按列排列: tb-lr, bt-lr, tb-rl, bt-rl
        布局方向8种组合
        '''
        self.orientation = 'lr-tb'
        self.add_widget(Label(text='C', size_hint=(.2, .1)))
        self.add_widget(Label(text='Java', size_hint=(.2, .1)))
        self.add_widget(Label(text='Python', size_hint=(.2, .1)))
        self.add_widget(Label(text='Javascript', size_hint=(.2, .1)))

class StackApp(App):
    def build(self):
        return StackLayoutWidget()

if __name__ == '__main__':
    StackApp().run()