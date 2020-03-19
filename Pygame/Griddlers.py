import pygame
from random import randint
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLOCK_SIZE = 55
margin = 120
board1 = [[randint(0, 1) for col in range(10)] for row in range(10)]
board2 = [[0 for col in range(10)] for row in range(10)]


def create_btns():
    size = BLOCK_SIZE + 5
    for row in range(10):
        for col in range(10):
            color = GREEN
            if board2[row][col] == 1: color = RED
            if board2[row][col] == 3: color = BLUE
            pygame.draw.rect(screen, color, (size * col + margin,
                                             size * row + margin, BLOCK_SIZE, BLOCK_SIZE))


def cols_info(b):
    cs = []
    a = []
    s = 0
    for c in range(10):
        for pos, i in enumerate(b):
            s += i[c]
            if i[c] == 1 and pos != 9: continue
            a.append(s)
            s = 0
        for i in range(a.count(0)):
            a.remove(0)
        cs.append(tuple(a))
        a.clear()
    return cs


def rows_info(b):
    rs = []
    a = []
    s = 0
    for r in range(10):
        for pos, i in enumerate(b[r]):
            s += i
            if i == 1 and pos != 9: continue
            a.append(s)
            s = 0
        for i in range(a.count(0)):
            a.remove(0)
        rs.append(tuple(a))
        a.clear()
    return rs


def show_msg(text, x, y, color=WHITE, s=32):
    font = pygame.font.Font(None, s)
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))


pygame.init()
screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption('Gridlers')
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = int(event.pos[0] // (margin / 2) -
                      (margin // (BLOCK_SIZE + 5)))
            row = int(event.pos[1] // (margin / 2) -
                      (margin // (BLOCK_SIZE + 5)))
            board2[row][col] = event.button
            if board2[row][col] != 1 and board2[row][col] != 3: board2[row][col] = 0

    for pos, i in enumerate(cols_info(board1)):
        ty = 80 if pos % 2 == 0 else 50
        show_msg(str(i), 120 + (pos * margin / 2), ty)
    for pos, i in enumerate(rows_info(board1)):
        show_msg(str(i), 20, 135 + (pos * margin / 2))

    create_btns()
    if board1 == board2:
        running = False
        show_msg('You Win!!!', 200, 300, WHITE, 128)
        pygame.display.update()
        pygame.time.delay(2000)
    pygame.display.update()
pygame.quit()
