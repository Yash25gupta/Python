# Tutorial 39 - If statement
age = input("Enter your age : ")
age = int(age)
if age>=18:
    print("You are above 18")


# Tutorial 40 - Pass statement
age = 14
if age>=14:
    pass        # If want to do nothing, use "pass"


# Tutorial 41 - If-else statement
age = input("Enter your age : ")
age = int(age)
if age>=18:
    print("You are above 18")
else:
    print("Sorry!! You are under 18")


# Tutorial 42 & 43 - Nested If-else, Exercise 1 and solution
# NUMBER_GESSING_GAME
# Make a variable and assign any number to it
# ask user to guess a number
# if guess correctly, Print "You Win!!!"
# else print "too low" or "too high" accordlingly.
actual_num = 57
user_num = input("Guess a number : ")
user_num = int(user_num)
if user_num == actual_num:
    print("You win!!!!")
else:
    if user_num > actual_num:
        print("Too High")
    else:
        print("Too Low")


# Tutorial 44 - And, Or Operator
name = 'Yash'
age = 19
if name == "Yash" and age == 19:
    print("True")
else:
    print("False")
if name == "Yah" or age == 19:
    print("True")
else:
    print("False")


# Tutorial 45 & 46 - Exercise 2 and solution
# ask user's name and age
# if name start with 'a' or 'A' and age is above 18 then
# print 'You can Watch COCO Movie' else
# print 'Sorry! You can't watch this movie'
name, age = input("Enter your name and age (comma seperated) : ").split(",")
age = int(age)
if age >= 18 and (name[0] == 'a' or name[0] == 'A'):
    print("You can Watch COCO Movie")
else:
    print("Sorry! You can't watch this movie")


# Tutorial 47 - If-elif-else statement
age = input("Enter your age : ")
age = int(age)
if age<=0:
    print("You cannot Watch")
elif 0 <age<=3:
    print("Free Ticket")
elif 4<age<=10:
    print("Ticket Price : 150")
elif 11<age<=60:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")


# Tutorial 48 - in keyword
name = "Yash"
if 'a' in name:
    print(f"a is present in {name}")
else:
    print(f"a is not present in {name}")


# Tutorial 49 - Check Empty or Not
name = "abc"
if name:            # Check if "name" variable is empty or not
    print("String is not empty")
else:
    print("String is empty")


# Tutorial 50 - While Loop
# print("Hello World")    # 10 times
i = 1
while i <= 10:
    print(f"Hello World {i}")
    i += 1


# Tutorial 51 - Sum of Numbers Program using while loop
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)


# Tutorial 52 & 53 - Exercise 3 and solution
# Sum of n Natural Numbers
n = input("Enter a Number : ")
n = int(n)
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(f"Sum of first {n} Natural Numbers is \"{total}\".")


# Tutorial 54 & 55 - Exercise 4 and solution
# Ask user to input a number containing more than 1 digit (Eg - 124)
# Calculate 1+2+4
num = input("Enter a number containing more than 1 digit : ")
i = 0
total = 0
while i < len(num):
    total += int(num[i])
    i += 1
print(f"Sum of all digits is '{total}'.")


# Tutorial 56 & 57 - Exercise 5 and solution
# Ask for Name
# print count of each letter
# Output : a = 2, y = 1, etc
name = input("Enter your name : ")      # yash gupta
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"\t{name[i]} : {name.count(name[i])}")
    i += 1


# Tutorial 58 - Infinite loop
# To stop Infinite Loop use (Ctrl+C)


# Tutorial 59 - For loop
for i in range(10):             # i --> 0 to 9
    print(f"Hello World {i}")
for i in range(1,11):           # i --> 1 to 10
    print(f"Hello World {i}")


# Tutorial 60 - For loop example 1
# Sum from 1 to n
n = int(input("Enter a number : "))
total = 0
for i in range(1,n+1):
    total += i
print(f"Sum of {n} natural number is {total}.")


# Tutorial 61 - Example 2 For loop
# ask user a multidigit number
# calculate sum of digits using for loop
num = input("Enter a number : ")
total = 0
for i in range(len(num)):
    total += int(num[i])
print(f"Sum = {total}")


# Tutorial 62 - Example 3 For loop
# Ask for Name
# print count of each letter using for loop
# Output : a = 2, y = 1, etc
name = input("Enter your name : ")      # yash gupta
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"\t{name[i]} : {name.count(name[i])}")


# Tutorial 63 - Break and Continue keyword
for i in range(1,11):
    if i == 5:
        break           # will print 1,2,3,4
    print(i)
for i in range(1,11):
    if i == 5:
        continue        # will print 1,2,3,4,6,7,8,9,10
    print(i)


# Tutorial 64 & 65 - Exercise 6 modify number guessing game and solution
import random
actual_num = random.randint(1,100)
user_num = int(input("Guess a number between 0 to 100 : "))
guess_times = 1
while True:
    if user_num == actual_num:
        print(f"You won, and you guessed this number in {guess_times} times.")
        break
    elif user_num > actual_num:
        print("Too High")
        user_num = int(input("Guess again : "))
        guess_times += 1
    else:
        print("Too Low")
        user_num = int(input("Guess again : "))
        guess_times += 1


# Tutorial 66 - DRY principle of coding
# Dont repeat yourself
import random
actual_num = random.randint(1,100)
user_num = int(input("Guess a number between 0 to 100 : "))
guess_times = 1
game_over = False
while not game_over:
    if user_num == actual_num:
        print(f"You won, and you guessed this number in {guess_times} times.")
        game_over = True
    elif user_num > actual_num:
        print("Too High")
    else:
        print("Too Low")
    user_num = int(input("Guess again : "))
    guess_times += 1


# Tutorial 67 - Step argument in range function
for i in range(1,11,2):     # 1,3,5,7,9
    print(i)
for i in range(10,0,-1):    # 10,9,8,7,6,5,4,3,2,1
    print(i)


# Tutorial 68 - For loop and string
name = "yashgupta"
# Old Method
for i in range(len(name)):
    print(name[i])

# Python Method
for i in name:
    print(i)

num = input("Enter a number: ")
total = 0
for i in num:
    total += int(i)
print(total)


# Tutorial 69 - Chapter 3 Summary
