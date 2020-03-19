# code.Pylet - Basic Platforms
# watch the video here - https://youtu.be/jiYL07Yj9e8
# Any questions? Just ask!

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


# define display surface
W, H = 576, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Platforms")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

platform_y = H - 50

# """ This is for color collision
collision_map = pygame.Surface((W, H))
HIT = WHITE
MISS = BLACK
pygame.draw.line(collision_map, WHITE, (0, platform_y), (W, platform_y), 1)
# """

player_x = HW
player_y = 0
falling_velocity = 3

# main loop
while True:
    events()

    if player_y <= platform_y and player_y + falling_velocity >= platform_y:
        player_y = platform_y
    else:
        player_y += falling_velocity

    # """ This is for color collision
    collision = False
    for collision_y in range(player_y, player_y + falling_velocity):
        color = collision_map.get_at((int(player_x), int(collision_y)))
        if color == HIT:
            collision = True
            player_y = collision_y
            break
    if not collision:
        player_y += falling_velocity
    # """

    pygame.draw.circle(DS, WHITE, (int(player_x), int(player_y - 25)), 25, 0)
    pygame.draw.line(DS, WHITE, (0, platform_y), (W, platform_y), 1)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
