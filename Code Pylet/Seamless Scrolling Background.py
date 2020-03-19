# code.Pylet - Scrolling Background Image
# watch the video here - https://youtu.be/US3HSusUBeI
# Any questions? Just ask!

import pygame
from pygame.locals import *
import sys
import os


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 576, 1024
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background Image")
FPS = 120

bg = pygame.image.load("mountains.png").convert()
x = 0

# main loop
while True:
    events()

    bg_x = x % bg.get_rect().width
    DS.blit(bg, (bg_x - bg.get_rect().width, 0))
    if bg_x < W:
        DS.blit(bg, (bg_x, 0))
    x -= 2
    pygame.draw.line(DS, (255, 0, 0), (bg_x, 0), (bg_x, H), 3)

    pygame.display.update()
    CLOCK.tick(FPS)
