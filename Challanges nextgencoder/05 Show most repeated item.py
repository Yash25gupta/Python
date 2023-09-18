# Program to show most repeated item(s) from input array
# input -> ["Next", "Gen", "Next", "Coder", "Coder"]
# output -> "Next", "Coder"


def findMostRepeated(lst):
    d = {}
    for i in lst:
        d[i] = lst.count(i)
    maxCount = 1
    for i in d.values():
        if i > maxCount:
            maxCount = i
    return [i for i in d if d[i] == maxCount]


lst = ["Next", "Gen", "Next", "Coder", "Coder", "Next"]
print(findMostRepeated(lst))
