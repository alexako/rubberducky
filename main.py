from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class RubberDucky(App):
    def build(self):
        layout = BoxLayout(spacing=10)
        return layout


if __name__ == "__main__":
    RubberDucky().run()
