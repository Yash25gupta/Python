# A Program which will take 1 string containing opening and closing brickets as an input
# and will give output whether the brickets are balanced or not
#          TEST CASES:
#     INPUT           OUTPUT
#   '{([()])}'  ->  'Balanced'
#   '{()}[()]'  ->  'Balanced'
#   '{({[}]})'  ->  'Not Balanced'


def checkBricket(string):
    d = {'(': ')', '{': '}', '[': ']', ')': '(', '}': '{', ']': '['}
    s = ' '
    for i in string:
        s = s[:-1] if s[-1] == d[i] else s + i
    if s == ' ': return 'Balanced'
    return 'Not Balanced'


def brickets(string):
    s = ''.join(''.join(''.join(string.split('()')).split('[]')).split('{}'))
    if s == '': return 'Balanced'
    if s == string: return 'NotBalanced'
    return brickets(s)


s1 = '{([()])}'
s2 = '{()}[()]'
s3 = '{({[}]})'
print(checkBricket(s1))
print(checkBricket(s2))
print(checkBricket(s3))
print(brickets(s1))
print(brickets(s2))
print(brickets(s3))
