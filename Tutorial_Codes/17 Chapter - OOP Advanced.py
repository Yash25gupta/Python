# Self
class Enemy(object):
    # instances = []      # e0, e1, ....
    def __init__(self, x):
        # self.__class__.instances.append(self)
        self.x = x
    def show(self):
        print(f'hi {self.x}')

# Create multiple instances of a class
n = 5   # Numbers of enemy
enemys = {f'e{i}': Enemy(50 + i) for i in range(n)} # e0, e1, ....

# Preform anything you want on all instances of a class
# for instance in Enemy.instances:
#     instance.move()
for enemy in enemys:
    print(enemy, enemys[enemy])
    enemys[enemy].show()


# *****************************************************************************************
# Self2
class Enemy2(object):
    def __init__(self, x):
        self.x = x
    def move(self):
        self.x += self.dx

# Create multiple instances of a class
n = 5   # Numbers of enemy
enemys = [Enemy2(50) for i in range(n)]

# Preform anything you want on all instances of a class
for enemy in enemys:
    enemy.y = 2000


# *****************************************************************************************
# Tutorial 203 - Chapter 17 intro and built in errors
# excetion, how to handle them
# raise our own error, debuging,etc

# # syntax error
# def func:       # () absent error
#     pass

# # IndentationError
# def func():
#     print('hi')
#    print('yash')

# # NameError
# print(var)

# # TypeError
# print(5 + 'ya')

# # IndexError
# l = [1,2,3]
# print(l[4])

# # ValueError
# s = '5ww'
# print(int(s))

# # AttributeError
# l = [1,2,3]
# l.push('12')      # push dont exist

# # KeyError
# d = {'name' : 'yash'}
# print(d['age'])


# *****************************************************************************************
# Tutorial 204 - Raise errors
def add(a,b):
    if type(a) == int and type(b) is int:
        return a+b
    raise TypeError('OOPs you are passing wrong data type to function')

print(add('2','3'))


# *****************************************************************************************
# Tutorial 205 - Error raise example 1
# NotImplementedError       # used when we use inheritance
# abstract method       # this is from Java, not from python

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('You have to define this method in subclasses')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

doggy = Dog('bonny', 'pug')
print(doggy.sound())


# *****************************************************************************************
# Tutorial 206 - Error raise example 2

class Mobile:
    def __init__(self, name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be oject of Mobile class')
    
oneplus = Mobile('OnePlus 6')
samsung = 'Samsung galaxy grand 2'
mobstore = MobileStore()
# mobstore.add_mobile(samsung)
mobstore.add_mobile(oneplus)
mob_phones = mobstore.mobiles
print(mob_phones[0].name)


# *****************************************************************************************
# Tutorial 207 - Try, Except exception handling
# Exception     # those errors which comes on the time of Execution
# try except

while True:
    try:
        age = int(input('Enter your age : '))       # seven # 7
        break
    except ValueError:
        print('invalid input. Please enter age in numbers')
    except:
        print('unexpected error ..')

if age < 18:
    print('You can\'t play this game.')
else:
    print('You can play this game.')


# *****************************************************************************************
# Tutorial 208 - Else finally with try except

while True:
    try:
        number = int(input('Enter a number : '))
    except ValueError:
        print('You did\'t entered integer')
    except:
        print('unexpected error ..')
    else:           # Run after try.
        print(f'User input = {number}')
        break
    finally:        # This will run always.
        print('finlly block.........')


# *****************************************************************************************
# Tutorial 209 & 210 - exercise 1 & solution
# make a function 'divide'
# divide(a,b)

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        return err      # will return default msg.
    except TypeError:
        return 'Please enter numbers only.'
    except:
        return 'Unexpected Error !!!'
    
print(divide(4,2))      # 2
print(divide(4,0))      # Please don't divide by zero, zero division error
print(divide('4',2))    # please input numbers only


# *****************************************************************************************
# Tutorial 211 - Custom Exception
# Q - Why custom exception?
# A - To increase the readability of code.

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('Name is too short.')

username = input('Enter your name : ')
validate(username)
print(f'Hello {username}')


# *****************************************************************************************
# Tutorial 212 - Python Debugger
import pdb  # import pbd module
''' module - python files contain useful classes and functions wrote
by developers.

According to wikipedia - Debuging is the process of finding and resolving
defects or problems within a computer program that prevents correct operation
of computer software or a system.

Why debugging?
1.) our program is not and causing unexpected errors.
2.) our program is working fine but not working the same way we want.

Steps for debugging
1.) set trace
2.) execute code line by line'''

pdb.set_trace()
# l     # show code line
# n     # execute 1 line of code
# c     # continue to run code
# q     # quit debuging
name = input('Please type your name : ')
age = input('Please type your age : ')
print(f'hello {name}. Your age is {age}.')
age2 = int(age) + 5
print(f'{name} you will be {age2} in next five years.')

