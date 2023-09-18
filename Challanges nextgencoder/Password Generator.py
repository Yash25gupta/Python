import random

uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = uppers.lower()
digits = '0123456789'
symbols = '[]{}().,></\\*-+=!@#$%^& '

upper, lower, num, sym = 1, 1, 1, 0
chars = ''
if upper: chars += uppers
if lower: chars += lowers
if num: chars += digits
if sym: chars += symbols

length = 10
amount = 10

# random.seed('a')

for x in range(amount):
    password = ''.join(random.sample(chars, length))
    print(password)
