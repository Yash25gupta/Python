# code.Pylet - Physics Style Gravity Jumping
# watch the video here - https://youtu.be/2gPI_P67GYY
# Any questions? Just ask!

import pygame
from pygame.locals import *
import sys


class player:
    def __init__(self, x, y, py, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.velocity_index = 0
        self.platform_y = py

    def do_jumping(self):
        global velocity
        # velocity = list([ -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0,
        #					0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])
        if self.jumping:
            self.y += velocity[self.velocity_index]
            self.velocity_index += 1
            if self.velocity_index >= len(velocity) - 1:
                self.velocity_index = len(velocity) - 1
            if self.y > self.platform_y:
                self.y = self.platform_y
                self.jumping = False
                self.velocity_index = 0

    def draw(self):
        global DS, WHITE, SOLID_FILL
        pygame.draw.circle(
            DS, WHITE, (int(self.x), int(self.y)), self.size, SOLID_FILL)

    def do(self):
        self.do_jumping()
        self.draw()


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and not player.jumping:
        player.jumping = True


W, H = 960, 540
HW, HH = W / 2, H / 2
AREA = W * H

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SOLID_FILL = 0

p = player(HW, HH, HH, 30)
velocity = list([-7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -
                 1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])


pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 30

while True:
    events()
    keys(p)

    p.do()

    if p.jumping:
        pygame.draw.rect(DS, WHITE, (HW - 100, HH +
                                     p.size, 200, 10), SOLID_FILL)
    else:
        pygame.draw.rect(DS, RED, (HW - 100, HH + p.size, 200, 10), SOLID_FILL)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
