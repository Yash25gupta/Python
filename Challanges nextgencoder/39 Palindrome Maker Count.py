def makePalindrome(txt):
    txt = txt.lower()
    if txt == txt[::-1]: return 0
    for i in range(len(txt)):
        if txt[i:] == txt[:i - 1:-1]:
            return i
    # return [i for i in range(len(txt)) if txt[i:] == txt[:i - 1:-1]][0]


for i in ('bob', 'add', 'raca', 'list', 'mada'):
    print(makePalindrome(i))
