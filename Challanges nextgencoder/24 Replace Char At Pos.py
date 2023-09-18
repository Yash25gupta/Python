def replaceCharAt(text, pos, old, new):
    return ' '.join([word[:pos - 1] + new + word[pos:] if word[pos - 1] == old else word for word in text.split(' ')])


print(replaceCharAt('Hello World', 2, 'o', 'i'))
print(replaceCharAt('Hello World', 2, 'i', 'o'))
print(replaceCharAt('Next Gen Coder', 2, 'e', 'i'))
print(replaceCharAt('Next Gen Coder', 2, 'd', 'i'))
