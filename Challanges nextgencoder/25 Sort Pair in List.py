def sortListPair(numList, pairList):
    if len(numList) > 10 or len(pairList) != 2: return 'Error'
    if pairList[0] in numList and pairList[1] in numList:
        indexs = sorted([numList.index(i) for i in pairList])
        for i, index in enumerate(indexs):
            numList[index] = pairList[i]
    return numList


print(sortListPair([1, 4, 7, 3, 2, 1], [2, 4]))
print(sortListPair([1, 9, 7, 3, 2, 1], [7, 1]))
print(sortListPair([1, 9, 7, 3, 4, 1], [2, 5]))
print(sortListPair([1, 9, 7, 3, 2, 1], [1, 6]))
