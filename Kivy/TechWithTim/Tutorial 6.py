import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class My6App(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    My6App().run()
