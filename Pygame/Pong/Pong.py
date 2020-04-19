import pygame
from random import randint, choice
from math import sqrt, pow
# Intialize the pygame
pygame.init()

# Intialize the screen
screen = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load('bg.png')
sound = pygame.mixer.Sound('bounce.wav')

# Title and icon
pygame.display.set_caption('Ping Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Ball
ballImg = pygame.image.load('ball.png')
ballX = 624
ballY = randint(50, 450)
ballX_change = 3
ballY_change = 3

# Player1
player1Img = pygame.image.load('bar.png')
player1X = 15
player1Y = 250
player1Y_change = 0
player1_score = 0

# Player2
player2Img = pygame.image.load('bar.png')
player2X = 1245
player2Y = 250
player2Y_change = 0
player2_score = 0

vel = 5

# Score
font = pygame.font.Font('freesansbold.ttf', 72)
textX = 560
textY = 20


def show_score(x, y):
    score = font.render(str(player1_score) + '    ' +
                        str(player2_score), True, (255, 255, 255))
    screen.blit(score, (x, y))


def ball(x, y):
    screen.blit(ballImg, (x, y))


def player1(x, y):
    screen.blit(player1Img, (x, y))


def player2(x, y):
    screen.blit(player2Img, (x, y))


def iscollision(bx, by, px, py):
    ''' This function returns "True" if their is collision between Ball and Paddle. '''
    distance = sqrt(pow(bx - px + 6, 2) + pow(by - py + 16, 2))
    return distance < 26


# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    # User inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1Y_change -= vel
            if event.key == pygame.K_s:
                player1Y_change += vel
            if event.key == pygame.K_UP:
                player2Y_change -= vel
            if event.key == pygame.K_DOWN:
                player2Y_change += vel
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1Y_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2Y_change = 0

    # Validate Users Movement
    player1Y += player1Y_change
    if player1Y < 10:
        player1Y = 10
    if player1Y > 580:
        player1Y = 580
    player2Y += player2Y_change
    if player2Y < 10:
        player2Y = 10
    if player2Y > 580:
        player2Y = 580

    # Ball Movement
    ballX += ballX_change
    ballY += ballY_change
    if not 5 < ballY < 680:
        ballY_change *= -1
    # # Collision with Paddles
    p1_Y = tuple(i for i in range(player1Y, player1Y + 128, 4))
    p2_Y = tuple(i for i in range(player2Y, player2Y + 128, 4))
    n = len(p1_Y)
    col1 = any(map(iscollision, [ballX] * n,
                   [ballY] * n, [player1X] * n, p1_Y))
    col2 = any(map(iscollision, [ballX] * n,
                   [ballY] * n, [player2X] * n, p2_Y))
    if col1 or col2:
        sound.play()
        ballX_change *= -1
        if ballX > 800:
            ballX_change -= 1
        if ballX < 400:
            ballX_change += 1
        if abs(ballX_change) % 6 == 0:
            vel += 3
    # # Collision with Wall (OUT)
    if not 5 < ballX < 1245:
        if ballX > 800:
            player1_score += 1
        if ballX < 400:
            player2_score += 1
        pygame.time.delay(50)
        ballX = 624
        ballY = randint(50, 450)
        ballX_change = choice([3, -3])
        vel = 5

    show_score(textX, textY)
    ball(ballX, ballY)
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    pygame.display.update()
