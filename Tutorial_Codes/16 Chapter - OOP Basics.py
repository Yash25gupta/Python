# Tutorial 183 - Object Oriented Programming Intro
# common topic in all popular Programming language(ptyhon, c++, java)
# with common idea but with different syntax
# OOP is just a style/way to write a code
# Very helpful in creating real life program

# class, object(instance), method

# list class        # in class we decide how /list/ object should be
# list object
# method

l1 = [1, 2, 3, 4]      # l1 is object
l2 = [3, 4, 5, 6]
l3 = ['yash', 'gupta']
l1.append(8)         # append() is method


# *****************************************************************************************
# Tutorial 184 - OOP Create Your First Class
# what is class?        --->    Class is a blueprint.
# how to create class.
# what is init method/constructor
# what are attribute, instance Variable
# how to create our object

class Person:           # convension --> 1st letter be Capital
    def __init__(self, first_name, last_name, age):
        # instance Variable
        print('init method called')
        self.first_name = first_name        # self represent object
        self.last_name = last_name
        self.p_age = age


p1 = Person('yash', 'gupta', 20)
p2 = Person('harsh', 'gupta', 10)

print(p1.first_name)
print(p1.p_age)
# print(p2.first_name)


# *****************************************************************************************
# Tutorial 185 & 186 - Exercise 1 & solution
# create a laptop class with attributes like brand name, model name, price
# create 2 object/instance of your laptop class

class Laptop2:
    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model = model
        self.price = price
        self.full_name = brand + ' ' + model


l1 = Laptop2('Lenovo', 'A30s', 25000)
l2 = Laptop2('HP', 'Pavalian 510', 45000)

print(l2.brand_name)
print(l1.model)
print(l1.full_name)


# *****************************************************************************************
# Tutorial 187 - OOP Instance Methods
l = [1, 2, 3]
# l.clear()
# list.clear(l)

# l.append(10)
# list.append(l, 10)
print(l)


class Person2:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18


p1 = Person2('yash', 'gupta', 20)
p2 = Person2('harsh', 'gupta', 17)
p3 = Person2('krish', 'gupta', 14)

print(p1.full_name())
print(Person2.full_name(p1))
print(p1.is_above_18())


# *****************************************************************************************
# Tutorial 188 & 189 - Exercise 2 & Solution
class Laptop1:
    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model = model
        self.price = price
        self.full_name = brand + ' ' + model

    def apply_discount(self, percent_discount):
        return (self.price - (self.price * percent_discount / 100))


l1 = Laptop1('Lenovo', 'A30s', 25000)
l2 = Laptop1('HP', 'Pavalian 510', 45000)

print(l1.apply_discount(15))
print(l2.apply_discount(20))


# *****************************************************************************************
# Tutorial 190 & 191 - Class Variable Part 1 & 2
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calc_circumference(self):
        return 2 * Circle.pi * self.radius


c1 = Circle(4)
c2 = Circle(5)
print(c1.calc_circumference())


class Laptop:
    discount_percent = 10

    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model = model
        self.price = price
        self.full_name = brand + ' ' + model

    def apply_discount(self):
        # self.discount_percent/Laptop.discount_percent
        # self is used when variable might be changed
        # Class name is used when variable cannot change
        return (self.price - (self.price * self.discount_percent / 100))


# Laptop.discount_percent = 0           # to turn off discount
l1 = Laptop('Lenovo', 'A30s', 45000)
l2 = Laptop('HP', 'Pavalian 510', 45000)
l2.discount_percent = 20            # to change %discount of perticular laptop
# print(l1.__dict__)
print(l1.apply_discount())
# print(l2.__dict__)
print(l2.apply_discount())
# print(l1.__dict__)
print(l1.apply_discount())


# *****************************************************************************************
# Tutorial 192 & 193 - Exercise 3 & Solution

class Person3:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person3.count_instance += 1


p1 = Person3('yash', 'gupta', 20)
p2 = Person3('harsh', 'gupta', 17)
p3 = Person3('krish', 'gupta', 14)

print(Person3.count_instance)


# *****************************************************************************************
# Tutorial 194 - OOP Class Methods
class Person4:
    count_instance = 0      # class variable / class attribute

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person4.count_instance += 1

    @classmethod
    def count_instances(cls):        # convension --> use cls to write class
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18


p1 = Person4('yash', 'gupta', 20)
p2 = Person4('harsh', 'gupta', 17)
p3 = Person4('krish', 'gupta', 14)

# Person4.method_name()     to use class method
print(Person4.count_instances())


# *****************************************************************************************
# Tutorial 195 - Class Method as a constructor
class Person5:
    count_instance = 0      # class variable / class attribute

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person5.count_instance += 1

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):        # convension --> use cls to write class
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18


p1 = Person5('yash', 'gupta', 20)
p3 = Person5.from_string('yash,gupta,20')
print(p3.full_name())


# *****************************************************************************************
# Tutorial 196 - OOP Static Method
class Person6:
    count_instance = 0      # class variable / class attribute

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person6.count_instance += 1

    @staticmethod
    def hello():
        print(f'hello static method called')

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):        # convension --> use cls to write class
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18


p1 = Person6('yash', 'gupta', 20)
Person6.hello()


# *****************************************************************************************
# Tutorial 197 - Encapsulation, Abstraction, Naming Convention, Name Mangling
# Encapsulation             -->     Write data and method near each other.
# Abstraction               -->     Hiding Complex programing from user
# Some special naming convention
# Name Mangling , __name(not a convension)

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        # can't use "__name". Python change it to "_{Cls name}__name"
        self.__price = price

    def make_a_call(self, phone_number):
        print(f'calling {phone_number} ...')

    def full_name(self):
        return f'{self.brand} {self._model}'


