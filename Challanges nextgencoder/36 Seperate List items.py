def seperateList(lst):
    return [[i] * lst.count(i) for i in set(lst)]


lists = ([1, 3, 5, 2, 4, 2, 1, 6],
         [1, 3, 5, 2, 3, 2, 1, 3],
         [1, 2, 3, 4, 5, 6, 7, 8],
         [1, 1, 1, 1, 1, 1, 1, 1])
for i in lists:
    print(seperateList(i))
