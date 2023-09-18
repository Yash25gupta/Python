def mirrorEncription(txt):
    out = ''
    for c in txt:
        if c.isupper(): out += chr(155 - ord(c))
        elif c.islower(): out += chr(219 - ord(c))
        else: out += c
    return out
    # return ''.join([chr(155 - ord(c)) if c.isupper() else (chr(219 - ord(c)) if c.islower() else c) for c in txt])


for i in ('abcd', 'zyxw', 'GEN', 'next', 'CODEr'):
    print(i, '-->', mirrorEncription(i))
