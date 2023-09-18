def swappedList(lst, n):
    slst = sorted(lst)
    swaps = [i for i in range(len(lst)) if lst[i] != slst[i]]
    if len(swaps) != 2 or n not in lst or lst.index(n) not in swaps: return 'Not Swapped', ''
    return 'Swapped', slst


l = ([1, 4, 2, 5], [1, 4, 2, 5], [6, 2, 3, 1, 7, 8], [4, 7, 2, 3])
nn = (2, 5, 6, 4)
for i, j in zip(l, nn):
    a, b = swappedList(i, j)
    print(a, b)
