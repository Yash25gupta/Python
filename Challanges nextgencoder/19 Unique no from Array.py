# A Program which will take 1 array of numbers as input and
# gives array of integer with unique integer as output.
#               TEST CASES:
#         INPUT              OUTPUT
#   [1,9,8,2,7,3,2,3,1]     [9,8,7]
#   [1,2,3,4,5,6]           [1,2,3,4,5,6]
#   [1,2,4,2,4,1]           []


def uniqueArray(lst):
    return [i for i in lst if lst.count(i) == 1]


l1 = [1, 9, 8, 2, 7, 3, 2, 3, 1]
l2 = [1, 2, 3, 4, 5, 6]
l3 = [1, 2, 4, 2, 4, 1]
print(uniqueArray(l1))
print(uniqueArray(l2))
print(uniqueArray(l3))
