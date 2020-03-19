# Tutorial 128 - What is list comprehension
# with help of list comprehension we can create a list in one line

# create a list of square in 1 line

# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
squares2 = [i**2 for i in range(1,11)]
print(squares2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
negative2 = [-i for i in range(1,11)]
print(negative2)

names = ['yash', 'harsh', 'krish']
# new_names = []                        # should print 1st letter
# for name in names:
#     new_names.append(name[0])
# print(new_names)
new_names2 = [name[0] for name in names]
print(new_names2)


# Tutorial 129 & 130 - Exercise 1 & solution
# define a function that takes a list of strings
# output --> reverse of strings

lst = ['abc', 'tuv', 'xyz']
# old method
# def rev(l):
#     r = []
#     for i in l:
#         r.append(i[::-1])
#     return r
# print(rev(lst))

# LIST Comprehension
def rev2(l):
    return [i[::-1] for i in l]
print(rev2(lst))


# Tutorial 131 - List Comprehension with if statement
numbers = list(range(1,11))
print(numbers)

e_num = []
for i in numbers:
    if i % 2 == 0:
        e_num.append(i)
print(e_num)

e_num2 = [i for i in numbers if i % 2 == 0]
print(e_num2)

o_num = [i for i in range(1,11) if i % 2 != 0]
print(o_num)


# Tutorial 132 & 133 - Chapter 9 Exercise 2 & solution
# define a function
# input --> [True, False, [1,2,3], 1, 2.0, 3, 'yash']
# output --> ['1', '2.0', '3']

lst = [True, False, [1,2,3], 1, 2.0, 3, 'yash']
def num(l):
    return [str(n) for n in l if (type(n) == int or type(n) == float)]
print(num(lst))


# Tutorial 134 - List comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4,-3,8,-5,....]
new_list = []
for i in nums:
    if i % 2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

new_list2 = [i*2 if i % 2 == 0 else -i for i in nums]   # if using 'if else' use it before 'for'
print(new_list2)


# Tutorial 135 - Nested list comprehension
# example = [[1,2,3], [1,2,3], [1,2,3]]

nested_list = [[i for i in range(1,4)] for j in range(3)]
print(nested_list)


# Tutorial 136 - Chapter 9 Summary

