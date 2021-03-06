from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.factory import Factory
import quackterpreter as Ducky
import os


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    console_output = ObjectProperty(None)

    def start_compile(self):
        to_compile = self.text_input.text
        try:
            result = Ducky.quack(to_compile)
            status = "Compilation successful!"
            print "result type: ", type(result)
        except Exception:
            result = status = "Compilation failed..."

        self._popup = Popup(title="Compilation Result",
                            content=Label(text=status),
                            size_hint=(0.4, 0.4))
        self._popup.open()
        return self.format_output(result)

    def show_result(self):
        self.console_output.text = self.start_compile()

    def format_output(self, result):
        #TODO: Fix this. Prints in a single line
        return  "\n".join(['='.join([x[0], str(x[1])]) for x in result])

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

class RubberDucky(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == "__main__":
    RubberDucky().run()
