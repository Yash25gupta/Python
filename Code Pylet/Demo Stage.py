import math
import random
import sys
import pygame
from pygame.locals import *

# exit the program


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


def text(font, string, x, y, xJustify=None, yJustify=None, surface=None):
    global WHITE, BLACK
    if not surface: surface = pygame.display.get_surface()
    textSurface = font.render(string, 1, WHITE, BLACK)
    textRect = textSurface.get_rect()
    if xJustify == 1:
        x -= textRect.width
    elif xJustify == 2:
        x -= textRect.center[0]
    if yJustify == 1:
        y -= textRect.height
    elif yJustify == 2:
        y -= textRect.center[1]
    surface.blit(textSurface, (x, y))


# define display surface
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
pygame.font.init()
CLOCK = pygame.time.Clock()
FONT_SMALL = pygame.font.Font(None, 26)
FONT_LARGE = pygame.font.Font(None, 50)
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255, 255)

circleRadius = 25

stageX = 50
stageY = HH - 200
stageHeight = 400
stageWidth = W - 100

dw = 712
dhw = dw / 2

# main loop
while True:
    events()

    mx, my = pygame.mouse.get_pos()

    if mx < stageX + circleRadius: mx = stageX + circleRadius
    if mx > stageX + stageWidth - circleRadius: mx = stageX + stageWidth - circleRadius

    if mx < stageX + dhw: dx = stageX + dhw
    elif mx > stageX + stageWidth - dhw: dx = stageX + stageWidth - dhw
    else:
        dx = mx

    pygame.draw.rect(DS, WHITE, (stageX, stageY, stageWidth, stageHeight), 2)
    pygame.draw.rect(DS, BLUE, (dx - dhw, stageY, dw, stageHeight), 2)
    pygame.draw.circle(DS, WHITE, (int(mx), int(HH + 100)), circleRadius, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
