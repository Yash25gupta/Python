from colorama import Fore
from random import choice
from os import system


def colorInt(*args):
    return [Fore.RED + str(txt) + Fore.RESET if type(txt) == int else txt for txt in args]


def printBoard(b):
    print('\n {} | {} | {}'.format(*colorInt(b[0], b[1], b[2])))
    print('---|---|---')
    print(' {} | {} | {}'.format(*colorInt(b[3], b[4], b[5])))
    print('---|---|---')
    print(' {} | {} | {}\n'.format(*colorInt(b[6], b[7], b[8])))


def askUserInput():
    while True:
        try:
            pos = int(input('Enter your choice from above Numbers: ')) - 1
            if -1 < pos < 9 and int(board[pos]): return pos
            print('Please Enter valid position number.')
        except ValueError:
            print('Enter digits Only.')


def compMovePos():
    blanks = [i for i in range(9) if type(board[i]) == int]
    for p in 'OX':
        for i in blanks:
            board[i] = p
            if checkWin(board)[0]: return i
            board[i] = i + 1
    return 4 if type(board[4]) == int else choice(blanks)


def checkWin(b):
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i, j, k in wins:
        if b[i] == b[j] == b[k]: return True, b[i]
    return False, None


def checkDraw(b):
    return not any([type(i) == int for i in b])


def makeMoves():
    system('cls')
    print(f'You="X" and Computer="O". First Turn is of "{first}"')
    if first == 'X':
        printBoard(board)
        board[askUserInput()] = 'X'
        if not checkDraw(board): board[compMovePos()] = 'O'
    else:
        board[compMovePos()] = 'O'
        printBoard(board)
        if not checkDraw(board): board[askUserInput()] = 'X'


playing = True
while playing:
    board = [i for i in range(1, 10)]
    gameOver = False
    first = choice('XO')
    while not gameOver:
        makeMoves()
        hasWinner, winner = checkWin(board)
        if hasWinner:
            gameOver = True
            print(f'Player {winner} wins!!!')
        if checkDraw(board):
            gameOver = True
            print('Game Draw!!!')
    playing = (input('Do you want to play again? (Y/y/N/n): ') in 'Yy')
