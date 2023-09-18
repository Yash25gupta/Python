# A program which will take 1 array of numbers as input and
# Display a sorted array as per their Occurance
#               TEST CASES:
#       INPUT               OUTPUT
# [1,2,4,3,3,5,2,2] - [2,2,2,3,3,1,4,5]
# [1,2,4,3,3,5,5,2] - [3,3,5,5,2,2,1,4]
# [5,4,4,5,3,2,5,5] - [5,5,5,5,4,4,3,2]


def sortOccurance(lst):
    return sorted(sorted(lst), key=lst.count, reverse=True)


l1 = [1, 2, 4, 3, 3, 5, 2, 2]
l2 = [1, 2, 4, 3, 3, 5, 5, 2]
l3 = [5, 4, 4, 5, 3, 2, 5, 5]
print(sortOccurance(l1))
print(sortOccurance(l2))
print(sortOccurance(l3))
