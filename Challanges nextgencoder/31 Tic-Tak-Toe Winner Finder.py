def winPlayer(r1, r2, r3):
    if any(map(lambda i: i not in 'XO-', r1 + r2 + r3)): return 'ERROR'
    player = ''
    if r1[0] == r1[1] == r1[2]: player = r1[0]      # H1
    elif r2[0] == r2[1] == r2[2]: player = r2[0]    # H2
    elif r3[0] == r3[1] == r3[2]: player = r3[0]    # H3
    elif r1[0] == r2[0] == r3[0]: player = r1[0]    # V1
    elif r1[1] == r2[1] == r3[1]: player = r1[1]    # V2
    elif r1[2] == r2[2] == r3[2]: player = r1[2]    # V3
    elif r1[0] == r2[1] == r3[2]: player = r1[0]    # D1
    elif r1[2] == r2[1] == r3[0]: player = r1[2]    # D2
    if player != '': return 'Player ' + player + ' Wins'
    return 'Draw'


row1 = (['X', 'O', '-'], ['X', 'O', '-'], ['X', 'O', '-'], ['X', 'O', '-'])
row2 = (['O', 'X', '-'], ['O', 'X', 'X'], ['X', 'O', '-'], ['O', '9', 'X'])
row3 = (['-', 'O', 'X'], ['O', 'X', 'O'], ['-', 'O', 'X'], ['O', 'X', 'O'])
for i, j, k in zip(row1, row2, row3):
    print(f'{i}\n{j}  =>  {winPlayer(i, j, k)}\n{k}\n')
