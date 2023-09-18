# A number is spy number if the sum and product of its digits are equal.
# Eg -> 123 is spy no
# (1+2+3) = (1*2*3)


def checkSpy(number):
    number = str(number)
    multi = 1
    total = 0
    for i in number:
        multi *= int(i)
        total += int(i)
    return multi == total


print(checkSpy(123))
