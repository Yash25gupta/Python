# Tutorial 17 - String Concatenation
first_name="Yash"
last_name='Gupta'
print(first_name + " " + last_name)
# print(first_name + 3)     Can't add integer with string
print(first_name + "3")     # Right
print(first_name + str(3))  # Right
print(first_name * 3)       # Will print first_name 3 times


# Tutorial 18 - User Input
# This always take input as "String"
name=input("Enter your name: ")
print("hello " + name)
age=input("Enter your age: ")   # "25", not 25
print("Your age is " + age)


# Tutorial 19 - Int() function
num1=input("Enter first number ")   # "4"
num2=input("Enter second number ")  # "4"
# total = num1 + num2      this gives      44 instead of 4+4=8
total = int(num1) + int(num2)
print("Sum of two number = " + str(total))
# str          4   ---> "4"
# int         "4"  --->  4
# float       "4"  --->  4.0


# Tutorial 20 - More about variables
name,age = "Yash Gupta", "25"             # Can give 2 variable in 1 line
print("Hello " + name + ". Your age is " + age)
x=y=z=1       # Assign more than one variable in 1 line
print(y)


# Tutorial 21 - Two or more input in one line
name, age = input("Enter your name and age ").split()           # Seperate 2 variable with space " "
print(name + "\n" + age)
name, age = input("Enter your name and age seperated by \",\" ").split(",")        # Seperate 2 variable with comma ","
print("Your name is " + name + " And your age is "  + age)


# Tutorial 22 - String formatting
name = "Yash"
age = 24
print("Hello " + name + " your age is " + str(age))         # Ugly Syntax
print("Hello {} your age is {} ".format(name, age + 2))     # python 3 Syntax
print(f"Hello {name} your age is {age + 4} ")               # python 3.6 Syntax (Best)


# Tutorial 23 & 24 - Exercise 1 & solution
# Ask user to input 3 number and print average of 3 numbers using string formating.
# Bonus - Take 3 input in 1 line
num1, num2, num3 = input("Enter 3 numbers seperated by \",\" ").split(",")
print(f"Average of given 3 numbers is {(int(num1) + int(num2) + int(num3))/3}.")


# Tutorial 25 - String Indexing
lang= "Python"
# index number (Position)
# p = 0 , -6
# y = 1 , -5
# t = 2 , -4
# h = 3 , -3
# o = 4 , -2
# n = 5 , -1

print(lang[3])      # print "h"


# Tutorial 26 - String Slicing
lang = "python"
# syntax - [start argument : stop argument-1 ]
print(lang[2:4])        # th
print(lang[-3:6])       # hon


# Tutorial 27 - Step Argument
lang = "python"
# syntax - [start argument : stop argument-1 : step ]
print("yashgupta"[1:5:1])   # ashg
print("yashgupta"[1:5:2])   # ah
print("yashgupta"[::2])     # ysgpa (if argument is not given --> 0 to end)
print("yashgupta"[3::-1])   # hsay
print("Yashgupta"[::-1])    # atpughsay
print("Yashgupta"[-1::-1])  # atpughsay


# Tutorial 28 & 29 - Exercise 2 & solution
# Ask user to input name and print back in reverse order
name = input("Enter your name ")
print(f"Your name in reverse order is \"{name[-1::-1]}\"")


# Tutorial 30 - String Methods Part 1
name = "yAsh GuPTa"
# 1. len() function
print(len(name))

# 2. lower() method
print(name.lower())

# 3. upper() method
print(name.upper())

# 4. title() method
print(name.title())

# 5. count() method
print(name.count("a"))


# Tutorial 31 & 32 - Exercise 3 & solution
# take 2 comma seperated input from user
# 1. name
# 2. a single character
# Output: 
# 1. Name Length
# 2. count the character that user inputed (bonus- case insensitive)
name, char = input("Enter your name and a character seperated by \",\": ").split(",")
print(f"Length of your name is {len(name)}")
print(f"Letter \"{char}\" appears {name.lower().count(char.lower())} times in {name}.")

# Ignore extra spaces
print(f"Length of your name is {len(name.strip())}")
print(f"Letter \"{char.strip()}\" appears {name.strip().lower().count(char.strip().lower())} times in {name.strip()}.")


# Tutorial 33 - Solve problem with spaces using strip method
# lstrip, rstrip, strip  method     
name = "   Ya  sh       "
dots = ".........."
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots) 
print(name.strip() + dots)          # Does not remove spaces in between
print(name.replace(" ","") + dots)


# Tutorial 34 - Find and Replace Method
string = "This is a Sentence."
print(string.replace(" ","_",2))        # Replaces 2 spaces
is1 = string.find("is")
is2 = string.find("is",is1 + 1)         # Start after position of 1st is
print(is2)


# Tutorial 35 - Center Method
name = input("Enter your name: ")
print(name.center(len(name) + 8,"*"))


# Tutorial 36 - Strings are Immutable
string = "String"
new_string = string.replace("t","T")
print(f"Old string: {string}")
print(f"New string: {new_string}")


# Tutorial 37 - Assignment Operators
name = "yash"
name += "gupta"   # name = name + "gupta"
print(name)
age = 25
age *= 2          # age = age * 2
print(age)


# Tutorial 38 - Chapter 2 Summary