p1 = Phone('Mi', 'A1', 14000)
# print(p1.__price)
print(p1._Phone__price)
p1._Phone__price = 22222
print(p1._Phone__price)

# in Python every thing is public
# _name     # convention for private name
# __name__      # dunder/magic methods

# l = [3,4,1,2]
# l.sort()    # tim sort      code of sort() method is hidden from us. This is Abstraction.
# print(l)


# *****************************************************************************************
# Tutorial 198 - OOP Property and setter decorator
# we discuss 3 problem
# and solve them using getter, setter decorator

class Phone2:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)     # solve -ve price
        # self.complete_spec = f'{self.brand} {self.model} and price is {self._price}'

    @property       # now we can call method without '()'
    def complete_spec(self):
        return f'{self.brand} {self.model} and price is {self._price}'

    # getter() -->  @property , setter() -->
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f'calling {phone_number} ...')

    def full_name(self):
        return f'{self.brand} {self.model}'


p1 = Phone2('Nokia', '1100', 1500)
p1._price = 500
print(p1.complete_spec)     # does not change
p1.price = -500
print(p1.price)


# *****************************************************************************************
# Tutorial 199 - Inheritance Intro

class Phone3:       # base / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self._price = price

    def make_a_call(self, phone_number):
        return f'calling {phone_number} ...'

    def full_name(self):
        return f'{self.brand} {self._model}'


class Smartphone(Phone3):   # derived / child class
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        # two
        # Phone3.__init__(self, brand, model, price)      # uncommon way
        super().__init__(brand, model, price)           # 2nd way
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


phone = Phone3('Nokia', '1100', 1500)
smartphone = Smartphone('Oneplus', '6T', 36000, '6 GB', '128 GB', '48 MP')
print(phone.full_name())
print(smartphone.full_name())


# *****************************************************************************************
# Tutorial 200 - Multilevel inheritance, MRO, Method Overriding
# can we drive more than one class from base class?
# multilevel inheritance
# method resolving order        # order of finding methods
# method Overriding             # last method override upper class method
# isinstance(), issubclass()

class Keypad_phone:       # base / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self._price = price

    def make_a_call(self, phone_number):
        return f'calling {phone_number} ...'

    def full_name(self):
        return f'{self.brand} {self._model}'


class Smart_phone(Keypad_phone):   # derived / child class
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f'{self.brand} {self._model} and price is {self._price}'


class Flagship_phone(Smart_phone):
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f'{self.brand} {self._model} and price is {self._price} and camera is {self.rear_camera}'


phone = Keypad_phone('Nokia', '1100', 1500)
oneplus5 = Smart_phone('Oneplus', '5', 30000, '4 GB', '64 GB', '32 MP')
oneplus6t = Flagship_phone('Oneplus', '6T', 36000,
                           '6 GB', '128 GB', '48 MP', '24 MP')

# print(oneplus6t.full_name())
# print(help(Flagship_phone))

# isinstance()
# print(isinstance(oneplus5, Smart_phone))
# print(isinstance(oneplus5, Keypad_phone))
# print(isinstance(oneplus5, Flagship_phone))

# print(isinstance(oneplus6t, Flagship_phone))
# print(isinstance(oneplus6t, Smart_phone))
# print(isinstance(oneplus6t, Keypad_phone))

# issubclass()
print(issubclass(Smart_phone, Keypad_phone))
print(issubclass(Keypad_phone, Smart_phone))


# *****************************************************************************************
# Tutorial 201 - Multiple Inheritance
# most person avoid Multiple inheritance

class A:

    def class_a_method(self):
        return "I'm just a Class A method."

    def hello(self):
        return "Hello from class A"


class B:

    def class_b_method(self):
        return "I'm just a Class B method."

    def hello(self):
        return "Hello from class B"


class C(B, A):
    pass


instance_c = C()

# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
print(help(C))
print(C.mro())
print(C.__mro__)


# *****************************************************************************************
# Tutorial 202 - Special magic(dunder) method, operator overloading, polymorphism

class Phone4:       # base / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price

    def make_a_call(self, phone_number):
        return f'calling {phone_number} ...'

    def full_name(self):
        return f'{self.brand} {self.model}'

    # str, repr
    def __str__(self):      # for normal user
        return f'{self.brand} {self.model} and price is {self._price}'

    def __repr__(self):     # for developers to use as Debuging purpose
        return f"Phone4('{self.brand}', '{self.model}', {self._price})"

    def __len__(self):
        return len(self.full_name())

    def __add__(self, other):       # operator overloading
        return self._price + other._price


class Smartphone3(Phone4):
    def __init__(self, brand, model, price, rear_camera):
        super().__init__(brand, model, price)
        self.rear_camera = rear_camera

    def full_name(self):
        return f'{self.brand} {self.model} and price is {self._price}'


# l = [1,2,3]
# print(l)
p = Phone4('mi', 'A1', 10000)
p2 = Phone4('samsung', 'm30s', 16000)
s = Smartphone3('oneplus', '5t', 30000, '20 MP')

# print(len(p))
# print(p)    # print __str__function
# print(str(p))
# print(repr(p))
# print(p.__str__())
# print(p.__repr__())
# print(p+p2)

print(s.full_name())
print(p.full_name())
