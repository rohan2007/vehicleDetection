from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App):
    def build(self):
        return Button(text="Hello World")

if __name__ == '__main__':
    LanguageLearnerApp().run()