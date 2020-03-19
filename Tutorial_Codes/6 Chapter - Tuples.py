# Tutorial 109 - Tuples Intro
# tupal is data stuucture
# tupal can store any type of data
# tupal are immutable
# no append, no pop, no remove, no insert, ...

example = ('one', 'two', 'three', 4, 5, "six", 7.0)
days = ('monday', 'Tuesday', 'wednesday')       # Tupals are faster than list
# methods
# count, index, len() function, slicing

# example[1] = 2          # generate error (cant modify data in tupal)
print(example[:2])


# Tutorial 110 - More about tuples
mixed = ('one', 'two', 'three', 4, 5, "six", 7.0)

# looping in tuple
for i in mixed:
    print(i)

# tuple with one element
nums = (1,)
print(type(nums))

# tuple w/o parenthesis
names = 'yash', 'gupta', 'harsh'
print(type(names))

# tuple unpacking
names = ('yash', 'gupta', 'harsh')
n1, n2, n3 = names      # no of variables should be same as in tuple
print(n3)

# list inside tuple
days = ('monday', 'to', 'friday', ['saturday', 'sunday'])
days[3].pop()
days[3].append('hi')
print(days)

# functions usable with tuple
# min(), max(), sum()
example = (1,2,4,5.0)
print(sum(example))


# Tutorial 111 - Function returning two values
def func(int1,int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply

print(func(5,6))        # function return tuple
a, m = func(5,6)
print(a)
print(m)


# Tutorial 112 - Tuples 4th video
nums_tuple = tuple(range(1,11))
print(nums_tuple)
nums_list = list(nums_tuple)
print(nums_list)
nums_str = str(nums_tuple)      # print displays as tuple/list but it is string
print(nums_str)
print(type(nums_str))


# Tutorial 113 - Chapter 6 Summary

