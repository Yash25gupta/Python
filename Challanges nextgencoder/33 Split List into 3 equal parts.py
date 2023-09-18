def splitInThree(lst):
    lst = sorted(lst, reverse=True)
    out = [[], [], []]
    temp = [0, 0, 0]
    for j in lst:
        i = temp.index(min(temp))
        temp[i] += j
        out[i].append(j)
    return out


for i in ([2, 4, 7, 3, 2, 4, 6], [3, 4, 6, 4, 7, 4, 2], [8, 5, 5, 2, 4, 5, 3]):
    print(splitInThree(i))
# [2,4,3][7,2][4,6], [3,7][4,6][4,4,2], [8,2][5,5][4,5,3]
