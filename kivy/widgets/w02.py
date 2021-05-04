# 1.导入kivy模块
import kivy 
from kivy.app import App
from kivy.uix.button import Button

#  2.创建App子类
class MyApp(App):
    def build(self):
        # 3.创建一个根Widget
        bt = Button(text='Click me')
        bt.bind(on_press=self.say_hello)
        return bt
    
    def say_hello(self, arg):
        print("Button clicked, Hello!")

if __name__ == '__main__':
    # 4.进入主循环
    MyApp().run()