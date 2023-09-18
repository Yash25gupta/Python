# A program which will take 4 arguments (1-string text, 2-int where old char will searched,
# 3-string old char to replace, 4-new char ) if it is in given string index
# input ->
# output -> 0 < length of list < 6
#       TEST CASES:
#           INPUT                          OUTPUT
#   func('Hello World', 2, o, i)         5 5 5 5 5


def replaceCharAt(text, pos, old, new):
    return ' '.join([word[:pos - 1] + new + word[pos:] if word[pos - 1] == old else word for word in text.split(' ')])


print(replaceCharAt('Hello World', 2, 'o', 'i'))
print(replaceCharAt('Hello World', 2, 'i', 'o'))
print(replaceCharAt('Next Gen Coder', 2, 'e', 'i'))
print(replaceCharAt('Next Gen Coder', 2, 'd', 'i'))
