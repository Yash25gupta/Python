# code.Pylet - Distance Based Collision
# watch the video here - https://youtu.be/gAkUlyj6irw
# Any questions? Just ask!

import math, random, sys
import pygame
from pygame.locals import *
from pygame import gfxdraw

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
pygame.font.init()
FONT = pygame.font.Font(None, 36)
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption("code.Pylet - Distance Based Collision")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = [0, 0, 255]

PI = math.pi
QTR_PI = PI / 2.0

def draw_arrow(color, x1, y1, x2, y2, alpha = 255, surface = None):
	global PI, QTR_PI, FONT, WHITE
	if not surface: surface = pygame.display.get_surface()
	headLength = 50
	headWidth = 10
	lineWidth = 5
	
	d = math.hypot(x2 - x1, y2 - y1)
	r = math.atan2(y2 - y1, x2 - x1)
	ax1, ay1 = x1 + math.cos(r) * headLength, y1 + math.sin(r) * headLength
	ax2, ay2 = x2 + math.cos(r - PI) * headLength, y2 + math.sin(r - PI) * headLength
	distanceText = FONT.render("{0:.2f}".format(d), 1, WHITE)
	textX = x1 + math.cos(r) * (d / 2)
	textY = y1 + math.sin(r) * (d / 2)
	textRect = distanceText.get_rect()
	arrowHead1 = [
		(ax1 + math.cos(r - QTR_PI) * lineWidth, ay1 + math.sin(r - QTR_PI) * lineWidth),
		(ax1 + math.cos(r - QTR_PI) * headWidth, ay1 + math.sin(r - QTR_PI) * headWidth),
		(ax1 + math.cos(r - PI) * headLength, ay1 + math.sin(r - PI) * headLength),
		(ax1 + math.cos(r + QTR_PI) * headWidth, ay1 + math.sin(r + QTR_PI) * headWidth),
		(ax1 + math.cos(r + QTR_PI) * lineWidth, ay1 + math.sin(r + QTR_PI) * lineWidth),
	]
	arrowHead2 = [
		(ax2 + math.cos(r + QTR_PI) * lineWidth, ay2 + math.sin(r + QTR_PI) * lineWidth),
		(ax2 + math.cos(r - QTR_PI) * headWidth, ay2 + math.sin(r - QTR_PI) * headWidth),
		(ax2 + math.cos(r) * headLength, ay2 + math.sin(r) * headLength),
		(ax2 + math.cos(r + QTR_PI) * headWidth, ay2 + math.sin(r + QTR_PI) * headWidth),
		(ax2 + math.cos(r - QTR_PI) * lineWidth, ay2 + math.sin(r - QTR_PI) * lineWidth),
	]
	arrow = arrowHead1 + arrowHead2
	pygame.gfxdraw.filled_polygon(surface, arrow, color + [alpha])
	surface.blit(distanceText, (textX - textRect.center[0], textY - textRect.center[1]))

x1, y1, radius1, color1 = HW, HH, 150, None
x2, y2, radius2, color2 = None, None, 300, GREY

# main loop
while True:
	events()

	x2, y2 = pygame.mouse.get_pos()
	
	distance = math.hypot(x1 - x2, y1 - y2)
	if distance <= radius1 + radius2:
		color1 = RED
	else:
		color1 = GREEN
	
	pygame.draw.circle(DS, color1, (x1, y1), radius1, 0)
	pygame.draw.circle(DS, color2, (x2, y2), radius2, 0)
	draw_arrow(BLUE, x1, y1, x2, y2, 128)	
	draw_arrow(BLUE, x1, y1, x1, y1 - radius1, 128)
	draw_arrow(BLUE, x2, y2, x2, y2 - radius2, 128)
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)