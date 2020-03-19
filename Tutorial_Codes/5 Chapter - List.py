# Tutorial 82 - Intro to list
numbers = [1, 2, 3, 4, 5]
words = ['One','Two', "Three", "Four", 'Five']
mixed = [1, 2, 'Three', "Four", 5]
print(numbers)
print(words[0:3])
print(mixed[-1])
mixed[1] = "Two"
print(mixed)
mixed[1:] = 'Two'
print(mixed)
mixed[1:] = 'Two', 3, "Four"
print(mixed)


# Tutorial 83 - Add data to list
fruits = ['grapes', 'mango']
fruits.append('apple')          # Add item to list at last position in the list
print(fruits)

fruits = []
fruits.append('apple')
fruits.append('mango')
print(fruits)


# Tutorial 84 - More methods to add data
fruits1 = ['grapes', 'mango']
fruits1.insert(1,'apple')              # 1 is position to add   "insert"
# print(fruits1)
fruits2 = ['apple', 'orange']
fruits = fruits1 + fruits2             # join(concatenate)
# print(fruits)
fruits1.extend(fruits2)                # extend(add list items to list) mostused
fruits1.append(fruits2)                # append(add list to list)
# print(fruits1)


# Tutorial 85 - Delete data from list
fruits = ['Orange', 'apple', 'pear', 'banana', 'kiwi', 'mango']
fruits.pop(1)                # Removes last by defaut (removes 'orange')
del fruits[1]                # We should pass parameter
fruits.remove('banana')      # if 2 banana are there it remove 1st banana
# print(fruits)

# append, extend, insert          # To add data
# pop, remove, del                # To remove data


# Tutorial 86 - In keyword with list
fruits = ['Orange', 'apple', 'pear', 'banana', 'kiwi', 'mango']
if 'apple' in fruits:
    print("apple is present")
else:
    print("apple is absent")


# Tutorial 87 - Some more list methods
fruits = ['orange', 'apple', 'pear', 'banana','kiwi', 'apple', 'kiwi', 'mango', 'apple']
# print(fruits.count('apple'))      # Count
# fruits.sort()                     # Sort list
# print(sorted(fruits))             # Only print sorted list
# fruits.clear()                    # Remove all entry in list
print(fruits)
new_fruits = fruits.copy()        # Create a copy of list
print(new_fruits)


# Tutorial 88 - is vs equals
fruits1 = ['orange', 'apple', 'pear', 'kiwi']
fruits2 = ['banana','kiwi', 'apple', 'kiwi', 'mango', 'apple']
fruits3 = ['orange', 'apple', 'pear', 'kiwi']
print(fruits1 == fruits3)       # values are same
print(fruits1 is fruits3)       # is is used to check object is in same memory or not


# Tutorial 89 - join and split method
# Split convert string to list(if 1 variable)
#  and to 2 variables if 2 variable is used.
user_info = 'Yash,20'.split(',')    # user_info --> name, age
print(user_info)

# Join convert list to string
user_info = ['yash', '24']
print(','.join(user_info))


# Tutorial 90 - List vs Array

# c, c++, java --->  'array' store same type of data (int, string)
# python --->  'list' store any data / flexiable            + + + + +
# python --->  'array module' store single type of data     - - - - -
# numpy arrays - binding with c / fast                      + + + + +
# javascript array = python list


# Tutorial 91 - List vs String
# string are immutable
# list are mutable
s = "string"
t = s.title()
print(t)

l = ['word1', 'word2', 'word3', 'word4'] 
l.pop()
print(l)


# Tutorial 92 - Looping in list
fruits = ['banana','kiwi', 'apple', 'kiwi', 'mango', 'apple']
for fruit in fruits:
    print(fruit)

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# Tutorial 93 - List inside List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      # 3 items "2d list"
for sublist in matrix:
    print(sublist)

for sublist in matrix:
    for i in sublist:
        print(i)

print(matrix[2][0])             # print '7'

s = 'String123'
print(type(s))                  # Display type of variable
print(type(matrix))


# Tutorial 94 - More about lists
numbers = list(range(1,11))

# poped = numbers.pop()             # pop method also return poped no
# print(poped)

print(numbers)
# print(numbers.index(1))             # give position of passed value

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))


# Tutorial 95 & 96 - Exercise 1 & Solution
# Generate a function that returns square of each item in a list
def sq_list(l):
    sq = []
    for i in l:
        sq.append(i**2)
    return sq

lst = list(range(1,11))
print(lst)
print(sq_list(lst))


# Tutorial 97 & 98 - Exercise 2 & solution
# Define a function which will take list as argument and returns a reversed list 
# [1, 2, 3, 4] -->  [4, 3, 2, 1]

# def rev_list(l):
#     l.reverse()
#     return l

# def rev_list(l):
#     return l[::-1]

def rev_list(l):
    reverse = []
    for i in range(len(l)):
        reverse.append(l.pop())
    return reverse

lst = [1, 2, 3, 4, 5]
print(rev_list(lst))


# Tutorial 99 & 100 - Exercise 3 & Solution
# ['abc', 'stu', 'xyz'] -->  ['cba', 'uts', 'zyx']
def rev_element(l):
    reverse = []
    for i in l:             # i is element of list
        reverse.append(i[::-1])
    return reverse

lst = ['yash', 'yaya', 'krish']
print(rev_element(lst))


# Tutorial 101 & 102 - Exercise 4 & solution
# [1,2,3,4,5,6,7] -->  [[1,3,5,7], [2,4,6]]
def filter_odd_even(l):
    o = []
    e = []
    for i in l:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
    r = [o, e]
    return r

lst = list(range(1,11))
print(filter_odd_even(lst))


# Tutorial 103 & 104 - Exercise 5 & Solution
# [1,2,3,4,5] , [1,2,6,7] -->  [1,2]
def common_in_2_list(l1,l2):
    c = []
    for i in l1:
        if i in l2:
            c.append(i)
    return c

a = [1,2,3,4,5]
b = [1,2,6,7,4]
print(common_in_2_list(a,b))


# Tutorial 105 - Min and max function
num = [6,60,3,78,11]
print(min(num))
print(max(num))

def greatest_diff(l):
    return max(l) - min(l)

print(greatest_diff(num))


# Tutorial 106 & 107 - Exercise 6 & solution
# count no of list inside a list
def cnt_list(l):
    cnt = 0
    for i in l:
        if type(i) == list:
            cnt += 1
    return cnt

lst = [1,3,2,[5,6],[3,8,4],'yash',5,[1]]
print(cnt_list(lst))


# Tutorial 108 - Chapter 5 Summary

