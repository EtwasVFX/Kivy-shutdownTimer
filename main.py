from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
import os

Config.set("graphics", "width", "600")
Config.set("graphics", "height", "300")

class MyApp(App):
    title = "Shutdown"
    
    def build(self):
        return Builder.load_file("main.kv")

    def on_button_click(self, instance):
    
        print("clicked")
        time_input = self.root.ids.idkinput.text
        test = int(time_input) * 60
        print(test)
        
        if time_input is not None :
            os.system(f"shutdown /s /t {test}")
    def Cancel(self, instance) :
            os.system("shutdown /a")
        
            

        



MyApp().run()