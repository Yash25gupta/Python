# Find no of "1" in a binary of a number
# Input -> 124	(1111100)
# Output -> No. of 1's = 5


def decToBin(num):
    """ This function takes a "int" as input and return its binary in "int" form."""
    output = []
    while num > 0:
        i = num % 2
        num = num // 2
        output.insert(0, str(i))
    return int("".join(output))


def myCount(valueToCount, countFrom):
    """ Params: int-valueToCount\n            int-countFrom
    It will return the count of that number. """
    return str(countFrom).count(str(valueToCount))


print(myCount(1, decToBin(124)))

#  or

print(bin(124).count("1"))
