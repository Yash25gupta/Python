# code.Pylet - Distance Based Collision
# watch the video here - https://youtu.be/gAkUlyj6irw
# Any questions? Just ask!

import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1920, 1080
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Distance Based Collision")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)

white_star = pygame.image.load("whitestar-100x100.png").convert_alpha()
green_star = pygame.image.load("greenstar-100x100.png").convert_alpha()
red_star = pygame.image.load("redstar-100x100.png").convert_alpha()
star_radius = green_star.get_rect().center[0] # * 0.75

x1, y1, radius1, color1 = HW, HH, star_radius, None
x2, y2, radius2, color2 = None, None, star_radius, white_star

# main loop
while True:
	events()

	x2, y2 = pygame.mouse.get_pos()
	
	distance = math.hypot(x1 - x2, y1 - y2)
	if distance <= radius1 + radius2:
		color1 = red_star
	else:
		color1 = green_star
	
	DS.blit(color1, (x1, y1))
	DS.blit(color2, (x2, y2))
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)