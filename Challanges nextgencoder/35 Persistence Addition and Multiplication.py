from math import prod


def persistenceAdd(num):
    return persistenceAdd(sum([int(i) for i in str(num)])) if num > 9 else num


def persistenceMul(num):
    return persistenceMul(prod([int(i) for i in str(num)])) if num > 9 else num


print(persistenceAdd(8316962))
print(persistenceMul(8316962))
