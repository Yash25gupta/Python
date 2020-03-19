cur_player = 'X'
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def show_board():
    print()
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def flip_player():
    global cur_player
    if cur_player == 'X':
        cur_player = 'O'
    else:
        cur_player = 'X'

def check_win():
    t = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,5,8), (2,5,7))
    for a,b,c in t:
        if board[a] == board[b] == board[c] != '-':
            return True
    return False

def check_tie():
    return '-' not in board

def check_gameover():
    if check_win():
        print(f'Player {cur_player} wins!!!')
        return True
    if check_tie():
        print(f'Game Over')
        return True
    return False

def get_position():
    while True:
        try:
            pos = int(input('Choose position (1-9) : ')) - 1
            if pos in range(9) and board[pos] == '-':
                return pos
            print('Not a valid choice.\n')
        except ValueError:
            print('Please type digits only.\n')

def playgame():
    show_board()
    while True:
        pos = get_position()
        board[pos] = cur_player
        show_board()
        if check_gameover() : break
        flip_player()
        print('Current Player : ' + cur_player)

playgame()

