import pygame
from math import sqrt, pow
from random import randint

# Intialize the pygame
pygame.init()

# Intialize the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('bg.png')

# Sounds
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound('laser.wav')
explosion = pygame.mixer.Sound('explosion.wav')

# Title and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
player_dX = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemy_dX = []
enemy_dY = []
enemy_nums = 6
for i in range(enemy_nums):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(randint(0, 736))
    enemyY.append(randint(50, 150))
    enemy_dX.append(1.5)
    enemy_dY.append(30)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_dY = 5
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf', 70)

def show_gameover():
    game_over = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (200, 250))

def show_score(x, y):
    score = font.render('Score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (int(x), int(y)))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (int(x), int(y)))

def fire_bullet(x, y):
    screen.blit(bulletImg, (int(x)+16, int(y)+10))

def iscolision(eX, eY, bX, bY):
    distance = sqrt(pow(eX-bX+16, 2) + pow(eY-bY+32, 2))
    return distance < 35

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dX = -1.5
            if event.key == pygame.K_RIGHT:
                player_dX = 1.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    laser.play()
                    bullet_state = 'fire'
                    bulletX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dX = 0

    # Checking Boundry
    playerX += player_dX
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    # Enemy Movement
    for i in range(enemy_nums):
        enemyX[i] += enemy_dX[i]
        if not 0 < enemyX[i] < 736:
            enemy_dX[i] *= -1
            enemyY[i] += enemy_dY[i]

        # Game over
        if enemyY[i] > 420:
            for j in range(enemy_nums):
                enemyY[j] = 2000
            show_gameover()
            break

        # Colision
        collision = iscolision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = randint(0, 736)
            enemyY[i] = randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_dY

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
