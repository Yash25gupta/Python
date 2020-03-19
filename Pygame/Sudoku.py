import pygame
import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50, 150, 255)
LIGHTPURPLE = (200, 150, 255)
LIGHTYELLOW = (255, 255, 100)


# Global Variables
WIDTH = 600
HEIGHT = 650
BOX_SIZE = 60
HALF_BOX_SIZE = BOX_SIZE // 2
BOX_COUNT = 9
PREVALUES = random.randint(20, 30)
X_POS = int((WIDTH - (BOX_SIZE * BOX_COUNT)) / 2)
Y_POS = int((HEIGHT - (BOX_SIZE * BOX_COUNT)) / 2) + 30
NUM_KEYS = (pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9,
            pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9)


# Game Variables
dr = dc = mouseX = mouseY = 0
boxX = boxY = X_POS + HALF_BOX_SIZE


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()


def makeBoard():
    grid = [[0 for cell in range(BOX_COUNT)] for row in range(BOX_COUNT)]
    for i in range(PREVALUES):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        while not Valid(grid, row, col, num):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
        grid[row][col] = num
    return grid


def Valid(g, r, c, n):
    for i in range(9):
        if g[r][i] == n: return False
        if g[i][c] == n: return False
    rowSec = (r // 3) * 3  # 0,0,0,3,3,3,6,6,6
    colSec = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if g[x + rowSec][y + colSec] == n: return False
    return True


def show_msg(text, x, y, color, s=36):
    font = pygame.font.Font('freesansbold.ttf', s)
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))


