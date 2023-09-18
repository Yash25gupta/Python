# Program to convert string from camelCase into snack_case or vice versa
CAPITALS = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'


def isCamelCase(txt):
    if "_" in txt or txt[0] in CAPITALS: return False
    for char in txt:
        if char in CAPITALS: return True


def is_snake_case(txt):
    if "_" not in txt or txt[0] in CAPITALS: return False
    for char in txt:
        if char in CAPITALS: return False
    return True


def getCamelCase(txt):
    lst = txt.split("_")
    newTxt = ''
    for i in lst:
        newTxt += i.capitalize() if newTxt != '' else i
    return newTxt


def get_snake_case(txt):
    newTxt = ''
    for char in txt:
        newTxt += ("_" + char.lower()) if char in CAPITALS else char
    return newTxt


def swapCase(txt):
    ''' This function change camelCase into snake_case and vice versa. '''
    if len(txt) > 5:
        if isCamelCase(txt): return get_snake_case(txt)
        elif is_snake_case(txt): return getCamelCase(txt)
    return txt + "\nGiven String is neither in 'camelCase' nor 'snake_case'."


text = input("Input : ")
print("Output:", swapCase(text))
