def charRotaion(text):
    out = [text[i:] + text[:i] for i in range(len(text))]
    return out[1:] if len(out) > 1 else out


for i in ('', 'a', 'as', 'gen', 'next', 'coder'):
    print(charRotaion(i))
