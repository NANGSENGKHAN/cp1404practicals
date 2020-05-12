"""Author: Nang Seng Khan
   Date: 10/05/2020
   link: https://github.com/NANGSENGKHAN/cp1404practicals
"""

from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.handle_greet()
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text


DynamicLabelsApp().run()
