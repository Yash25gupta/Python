# Tutorial 1    -----------------------------------
import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="My first window")


# Tutorial 2    -----------------------------------
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="First Name"))
        self.fname = TextInput(multiline=False)
        self.add_widget(self.fname)

        self.add_widget(Label(text="Last Name"))
        self.lname = TextInput(multiline=False)
        self.add_widget(self.lname)

        self.add_widget(Label(text="Email"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class MyApp(App):
    def build(self):
        return MyGrid()


# Tutorial 3    -----------------------------------
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name"))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name"))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.btn_press)
        self.add_widget(self.submit)

    def btn_press(self, instance):
        name = self.fname.text
        last = self.lname.text
        email = self.email.text

        print(f"Name : {name} {last} \nEmail : {email}")
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
