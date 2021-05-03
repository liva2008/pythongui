from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout

class RelativeLayoutWidget(RelativeLayout):
    pass

class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        relative_layout = RelativeLayoutWidget()
        # pos_hint使用x,y,center_x,center_y,right, top属性定位
        button1 = Button(text='C', size_hint=(.3,.2), pos_hint={'right':1, 'top':1})
        button2 = Button(text='Java', size_hint=(.3,.2), pos_hint={'x':0, 'y':0})
        button3 = Button(text='Python', size_hint=(.3,.2), pos_hint={'center_x':.5, 'center_y':.5})
        button4 = Button(text='Javascript', size_hint=(.3,.2), pos_hint={'x':0, 'top':1})
        relative_layout.add_widget(button1)
        relative_layout.add_widget(button2)
        relative_layout.add_widget(button3)
        relative_layout.add_widget(button4)
        self.add_widget(relative_layout)

class RelativeApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    RelativeApp().run()