def welcome():
    run = True
    while run:
        clock.tick(10)
        screen.fill(WHITE)
        show_msg('Welcome to Sudoku', 80, 200, RED, 45)
        show_msg('Press SpaceBar to Play Game', 40, 300, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: run = False
                if event.key == pygame.K_SPACE:
                    run = False
                    mainloop()
        pygame.display.update()


def mainloop():
    global mouseX, mouseY, dr, dc
    running = True
    mainBoard = makeBoard()
    userBoard = [x[:] for x in mainBoard]
    cornerBoard = [[list() for cell in range(BOX_COUNT)]
                   for row in range(BOX_COUNT)]
    btn1 = Button('Normal', 'Corner', 200, 20, 100, 50)
    while running:
        screen.fill(WHITE)
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                if event.key == pygame.K_DELETE:
                    mainBoard = makeBoard()
                    userBoard = [x[:] for x in mainBoard]
                    cornerBoard = [[list() for cell in range(BOX_COUNT)]
                                   for row in range(BOX_COUNT)]
                if event.key == pygame.K_BACKSPACE: delSelBox(
                    userBoard, cornerBoard)
                if event.key == pygame.K_TAB: btn1.clicked = not btn1.clicked
                if event.key in (pygame.K_KP1, pygame.K_1): key = 1
                elif event.key in (pygame.K_KP2, pygame.K_2): key = 2
                elif event.key in (pygame.K_KP3, pygame.K_3): key = 3
                elif event.key in (pygame.K_KP4, pygame.K_4): key = 4
                elif event.key in (pygame.K_KP5, pygame.K_5): key = 5
                elif event.key in (pygame.K_KP6, pygame.K_6): key = 6
                elif event.key in (pygame.K_KP7, pygame.K_7): key = 7
                elif event.key in (pygame.K_KP8, pygame.K_8): key = 8
                elif event.key in (pygame.K_KP9, pygame.K_9): key = 9
                if event.key == pygame.K_UP: dr, dc = -1, 0
                elif event.key == pygame.K_DOWN: dr, dc = 1, 0
                elif event.key == pygame.K_LEFT: dr, dc = 0, -1
                elif event.key == pygame.K_RIGHT: dr, dc = 0, 1
                if event.key in NUM_KEYS: add(
                    key, userBoard, cornerBoard, btn1.clicked, boxX, boxY)

            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = event.pos

            btn1.handle_event(event)

        highlightCell(mouseX, mouseY)
        mouseX, mouseY = 0, 0
        btn1.update()
        btn1.draw(screen)
        drawGrid(screen)
        writeText(screen, mainBoard, userBoard, cornerBoard)
        pygame.display.update()


def highlightCell(mX, mY):
    global boxX, boxY, dr, dc
    boxX += dc * 60
    boxY += dr * 60
    if boxX < X_POS: boxX = X_POS + BOX_SIZE * BOX_COUNT - HALF_BOX_SIZE
    if boxX > X_POS + BOX_SIZE * BOX_COUNT: boxX = X_POS + HALF_BOX_SIZE
    if boxY < Y_POS: boxY = Y_POS + BOX_SIZE * BOX_COUNT - HALF_BOX_SIZE
    if boxY > Y_POS + BOX_SIZE * BOX_COUNT: boxY = Y_POS + HALF_BOX_SIZE
    grid = pygame.Rect(X_POS, Y_POS, BOX_SIZE *
                       BOX_COUNT, BOX_SIZE * BOX_COUNT)
    if grid.collidepoint(mX, mY): boxX, boxY = mX, mY
    r, c = boxAt(boxX, boxY)
    if r != -1:
        x, y = box_XY(r, c)
        pygame.draw.rect(screen, LIGHTYELLOW, (x, y, BOX_SIZE, BOX_SIZE))
    dr = dc = 0


def delSelBox(ub, cb):
    r, c = boxAt(boxX, boxY)
    ub[c][r] = 0
    cb[c][r] = []


def drawGrid(win):
    for i in range(BOX_COUNT + 1):
        w = 1
        if i % 3 == 0: w = 2
        pygame.draw.line(win, BLACK, (X_POS + BOX_SIZE * i, Y_POS),
                         (X_POS + BOX_SIZE * i, Y_POS + BOX_SIZE * BOX_COUNT), w)
        pygame.draw.line(win, BLACK, (X_POS, Y_POS + BOX_SIZE * i),
                         (X_POS + BOX_SIZE * BOX_COUNT, Y_POS + BOX_SIZE * i), w)
    pygame.draw.rect(win, BLACK, (X_POS, Y_POS, BOX_SIZE *
                                  BOX_COUNT, BOX_SIZE * BOX_COUNT), 3)


def boxAt(x, y):
    for row in range(BOX_COUNT):
        for cell in range(BOX_COUNT):
            left, top = box_XY(row, cell)
            box = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if box.collidepoint(x, y):
                return (row, cell)
    return (-1, -1)


def box_XY(r, c):
    left = X_POS + BOX_SIZE * r
    top = Y_POS + BOX_SIZE * c
    return (left, top)


def writeText(win, mb, ub, cb):
    for row in range(BOX_COUNT):
        for cell in range(BOX_COUNT):
            left, top = box_XY(row, cell)
            if mb[cell][row] != 0:
                show_msg(str(mb[cell][row]), left + 20, top + 15, BLACK)
            elif ub[cell][row] != 0:
                show_msg(str(ub[cell][row]), left + 20, top + 15, BLUE)
            elif len(cb[cell][row]) > 0:
                try:
                    show_msg(str(cb[cell][row][0]), left +
                             2, top + 1, LIGHTPURPLE, 20)
                    show_msg(str(cb[cell][row][1]), left +
                             46, top + 1, LIGHTPURPLE, 20)
                    show_msg(str(cb[cell][row][2]), left +
                             2, top + 40, LIGHTPURPLE, 20)
                    show_msg(str(cb[cell][row][3]), left +
                             46, top + 40, LIGHTPURPLE, 20)
                except:
                    pass


def add(k, ub, cb, b, bX, bY):
    if X_POS < bX < X_POS + BOX_SIZE * BOX_COUNT and Y_POS < bY < Y_POS + BOX_SIZE * BOX_COUNT:
        r, c = boxAt(bX, bY)
        if b:
            cb[c][r].append(k)
        else:
            ub[c][r] = k


class Button():
    def __init__(self, text1, text2, x=0, y=0, width=100, height=50):
        self.text1 = text1
        self.text2 = text2
        self.text = text1
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(BLUE)
        self.image_normal2 = pygame.Surface((width, height))
        self.image_normal2.fill(BLUE)
        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill(RED)
        self.image_hovered2 = pygame.Surface((width, height))
        self.image_hovered2.fill(RED)
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        font = pygame.font.Font('freesansbold.ttf', 15)
        text_image = font.render(text1, True, WHITE)
        text_rect = text_image.get_rect(center=self.rect.center)
        text_image2 = font.render(text2, True, WHITE)
        text_rect2 = text_image2.get_rect(center=self.rect.center)
        self.image_normal.blit(text_image, text_rect)
        self.image_normal2.blit(text_image2, text_rect2)
        self.image_hovered.blit(text_image, text_rect)
        self.image_hovered2.blit(text_image2, text_rect2)
        self.rect.topleft = (x, y)
        self.hovered = False
        self.clicked = False

    def update(self):
        self.text = self.text1 if self.clicked else self.text2
        if self.clicked:
            self.image = self.image_hovered2 if self.hovered else self.image_normal2
        else:
            self.image = self.image_hovered if self.hovered else self.image_normal

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.clicked = not self.clicked


welcome()
