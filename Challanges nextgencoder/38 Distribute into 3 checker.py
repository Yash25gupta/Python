def distributeInThree(lst):
    out = [0, 0, 0]
    for i in sorted(lst, reverse=True):
        ind = out.index(min(out))
        out[ind] += i
    return 'Yes' if len(set(out)) == 1 else 'No'


for i in ([2, 3, 1, 3], [3, 1, 4, 3], [3, 1, 1, 4, 3]):
    print(distributeInThree(i))
