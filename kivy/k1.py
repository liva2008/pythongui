# 1.导入kivy模块
import kivy 
from kivy.app import App
from kivy.uix.label import Label

#  2.创建App子类
class MyApp(App):
    def build(self):
        # 3.创建一个根Widget
        return Label(text='Hello kivy!')

if __name__ == '__main__':
    # 4.进入主循环
    MyApp().run()