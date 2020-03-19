import pygame
from random import randint
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
players = ('Yellow', 'Red')
board = []
play_with_AI = None

pygame.init()
screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()


def makeBoard():
    board.clear()
    for row in range(6):
        board.append([0 for col in range(7)])


def is_wining_move():
    b = board
    for r in range(6):
        for c in range(7):
            # Horizontal
            if c < 4 and (b[r][c] == b[r][c + 1] == b[r][c + 2] == b[r][c + 3] != 0): return True
            # Vertical
            if r < 3 and (b[r][c] == b[r + 1][c] == b[r + 2][c] == b[r + 3][c] != 0): return True
            # Diagonal
            if r < 3 and c < 4 and (b[r][c] == b[r + 1][c + 1] == b[r + 2][c + 2] == b[r + 3][c + 3] != 0): return True
            # -ve Diagonal
            if r > 2 and c < 4 and (b[r][c] == b[r - 1][c + 1] == b[r - 2][c + 2] == b[r - 3][c + 3] != 0): return True
    return False


def comp_move():
    for r in range(6):
        for c in range(7):
            above = board[r - 1][c] != 0
            if r == 0: above = True
            if board[r][c] == 0 and above:
                board[r][c] = 1
                if is_wining_move():
                    board[r][c] = 0
                    return c
                board[r][c] = 2
                if is_wining_move():
                    board[r][c] = 0
                    return c
                board[r][c] = 0
    return randint(0, 6)


def is_game_over():
    for r in range(6):
        for c in range(7):
            if 0 == board[5 - r][c]:
                return False
    return True


def show_msg(text, x, y=20, color=WHITE, s=36):
    font = pygame.font.Font('freesansbold.ttf', s)
    msg = font.render(text, True, color)
    msg_rect = msg.get_rect()
    msg_rect.center = 350, y
    screen.blit(msg, msg_rect)
    return msg, msg_rect


def draw_board(win, b, x):
    win.fill(BLACK)
    pygame.draw.rect(win, BLUE, (0, 100, 700, 700))
    for r in range(6):
        for c in range(7):
            COLOR = BLACK
            if b[5 - r][c] == 1: COLOR = RED
            if b[5 - r][c] == 2: COLOR = YELLOW
            pygame.draw.circle(
                win, COLOR, (50 + (c * 100), 150 + (r * 100)), 45)
    pygame.draw.circle(win, RED, (x, 50), 45)


def welcome():
    global play_with_AI
    run = True
    while run:
        clock.tick(10)
        screen.fill((233, 210, 229))
        show_msg('Welcome to the Connect4 vs AI', 50, 200, RED, 45)
        vsPl, vsPl_pos = show_msg('Player1 vs Player2', 150, 310, RED)
        vsAI, vsAI_pos = show_msg('Player vs AI', 150, 370, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: run = False
            if event.type == pygame.MOUSEMOTION:
                if vsPl_pos.collidepoint(event.pos): show_msg(
                    'Player1 vs Player2', 150, 310, BLUE)
                if vsAI_pos.collidepoint(event.pos): show_msg(
                    'Player vs AI', 150, 370, BLUE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vsPl_pos.collidepoint(event.pos):
                    run = False
                    play_with_AI = False
                    mainloop()
                if vsAI_pos.collidepoint(event.pos):
                    run = False
                    play_with_AI = True
                    mainloop()
        pygame.display.update()


def mainloop():
    makeBoard()
    turn = posx = 0
    running = True
    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
            if event.type == pygame.MOUSEMOTION: posx = event.pos[0]
            if play_with_AI:
                if event.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0:   # Human Turn
                    c = event.pos[0] // 100
                    if 0 != board[5][c]: break
                    for r in range(6):
                        if board[r][c] == 0:
                            board[r][c] = 1
                            break
                    turn += 1
                elif turn % 2 == 1:   # Computer
                    c = comp_move()
                    if 0 != board[5][c]: break
                    for r in range(6):
                        if board[r][c] == 0:
                            board[r][c] = 2
                            break
                    turn += 1
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    c = event.pos[0] // 100
                    if 0 != board[5][c]: break
                    p = 1
                    if turn % 2 != 0: p = 2
                    for r in range(6):
                        if board[r][c] == 0:
                            board[r][c] = p
                            break
                    turn += 1
        draw_board(screen, board, posx)
        if is_wining_move(): show_msg(
            'Player {} wins!!!'.format(players[turn % 2]), 200)
        if is_game_over(): show_msg('GAME OVER. Nobody wins...', 100)
        pygame.display.update()
        if is_wining_move() or is_game_over():
            pygame.time.delay(2000)
            running = False
            welcome()


welcome()
