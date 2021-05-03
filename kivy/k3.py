# 1.导入kivy模块 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

#  2.创建App子类
class MyApp(App):
    def build(self):
        # 3.创建一个根Widget
        bt = Button(text='Click me')
        bt.bind(on_press=self.say_hello)
        return bt
    
    def say_hello(self, arg):
        popup = Popup(title='Title',content=Label(text='Message infomation'),size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    # 4.进入主循环
    MyApp().run()