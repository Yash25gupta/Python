# code.Pylet - Basic Jumping
# watch the video here - https://youtu.be/osDofIdja6s
# Any questions? Just ask!

import pygame
from pygame.locals import *
import sys


class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.jump_offset = 0


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and not player.jumping and player.jump_offset == 0:
        player.jumping = True


def do_jumping(player):
    global jump_height

    if player.jumping:
        player.jump_offset += 1
        if player.jump_offset >= jump_height:
            player.jumping = False
    elif player.jump_offset > 0 and not player.jumping:
        player.jump_offset -= 1


W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SOLID_FILL = 0

p = player(HW, HH, 30)
jump_height = 50

pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 30

while True:
    events()
    keys(p)

    do_jumping(p)
    pygame.draw.circle(
        DS, WHITE, (int(p.x), int(p.y - p.jump_offset)), p.size, SOLID_FILL)

    if p.jump_offset == 0:
        pygame.draw.rect(DS, WHITE, (HW - 100, HH +
                                     p.size, 200, 10), SOLID_FILL)
    else:
        pygame.draw.rect(DS, RED, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
