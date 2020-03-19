# Tutorial 177 - Intro to generators
# generator are iterators

l = [1,2,3]                 # iterable
# for i in l:
#     print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

m = map(lambda a: a**2, l)      # iterator
# for i in m:
#     print(i)

# memory   ----   [................]    # list
# memory   ----   (.)                   # generator

# if we have to use our sequence only once , we use generator
# if we have to use our sequence again and again , we use list


# *****************************************************************************************
# Tutorial 178 - Generator example
# create your 1st generator with generator function
# 1.) generator function
# 2.) generator comprehension

# 10, 1 to 10
def nums(n):
    for i in range(1,n+1):
        # print(i)
        yield i

# for num in nums(10):        # this can be run many times b/c func is calling here
#     print(num)
# memory ------>  3

numbers = nums(10)

for i in numbers:           # ONLY PRINT 1 TIME
    print(i)

for i in numbers:
    print(i)


# *****************************************************************************************
# Tutorial 179 & 180 - Exercise 1 & solution
# define a generator function
# takes 1 argument
# generate a sequence of even numbers from 1 to that number

def e_num(n):
    # for i in range(1, n+1):
    #     if i % 2 == 0:
    #         yield i
    for i in range(2, n+1, 2):
        yield i

e = e_num(20)
for i in e:
    print(i)


# *****************************************************************************************
# Tutorial 181 - Generator Comprehension
square_list = [i**2 for i in range(1,11)]
print(square_list)

square_generator = (i**2 for i in range(1,11))
print(next(square_generator))
print(next(square_generator))
print(next(square_generator))
# for i in square_generator:      # print only once
#     print(i)


# *****************************************************************************************
# Tutorial 182 - List vs Generators
# memory usage, time
# when to use list, and when to use generator
import time

t1 = time.time()
l = [i**2 for i in range(10000000)]     # 1 Crore
print(f'Time taken to process list = {time.time()-t1} sec')
# 766-450 MB
# time = 3.09 sec

t2 = time.time()
g = (i**2 for i in range(10000000))     # 1 Crore
print(f'Time taken to process generator = {time.time()-t2} sec')
# # 764-448 MB
# time = 0.0 sec

