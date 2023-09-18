# A program which will take one number as input and splits it into parts
# Foe Eg -> 20 = [5 5 5 5] or [3 2 5 8 2]
# and Output parts which creates biggest product of the imputed number 20 = [4 4 4 4 4]
# input -> 0 < num < 99
# output -> 0 < length of list < 6
#       TEST CASES:
#   INPUT        OUTPUT
#    25         5 5 5 5 5
#    32         7 7 6 6 6
#    -1         Error
#    6          3 3
#    1          1
#    0          0


def biggestProduct(num):
    if not 4 < num < 100: return num if num > -1 else 'Error'
    n = 2 if num < 8 else (3 if num < 10 else 5)
    out = [(num // n) for _ in range(n)]
    if sum(out) == num: return out
    for i in range(num - sum(out)):
        out[i] += 1
    return out


nList = [25, 32, -1, 0, 1, 5, 6, 7, 8, 9, 10, 12]
for i in nList:
    print(biggestProduct(i))
