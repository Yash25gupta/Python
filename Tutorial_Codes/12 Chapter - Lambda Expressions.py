# Tutorial 150 - Lambda Expression
# anonymous function
def add(a,b):
    return a+b

add2 = lambda a,b : a+b
print(add2(2,3))

multiply = lambda a,b : a*b
print(multiply(2,3))

print(add)
print(add2)
print(multiply)


# Tutorial 151 - Lambda Expression Practice
def is_even(a):
    return a % 2 ==0
print(is_even(5))

iseven2 = lambda a : a % 2 == 0
print(iseven2(6))

def lastchar(s):
    return s[-1]
print(lastchar('yash'))

lastchar2 = lambda s : s[-1]
print(lastchar2('yash'))

# lambda with if else
def func(s):
    if len(s) > 5:
        return True
    return False
func2 = lambda s : True if len(s) > 5 else False
func3 = lambda s : len(s) > 5

print(func('yashg'))
print(func2('yashgup'))
print(func3('yasg'))

