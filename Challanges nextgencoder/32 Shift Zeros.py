def pushZeros(lst):
    # s = ''.join(''.join(map(str, lst)).split('0'))
    # for i in range(len(lst) - len(s)):
    #     s += '0'
    # return [i for i in s] if s.isdigit() else 'ERROR'

    # # or
    lst.sort(key=lambda x: x == 0)
    return lst if ''.join(map(str, lst)).isdigit() else 'ERROR'


lists = ([2, 4, 0, 3, 5, 0], [0, 4, 0, 3, 0, 1], [0, 4, 8, 3, 0, 1],
         [0, 0, 0, 0, 0, 0], [7, 2, 5, 7, 4, 9], [0, 6, 0, 4, 0, 'A'])
for i in lists:
    print(pushZeros(i))
