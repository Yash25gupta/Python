# Perfect number is ifit is equal to sum of its proper divisors
# Eg -> (1+2+3) = 6


def checkProper(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


print(checkProper(6))
