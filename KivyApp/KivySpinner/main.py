from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder



class MiSpinner(Widget):
    def spinner_click(self, value):
        self.ids.click_label.text = f'Ha seleccionado: {value}'
    
class MainApp(App):
    def build(self):
        return MiSpinner()

if __name__ == '__main__':
    MainApp().run()