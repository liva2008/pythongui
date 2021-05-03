from typing import Text
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# BoxLayout
class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical' # horizontal | vertical
        self.radio1 = BoxLayout()
        self.radio1.orientation = 'horizontal'
        self.box1 = CheckBox()
        self.label1 = Label(text='Option A')
        self.radio1.add_widget(self.box1)
        self.radio1.add_widget(self.label1)

        self.radio2 = BoxLayout()
        self.radio2.orientation = 'horizontal'
        self.box2 = CheckBox()
        self.label2 = Label(text='Option B')
        self.radio2.add_widget(self.box2)
        self.radio2.add_widget(self.label2)

        self.radio3 = BoxLayout()
        self.radio3.orientation = 'horizontal'
        self.box3 = CheckBox()
        self.label3 = Label(text='Option C')
        self.radio3.add_widget(self.box3)
        self.radio3.add_widget(self.label3)

        self.radio4 = BoxLayout()
        self.radio4.orientation = 'horizontal'
        self.box4 = CheckBox()
        self.label4 = Label(text='Option D')
        self.radio4.add_widget(self.box4)
        self.radio4.add_widget(self.label4)

        self.box1.bind(active=self.print_selection)
        self.box2.bind(active=self.print_selection)
        self.box3.bind(active=self.print_selection)
        self.box4.bind(active=self.print_selection)

        self.add_widget(self.radio1)
        self.add_widget(self.radio2)
        self.add_widget(self.radio3)
        self.add_widget(self.radio4)

    def print_selection(self, checkbox, value):
        print(checkbox, value)

class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()

if __name__ == '__main__':
    BoxApp().run()