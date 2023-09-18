def duplicate(txt):
    return ''.join([c * 2 if txt.count(c) == 1 else c for c in txt])


t = 'hello World nextgencoder NextGenCoder'.split(' ')
for i in t:
    print(duplicate(i))
    
