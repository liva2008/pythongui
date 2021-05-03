from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

# GridLayout网格布局
class GridLayoutWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.rows = 2  #行数
        self.cols = 2  #列数

        self.add_widget(Label(text='C'))
        self.add_widget(Label(text='Java'))
        self.add_widget(Label(text='Python'))
        self.add_widget(Label(text='Javascript'))

class GridApp(App):
    def build(self):
        return GridLayoutWidget()

if __name__ == '__main__':
    GridApp().run()