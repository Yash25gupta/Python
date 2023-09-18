import os
from pyfiglet import Figlet


def print_cool(text):
    cooltext = Figlet(font="slant")
    os.system("cls")
    os.system("mode con: cols=75 lines=30")
    return str(cooltext.renderText(text))


print(print_cool("yash_gupta"))
