'''
_____________________  |  sum - count
| 00 | 01 | 02 | 03 |  |   0  -  1  =>  1 Thife is required to block the policeman.
| 0  | 1  | 2  | 3  |  |   1  -  2  =>  2 Thife are required to block the policeman.
|____|____|____|____|  |   2  -  3  =>  3 Thife are required to block the policeman.
| 10 | 11 | 12 | 13 |  |   3  -  4  =>  4 Thife are required to block the policeman.
| 1  | 2  | 3  | 4  |  |   4  -  3  =>  3 Thife are required to block the policeman.
|____|____|____|____|  |   5  -  2  =>  2 Thife are required to block the policeman.
| 20 | 21 | 22 | 23 |  |   6  -  1  =>  1 Thife is required to block the policeman.
| 2  | 3  | 4  | 5  |  |   -------
|____|____|____|____|  |   s  -  s+1 or 7-s
| 30 | 31 | 32 | 33 |  |
| 3  | 1  | 5  | 6  |  |   No. of theves at position (whose sum of i,j is 's') = s+1 or 7-s
|____|____|____|____|  |  

'''


def canFindDiamond(x1, y1, x2, y2, x3, y3, x4, y4):
    s = (x1 + y1, x2 + y2, x3 + y3, x4 + y4)
    dic = {i: s.count(i) for i in range(7)}
    for k, v in dic.items():
        if v in (k + 1, 7 - k): return 'Failure'
    return 'Success'


print(canFindDiamond(0, 1, 2, 2, 3, 0, 2, 0))
print(canFindDiamond(0, 1, 1, 1, 1, 0, 2, 0))
