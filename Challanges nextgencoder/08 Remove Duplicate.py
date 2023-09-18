# Program to remove surrounding duplicate from string
# Input -> "NEEXXxTTGGEENNNCCOODEERR"
# Output -> "NEXxTGENCODER"


def removeSurrDuplicate(txt):
    output = txt[0]
    for char in txt[1:]:
        if output[-1] != char:
            output += char
    return output


text = input("Input : ")
print("Output:", removeSurrDuplicate(text))
