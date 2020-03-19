# Tutorial 70 - Functions Intro
# name = "yashgupta"
# print(len(name))        # len is a function

def add_two(a,b):
    return a+b
# print(add_two(50,4))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(add_two(num1,num2))

txt1 = input("Enter first name : ")
txt2 = input("Enter second name : ")
print(add_two(txt1,txt2))


# Tutorial 71 - Print vs Return
def add_three(a,b,c):
    return a+b+c                # will return a+b+c
print(add_three(1,2,3))         # then we print it

def add_three2(a,b,c):
    print(a+b+c)                # function will print
add_three(1,2,3)                # no need to print after calling function


# Tutorial 72 - Function practice

# def last_letter(text):
#     return text[-1]
# name = input("Enter a name : ")
# print(f"Last letter is '{last_letter(name)}'.")

# def odd_even(number):               # Long Method
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# def odd_even(number):               # Short Method
#     if number % 2 == 0:
#         return "Even"
#     return "Odd"


# def is_even(number):                # Short boolian Method
#     if number % 2 == 0:
#         return True
#     return False


def is_even(number):                  # Shortest Method
    return number % 2 == 0

num = int(input("Enter a number : "))
print(is_even(num))


# Tutorial 73 & 74 - Exercise 1 solution
def greater1(a,b):
    if a > b:
        return a
    return b

n1 = int(input("Enter a number : "))
n2 = int(input("Enter another number : "))
print(f"Greater number is {greater1(n1,n2)}.")


# Tutorial 75 - Define greatest
def greatest1(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
print(f"{greatest1(n1,n2,n3)} is greatest number.")


# Tutorial 76 - Function inside function
def greater2(a,b):
    if a > b:
        return a
    return b

def greatest2(a,b,c):
    return greater2(greater2(a,b),c)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
print(f"{greatest2(n1,n2,n3)} is greatest number.")


# Tutorial 77 & 78 - Exercise 2 solution
# palindrome --> word that reads same backward as forward
# Define a function that take a word and return if it is palindrome or not

def is_palindrome(txt):
    return txt == txt[::-1]

word = input("Enter a palindrome word : ")
print(is_palindrome(word))


# Tutorial 79 - Fibonacci series program
# 0 1 1 2 3 5 8 13 21 34 ....
# print("htrtyu", end = " ")      # Dont go to next line

def fibonacci_series(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a, b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")

fibonacci_series(10)


# Tutorial 80 - Default Parameters
# Default parameter should be given at last.
def user_info(first_name, last_name = 'Unknown', age = None):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info('yash')


# Tutorial 81 - Variable Scope
# Local variable cannot be used inside outside its function(group)
x = 5               # Global variable
def func():
    global x
    x = 7           # Local Variable
    return x

print(x)            # print 5
print(func())       # print 7
print(x)            # print 5 if "global x" is not used

