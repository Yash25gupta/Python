# Tutorial 152 - Enumerate function
# we use Enumerate function with for loop to track position of our item in iterable
names = ['abc', 'abcdef', 'yash']
# 0 - 'abc', 1 - 'abcdef'

# How we can do this without Enumerate function
pos = 0
for name in names:
    print(f'{pos} ---> {name}')
    pos += 1

# with enumerate function
for pos, name in enumerate(names):
    print(f'{pos} ---> {name}')

def find_pos(l,s):
    for pos, name in enumerate(l):
        if name == s:
            return pos
    return -1

print(find_pos(names,'yash'))


# Tutorial 153 - Map function
numbers = [1,2,3,4,5,6]

def square(a):
    return a**2
squares1 = list(map(square, numbers))           # map() function
print(squares1)

squares2 = list(map(lambda a: a**2, numbers))   # lambda
print(squares2)

squares3 = [i**2 for i in numbers]              # LIST Compherinsion
print(squares3)

lst = []
for i in numbers:
    lst.append(square(i))
print(lst)

names = ['abc', 'abcd', 'abcde']
length = map(len, names)
for i in length:            # we can run loop on map only once
    print(i)

length = list(map(len, names))
print(length)


# Tutorial 154 - Filter Function
numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(a):
    return a % 2 == 0
evens1 = list(filter(is_even, numbers))
print(evens1)

evens2 = list(filter(lambda a : a % 2 == 0, numbers))
print(evens2)

evens3 = [i for i in numbers if i%2 == 0]
print(evens3)


# Tutorial 155 - Iterator vs Iterable
numbers = [1,2,3,4]                         # iterables(list,tuple,...)
squares = map(lambda a:a**2, numbers)       # iterator

# for i in numbers:
    # print(i)

number_iter = iter(numbers)     # create iterator
print(next(number_iter))        # print next item
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(squares))            # no need to use iter()
print(next(squares))
print(next(squares))
print(next(squares))


# Tutorial 156 - Zip function
user_id = ['user1', 'user2', 'user3']
names = ['yash', 'harsh', 'krish']
last_name = ['gupta', 'kumar', 'varshney']

# ('user1', 'yash'), ('user2', 'harsh')
mixed = list(zip(user_id, names, last_name))
print(mixed)

# example = [('a', 1), ('b', 2)]        ****Tuple to dict
# print(dict(example))                  ****


# Tutorial 157 - Zip function part 2
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
l = [(1,2), (3,4), (5,6), (7,8)]
l1,l2 = list(zip(*l))
print(l1)
print(l2)

l1 = [1,3,5,7]
l2 = [2,4,6,8]

new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)

new_list2 = []
for i in range(min(len(l1), len(l2))):
    new_list2.append(max(l1[i], l2[i]))
print(new_list2)

new_list3 = [max(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]
print(new_list3)


# Tutorial 158 - Advance Function Practice 1
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

def av(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(av(l1,l2,l3))

av2 = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(av2(l1,l2,l3))


# Tutorial 159 - Skipped Number


# Tutorial 160 - Any and all function
nums1 = [2,4,6,8,10]
nums2 = [1,2,3,4,5,6]

# even1 = []
# for num in nums1:
#     even1.append(num%2 == 0)
# print(even1)
# print(all(even1))         # all() checks all values are True or not
# print(any(even1))         # all() checks if any value is True or not

print(all([num % 2 == 0 for num in nums1]))


# Tutorial 161 - Any and all practice
def my_sum(*args):
    if all([type(arg) == int or type(arg) == float for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong type of data is entered"

l = [1, 2, 3, 4.0, 'yash', ['yas', 2]]
print(my_sum(l))


# Tutorial 162 - Advance min() and max()
# numbers = [1,3,4,5,8]
# print(max(numbers))

# def func(item):
#     # return [len(i) for i in item]
#     return len(item)
names = ['Yash', 'gupta', 'ab']
print(max(names, key= lambda item : len(item)))

students = [
    {'name' : 'yash', 'score' : 50, 'age' : 20},
    {'name' : 'gupta', 'score' : 70, 'age' : 15},
    {'name' : 'hsdfdsdg', 'score' : 60, 'age' : 30},
]
# print name of student whose 'score' is max
# print(max(students, key= lambda item : item.get('score'))['name'])
print(max(students, key= lambda item : item['score'])['name'])

students2 = {
    'yash' : {'score' : 90, 'age' : 20},
    'gupta' : {'score' : 74, 'age' : 30},
    'ysh' : {'score' : 82, 'age' : 26},
}
# print name of student whose 'score' is max
print(max(students2, key= lambda item : students2[item]['score']))


# Tutorial 163 - Advance sorted function
fruits1 = ['grapes', 'mango', 'apple']
fruits1.sort()
print(fruits1)

fruits2 = ('grapes', 'mango', 'apple')
print(sorted(fruits2))          # return list

fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))

guitars = [
    {'model' : 'yamaha f310', 'price' : 8400},
    {'model' : 'faith naptune', 'price' : 50000},
    {'model' : 'faith apollo', 'price' : 35000},
    {'model' : 'taylor 814ce', 'price' : 450000},
]
print(sorted(guitars, key= lambda d : d['price'], reverse= True))

guitars = {
    'y' : {'model' : 'yamaha f310', 'price' : 8400},
    'fn' : {'model' : 'faith naptune', 'price' : 50000},
    'fa' : {'model' : 'faith apollo', 'price' : 35000},
    't' : {'model' : 'taylor 814ce', 'price' : 450000},
}
print(sorted(guitars, key= lambda d : guitars[d]['price']))


# Tutorial 164 - More about functions
# what are doc string
# how to write doc string
# how to see doc string
# what is help function

def add(a,b):
    ''' this function takes 2 numbers and return their sum '''
    return a+b
print(add.__doc__)
print(help(sum))
print(sum.__doc__)

