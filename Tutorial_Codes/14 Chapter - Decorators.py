# Tutorial 165 - Chapter 14 Intro
# you have to have a complete understanding of functions, 
# first class function / Closures
# then finally we will learn about decorators

def square(a):
    return a**2
s = square
print(s.__name__)
print(square.__name__)
print(s)
print(square)

# *****************************************************************************************
# Tutorial 166 - Pass function as argument
# map
def square2(a):
    return a**2

l = [1,2,3,4]

# print(list(map(square2, l)))
print(list(map(lambda a : a**2, l)))        # giving map object

def my_map(func, l):
    map_list = []
    for item in l:
        map_list.append(func(item))
    return map_list

def my_map2(func, l):
    return [func(item) for item in l]

# print(my_map(square2, l))
print(my_map2(lambda a : a**2, l))           # giving list

# *****************************************************************************************
# Tutorial 167 - Function returning function

def outer_func():
    def inner_func():
        print('inside inner function')
    return inner_func

# out = outer_func()
# out()

def outer_func2(msg):
    def inner_func2():
        print(f'message is {msg}')
    return inner_func2

var = outer_func2('yash')
var()

# *****************************************************************************************
# Tutorial 168 - Closures Practice
# function returning function

def to_power(n):
    def calc_power(x):
        return x**n
    return calc_power

cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(5))

# *****************************************************************************************
# Tutorial 169 - Decorators Intro
# decorators - enhance the functionality of other function
# @ use for decorator

# this is awesom function

def decorator_func(any_func):
    def wrapper_func():
        print('this is awesom function')
        any_func()
    return wrapper_func

@decorator_func                         # shortcut
def func1():
    print('this is function 1')

@decorator_func
def func2():
    print('this is function 2')

# func1 = decorator_func(func1)             # var --> func1 we can use any name
# func1()
func2()

# *****************************************************************************************
# Tutorial 170 - Decorators Part 2
def decorator_func2(any_func):
    def wrapper_func2(*args, **kwargs):
        print('this is awesom function')
        return any_func(*args, **kwargs)
    return wrapper_func2

@decorator_func2
def func(a):
    print(f'this is a function with argument {a}')

func(7)

@decorator_func2
def add(a, b):
    return a+b

print(add(2,3))

# *****************************************************************************************
# Tutorial 171 - Decorators part 3
from functools import wraps
def decorator_func3(any_func):
    @wraps(any_func)
    def wrapper_func3(*args, **kwargs):
        ''' this is wrapper function '''
        print('this is awesom function')
        return any_func(*args, **kwargs)
    return wrapper_func3

@decorator_func3
def add2(a, b):
    ''' this is add function '''
    return a+b

print(add2.__doc__)

# *****************************************************************************************
# Tutorial 172 - Decorators Practice
from functools import wraps
# Make a decorator function which return output as --> 
# output should be -->
# you are calling 'add3' function
# This function takes two numbers as arguments and return their sum.
# 9

def print_func_data(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        '''This is Wrapper Function.'''
        print(f'You are calling {func.__name__} Function.')
        print(func.__doc__)
        return func(*args, **kwargs)
    return wrapper_function

@print_func_data
def add3(a,b):
    '''This function takes two numbers as arguments and return their sum.'''
    return a+b

print(add3(4,5))

# *****************************************************************************************
# Tutorial 173 & 174 - Exercise 1 & solution
# define decorator function which shows the time taken by a function to run.
# output    --->   this function took 3 sec to run
import time
from functools import wraps

def calculate_time(function):
    @wraps(function)
    def wrapper_function2(*args, **kwargs):
        print(f'Exicuting ...... {function.__name__}')
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        for num, squ in enumerate(returned_value):
            print(f'{num + 1} --> {squ}')
        t2 = time.time()
        print(f'This function took {t2-t1} sec to run.')
        return returned_value
    return wrapper_function2

@calculate_time
def square_list(a):
    return [i**2 for i in range(1, a+1)]

square_list(1000)

# *****************************************************************************************
# Tutorial 175 - Decorators Practice 2
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper1(*args, **kwargs):
        # data_type = []
        # for arg in args:
        #     data_type.append(type(arg) == int)
        # if all(data_type):
        #     return function(*args, **kwargs)
        # else:
        #     return 'Invalid Arguments are passed'
        return function(*args, **kwargs) if all([type(arg) == int for arg in args]) else 'Invalid Arguments'
    return wrapper1

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5))

# *****************************************************************************************
# Tutorial 176 - Decorators with arguments
from functools import wraps

def only_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper2(*args, **kwargs):
            return function(*args, **kwargs) if all([type(arg) == data_type for arg in args]) else 'Invalid Arguments'
        return wrapper2
    return decorator

@only_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('yash', 'gupta', 'is', 'my', 'name', 12))

