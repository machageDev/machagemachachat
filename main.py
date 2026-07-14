from tkinter.ttk import Label

from kivy.app import App
from kivy.uix.label import Label


class MachChat(App):
    def build(self):
        return Label(text="Hello, MachChat!")
    
MachChat().run()    