# Tutorial 140 - Intro to *args
def add_two(a,b):
    return a+b
print(add_two(5,6))

# '*args' passes many parameters in a function
# "args" return tuple <<<<<<<<<-----------

def total(*args):       
    t = 0
    for i in args:
        t += i
    return t
print(total(1,2,3,4,5))         # now we can pass many argments


# Tutorial 141 - *args with normal parameter
def multiply(num, *args):       
    m = 1
    print(num)
    print(args)
    for i in args:
        m *= i
    return m

print(multiply(2,3,4,5))        # now we have to pass minimum of 1 parameter


# Tutorial 142 - Args as argument
def multiply2(*args):       
    m = 1
    for i in args:
        m *= i
    return m

nums = [2,3,4]
print(multiply2(*nums))          # * is used to pass list/tuple as individual item (unpack)


# Tutorial 143 & 144 - Exercise 1 & solution
def power(p,*args):
    if args:
        return [num**p for num in args]
    else:
        return 'You didnt pass any args'

lst = [1,2,3,4,5]
print(power(3,*lst))


# Tutorial 145 - **Kwargs
# double star operator
# generates dictionary <<<<<<<---------
def func(**kwargs):
    # print(kwargs)
    for k,v in kwargs.items():
        print(f'{k} : {v}')

func(first_name = 'Yash', last_name = 'Gupta')

# dictionary unpacking
d = {'name' : 'Yash', 'age' : 20}
func(**d)


# Tutorial 146 - Function with all type of parameters
# PADK   <<<<------- Order
# parameters, args, default parameters, kwargs

def funcn(name, *args, last_name = 'Unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

funcn('yash', 1, 2, 3, 4, last_name='gupta', age = 20, height = 5.10)


# Tutorial 147 & 148 - Exercise 2 & Solution
def func1(lst, reverse_str=False):      # Simple method
    new_list = []
    for name in lst:
        if reverse_str:
            new_list.append(name[::-1].title())
        else:
            new_list.append(name.title())
    return new_list

def func2(lst, reverse_str=False):      # Default Parameter
    return [name[::-1].title() if reverse_str else name.title() for name in lst]

def func3(lst,**kwargs):                # **kwargs
    return [name[::-1].title() if kwargs.get('reverse_str') else name.title() for name in lst]

names = ['yash', 'gupta']
print(func1(names))
print(func1(names, True))
print(func2(names))
print(func2(names, reverse_str = True))
print(func3(names))
print(func3(names, reverse_str = True))


# Tutorial 149 - Chapter 11 summary

