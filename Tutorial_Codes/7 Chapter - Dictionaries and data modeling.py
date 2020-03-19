# Tutorial 114 - Intro to dictionaries
# lists are not enough to represent real data
# user = ['Yash', 20, ['Avengers', 'MIB'], ['SAO', 'death note']]

# This list contain data but not in good way. So we use dictionaries
# dictionaries : unordered collection of data in key : value pair.
# We can store anything in dictionaries
# numbers, string, list, dictionary

# use {} to create dictionary
user1 = {'name' : 'Yash', 'age' : 20}
print(user1)
print(type(user1))

# Other methodto create dictionaries
user2 = dict(name = 'gupta', age = 22)
print(user2)
print(type(user2))
print(user2['age'])

# user = ['Yash', 20, ['Avengers', 'MIB'], ['SAO', 'death note']]
user3 = {
    'name' : 'Yash',
    'age' : 20,
    'fav_movie' : ['Avengers', 'MIB'],
    'fav_series' : ['SAO', 'death note']
}
print(user3)
print(user3['fav_movie'])

# users = {
#     user11 : {'name' : 'Yash', 'age' : 20},
#     user22 : dict(name = 'gupta', age = 22),
#     user33 : {
#         'name' : 'Yash',
#         'age' : 20,
#         'fav_movie' : ['Avengers', 'MIB'],
#         'fav_series' : ['SAO', 'death note']
#     }
# }
# print(users)

# how to add data to empty dictionary
user_info = {}
user_info['name'] = 'Krish'
user_info['age'] = 14
print(user_info)


# Tutorial 115 - Looping and In Keyword in dictionary
user = {
    'name' : 'Yash',
    'age' : 20,
    'fav_movie' : ['Avengers', 'MIB'],
    'fav_series' : ['SAO', 'death note']
}

# check if key exist in dictionary
if 'name' in user:                # 'in' checks only for keys
    print('present')
else:
    print('not present')

# check if value exist in dictionary --->   value method
if 20 in user.values():          # to check in values
    print('present')
else:
    print('not present')

# loops in dictionary
for i in user.values():          # print keys/values
    print(i)
for i in user:                   # print keys/values
    print(user[i])

# value method
user_values = user.values()
print(user_values)
print(type(user_values))

# key method
user_keys = user.keys()
print(user_keys)
print(type(user_keys))

# item method                 # most important
# Return -->  [(), (), (), ()]
user_item = user.items()
print(user_item)
print(type(user_item))

for i,j in user.items():
    print(f"Key is {i}, and Value is {j}.")


# Tutorial 116 - Add and delete data from dictionaries
user = {
    'name' : 'Yash',
    'age' : 20,
    'fav_movie' : ['Avengers', 'MIB'],
    'fav_series' : ['SAO', 'death note']
}

# how to add data
user['fav_song'] = ['song1', 'song2']
print(user)

# pop method         --->        remove item and return it
poped = user.pop('fav_movie')       # need to pass a argument in pop
print(user)
print(poped)                        # ['Avengers', 'MIB']    # return value only

# popitem method
poped_item = user.popitem()         # ('fav_series', ['SAO', 'death note'])
print(user)
print(poped_item)                   # return tuple (key,value)


# Tutorial 117 - Update Dictionary
user = {
    'name' : 'Yash',
    'age' : 20,
    'fav_movie' : ['Avengers', 'MIB'],
    'fav_series' : ['SAO', 'death note']
}

more = {'name' : 'yash gupta', 'state' : 'UP', 'hobbies' : ['coding', 'reading', 'gaming']}

user.update(more)
print(user)


# Tutorial 118 - fromkeys get copy clear method

# fromkeys  -->  create dictionary with different keys and same values
# d = {'name' : 'Unknown', 'age' : 'Unknown'}
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# d = dict.fromkeys(('name', 'age', 'height'), 'unknown')
# d = dict.fromkeys(range(1,11), 'unknown')       # "unknown" can be string, list, etc
print(d)

# get method    (Useful)        # gives values
d = {'name' : 'Unknown', 'age' : 'Unknown'}
# print(d['names'])             # return 'error' if not in dictionary
print(d.get('names'))           # return 'None' if not in dictionary

# if 'name' in d:
#     print('present')
# else:
#     print('not present')
if d.get('names'):              # 'None' act as 'False'
    print('present')
else:
    print('not present')

# d.clear()                       # Clear dictionary 
# print(d)

d1 = d.copy()                   # these are 2 dictionary
# d1 = d                          # both dictionary are same(act as 1)
print(d1 is d)


# Tutorial 119 - More about get() Method
user = {'name' : 'yash', 'age' : 20, 'age' : 30}    # if a key is given twice, last will be return
# print(user.get('names','not found'))        # return "not found" instead of 'None'
print(user)


# Tutorial 120 & 121 - Chapter 7 Exercise 1 & solution
# define a function takes a number(n) and return dictionary with its cube 
def cube_dict(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i**3
    return d

print(cube_dict(10))


# Tutorial 122 - Word Counter Dictionary
# yash gupta
# d = {'y' : 1, 'a' : 2, etc}
def word_count(txt):
    d = {}
    for char in txt:
        d[char] = txt.count(char)
    return d

print(word_count('yash gupta'))


# Tutorial 123 & 124 - Chapter 7 Exercise 2 & solution
name = input("Enter your name : ")
age = int(input("Enter your age : "))
movies = input("Enter your favourite movies (Seperated by ','): ").split(',')
songs = input("Enter your favourite songs (Seperated by ','): ").split(',')
user = {}
user['name'] = name
user['age'] = age
user['fav_movies'] = movies
user['fav_songs'] = songs

for key, value in user.items():
    print(f"{key} : {value}")


# Tutorial 125 - Dictionary Summary

