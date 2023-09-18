from os import system
hs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}


def addArmy(h1, qty):
    hs[h1] += int(qty)


def join(h1, h2):
    hs[h1], hs[h2] = (hs[h1] + hs[h2], None) if hs[h1] >= hs[h2] else (None, hs[h1] + hs[h2])


def attack(h1, h2):
    hs[h1], hs[h2] = (hs[h1] * 2 // 3, None) if hs[h1] >= hs[h2] else (None, hs[h2] * 2 // 3)


def checkWin():
    if len([i for i in hs.values() if i is not None]) == 1:
        for k in hs.keys():
            if hs[k] is not None: return True, k
    return False, None


def menu():
    while True:
        system('cls')
        for k, v in hs.items(): print(k, v, end=' ' * 5)
        print('\nFunctions:')
        print('1 : addArmy(house, qty)')
        print('2 : join(house1, house2)')
        print('3 : attack(house1, house2)\n')
        fun, a1, a2 = input(
            'Write function number and values seperated by " "(space).\n').lower().split(' ')
        if fun == '1': addArmy(a1, a2)
        if fun == '2': join(a1, a2)
        if fun == '3': attack(a1, a2)
        win, winner = checkWin()
        if win: break
    print(winner, 'is the winner')


menu()
