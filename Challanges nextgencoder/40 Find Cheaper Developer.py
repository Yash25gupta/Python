def minCoin(coder, cost):
    high = max(cost)
    out = [high, high, high]
    for i in range(len(coder)):
        out[coder[i] - 1] = min(out[coder[i] - 1], cost[i])
    return sum(out[:2]) if sum(out[:2]) < out[2] else out[2]


c = ([1, 3, 2, 3, 1], [3, 1, 2, 3, 1], [3, 1, 2, 3, 1])
a = ([3, 5, 2, 4, 6], [9, 5, 2, 7, 3], [9, 5, 2, 7, 6])
for i, j in zip(c, a):
    print(minCoin(i, j))
