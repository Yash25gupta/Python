# Take input as string and arrange its character in alphabitical order
# Eg -> YashGupta -> aaGhpstuY


def arrange(text):
    return "".join(sorted(list(text), key=lambda i: i.lower()))


print(arrange("YashGupta"))
