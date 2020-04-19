import pygame
from random import randint, choice
from math import sqrt, pow
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))

bounce = pygame.mixer.Sound('bounce.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

pygame.display.set_caption('Ping Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 3
        self.dy = 3

    @staticmethod
    def iscollision(bx, by, px, py):
        ''' This function returns "True" if their is collision between Ball and Paddle. '''
        distance = sqrt(pow(bx - px - 7, 2) + pow(by - py, 2))
        return distance < 21

    def draw(self, win):
        self.move()
        if not 40 < self.x < 1220:
            self.collision()
        pygame.draw.circle(win, WHITE, (self.x, self.y), 10)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if not 20 < self.y < 700:   # Top & Bottom
            self.dy *= -1
        if not 10 < self.x < 1270:  # Out Left & Right
            if self.x > 800:
                player1.score += 1
            if self.x < 400:
                player2.score += 1
            pygame.time.delay(100)
            self.x = 624
            self.y = randint(50, 450)
            self.dx = choice([3, -3])
            Player.vel = 5

    def collision(self):
        p1_Y = tuple(i for i in range(player1.y, player1.y + 128, 4))
        p2_Y = tuple(i for i in range(player2.y, player2.y + 128, 4))
        n = len(p1_Y)
        col1 = any(
            map(self.iscollision, [self.x] * n, [self.y] * n, [player1.x] * n, p1_Y))
        col2 = any(
            map(self.iscollision, [self.x] * n, [self.y] * n, [player2.x] * n, p2_Y))
        if col1 or col2:
            bounce.play()
            self.dx *= -1
            if self.x > 800:
                self.dx -= 1
            if self.x < 400:
                self.dx += 1
            if abs(self.dx) % 6 == 0:
                Player.vel += 3


class Player(object):
    vel = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.score = 0

    def draw(self, win):
        self.move()
        pygame.draw.line(win, WHITE, (self.x, self.y),
                         (self.x, self.y + 128), 14)

    def move(self):
        self.y += self.dy
        if self.y < 10:
            self.y = 10
        if self.y > 580:
            self.y = 580


def show_score(win):
    font = pygame.font.Font('freesansbold.ttf', 72)
    score = font.render(str(player1.score) + '    ' +
                        str(player2.score), True, WHITE)
    win.blit(score, (560, 20))


def background(win):
    win.fill(BLACK)
    lines = ((RED, (0, 2), (640, 2)), (RED, (0, 0), (0, 720)), (RED, (0, 718), (640, 718)),
             (BLUE, (640, 2), (1280, 2)), (BLUE, (1277, 2), (1277, 718)), (BLUE, (640, 718), (1280, 718)), (WHITE, (636, 0), (636, 720)))
    for i in lines:
        pygame.draw.line(win, i[0], i[1], i[2], 8)


def redrawGameWindow():
    background(screen)
    ball.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    show_score(screen)
    pygame.display.update()


# main loop
ball = Ball(640, randint(50, 450))
player1 = Player(20, 250)
player2 = Player(1260, 250)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.dy -= Player.vel
            if event.key == pygame.K_s:
                player1.dy += Player.vel
            if event.key == pygame.K_UP:
                player2.dy -= Player.vel
            if event.key == pygame.K_DOWN:
                player2.dy += Player.vel
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1.dy = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2.dy = 0
    redrawGameWindow()
