import pygame
from math import sqrt, pow
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bg.png').convert()

pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound('laser.wav')
explosion = pygame.mixer.Sound('explosion.wav')

with open('hiscore.txt', 'r') as f:
    hiscore = f.read()

class Player(object):
    score = 0
    def __init__(self, x, y):
        self.img = pygame.image.load('player.png').convert_alpha()
        self.x = x
        self.y = y
        self.dx = 0

    def draw(self, win):
        self.move()
        win.blit(self.img, (int(self.x), int(self.y)))

    def move(self):
        self.x += self.dx
        if self.x < 0:
            self.x = 0
        if self.x > 736:
            self.x = 736

class Enemy(object):
    def __init__(self, x, y):
        self.img = pygame.image.load('enemy.png').convert_alpha()
        self.x = x
        self.y = y
        self.dx = 1.5
        self.dy = 30

    @staticmethod
    def iscollision(eX, eY, bX, bY):
        distance = sqrt(pow(eX-bX+16, 2) + pow(eY-bY+32, 2))
        return distance < 35

    def draw(self, win):
        self.move()
        self.collision()
        win.blit(self.img, (int(self.x), int(self.y)))

    def move(self):
        self.x += self.dx
        if not 0 < self.x < 736:
            self.dx *= -1
            self.y += self.dy
        if self.y > 420:
            show_gameover()
            for enemy in enemys:
                enemy.y = 2000
            with open('files\\space hiscore.txt', 'w') as f:
                f.write(str(hiscore))

    def collision(self):
        col = self.iscollision(self.x, self.y, bullet.x, bullet.y)
        if col:
            explosion.play()
            bullet.y = 480
            bullet.state = 'ready'
            Player.score += 1
            self.x = randint(0, 736)
            self.y = randint(50, 150)

class Bullet(object):
    def __init__(self):
        self.img = pygame.image.load('bullet.png').convert_alpha()
        self.x = 0
        self.y = 480
        self.dy = 5
        self.state = 'ready'

    def draw(self, win):
        if bullet.state == 'fire':
            self.move()
            win.blit(self.img, (int(self.x), int(self.y)))

    def move(self):
        self.y -= self.dy
        if self.y < 0:
            self.y = 480
            self.state = 'ready'

def show_gameover():
    over_font = pygame.font.Font('freesansbold.ttf', 70)
    game_over = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (200, 250))

def show_score(hs):
    global hiscore
    if Player.score > int(hs) : hiscore = Player.score
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render('Score : ' + str(Player.score) + '   HiScore : ' + str(hiscore), True, (255, 255, 255))
    screen.blit(score, (10, 10))

def redrawGameWindow():
    screen.blit(background, (0, 0))
    player.draw(screen)
    for enemy in enemys:
        enemy.draw(screen)
    bullet.draw(screen)
    show_score(hiscore)
    pygame.display.update()

# main loop
player = Player(370, 480)
bullet = Bullet()
n = 5   # Numbers of enemy
enemys = tuple(Enemy(randint(0, 736), randint(50, 150)) for i in range(n))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.dx = -1.5
            if event.key == pygame.K_RIGHT:
                player.dx = 1.5
            if event.key == pygame.K_SPACE:
                if bullet.state == 'ready':
                    laser.play()
                    bullet.state = 'fire'
                    bullet.x = player.x + 16
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.dx = 0

    redrawGameWindow()
