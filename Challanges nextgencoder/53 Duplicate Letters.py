def duplicate(txt):
    return ''.join([c * 2 if txt.count(c) == 1 else c for c in txt])


test = 'hello World nextgencoder NextGenCoder'.split(' ')
for i in test:
    print(duplicate(i))
