def differenceList(diff, lst):
    lst = sorted(lst, reverse=True)
    difs = []
    for i in range(len(lst)):
        if lst[i] < diff: break
        for j in range(i, len(lst)):
            d = lst[i] - lst[j]
            if d == diff:
                difs.append((lst[i], lst[j]))
            if d >= diff: break
    return len(difs)


d = (3, 2, 32)
ls = ([5, 4, 6, 7, 8, 9, 1, 17, 14],
      [5, 4, 6, 7, 8, 9, 1, 17, 14],
      [9, 12, 8, 6, 5, 2, 19, 3])
for i, j in zip(d, ls):
    print(i, j, '-->', differenceList(i, j))
