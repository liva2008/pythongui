from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, NumericProperty

class ConverterWidget(GridLayout):
    input_type = 2
    input_value = NumericProperty()

    binary_result = StringProperty()
    octal_result = StringProperty()
    decimal_result = StringProperty()
    hexa_result = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def converting(self, value):
        if self.input_type in [2, 8, 10, 16]:
            try:
                d = int(str(value), self.input_type)
            except ValueError:
                pass
            else:
                self.decimal_result = str(d)
                self.binary_result = '{:0b}'.format(d)
                self.octal_result = '{:0o}'.format(d)
                self.hexa_result = '{:0x}'.format(d)

                print("BIN =%s" % self.binary_result)
                print("DEC =%s" % self.decimal_result)
                print("OCT =%s" % self.octal_result)
                print("HEX =%s" % self.hexa_result)
                
class ConverterApp(App):
    def build(self):
        return ConverterWidget()

if __name__ == '__main__':
    ConverterApp().run()
    