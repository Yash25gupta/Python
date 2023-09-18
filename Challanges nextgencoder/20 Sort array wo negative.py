# A Program which will take 1 array of numbers as input and
# sorts number in ascending order but -ve number does not change its position.
#               TEST CASES:
#         INPUT                     OUTPUT
#   [4,7,0,2,4,6,3]             [0,2,3,4,4,6,7]
#   [7,-10,5,-34,-81,1,5]       [1,-10,5,-34,-81,5,7]
#   [-4,-7,0,-2,-4,-6,-3]       [-4,-7,0,-2,-4,-6,-3]


def sortPositive1(lst):
    for _ in range(len(lst)):
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
    output = [i if i < 0 else '' for i in lst]
    for i in lst:
        if i >= 0: output[output.index('')] = i
    return output


def sortPositive(lst, n=0):
    flag = False
    for i in range(1, (len(lst) - n)):
        if lst[i - 1] > lst[i]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            flag = True
    if flag: sortPositive(lst, n + 1)
    output = [i if i < 0 else '' for i in lst]
    for i in lst:
        if i >= 0: output[output.index('')] = i
    return output


# or

def sortPositive2(lst):
    nums = sorted([i for i in lst if i >= 0])
    j = 0
    for i in range(len(lst)):
        if lst[i] >= 0:
            lst[i] = nums[j]
            j += 1
    return lst


l1 = [4, 7, 0, 2, 4, 6, 3]
l2 = [7, -10, 5, -34, -81, 1, 5]
l3 = [-4, -7, 0, -2, -4, -6, -3]
print(sortPositive(l1))
print(sortPositive1(l2))
print(sortPositive2(l3))
