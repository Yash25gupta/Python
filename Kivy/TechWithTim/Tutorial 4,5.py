import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    email = ObjectProperty(None)

    def btnsubmit(self):
        print(f"Name: {self.fname.text} {self.lname.text} \nEmail: {self.email.text}")
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""


class My45App(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    My45App().run()
