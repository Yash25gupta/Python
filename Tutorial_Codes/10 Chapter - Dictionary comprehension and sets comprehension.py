# Tutorial 137 - Dictionary Comprehension
# square = {1:1, 2:4, ...}
# square = {i:i**2 for i in range(1,11)}
square = {'square of {} is'.format(i): i**2 for i in range(1, 11)}
for k, v in square.items():
    print('{} : {}'.format(k, v))

txt = 'Yashgutaup'
word_count = {char: txt.count(char) for char in txt}
print(word_count)


# Tutorial 138 - Dictionary comprehension with if else
o_e = {i: ('Even' if i % 2 == 0 else 'Odd') for i in range(1, 11)}
print(o_e)


# Tutorial 139 - Sets comprehension
# not so important
s = {i**2 for i in range(1, 11)}
print(s)

names = ['Yash', 'Harsh', 'Krish']
first = {i[0] for i in names}
print(first)
