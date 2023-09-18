import pygame

WIDTH = 720
E_WIDTH = 280
TITLE = 'A* PathFinder - Yash Gupta'
FPS = 60
ROWS = 48  # multiple of WIDTH
WALL_PERCENTAGE = 30  # (x %)
E_H_WIDTH = E_WIDTH // 2

''' ---COLORS CODE--- '''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
''' ---GAME COLORS---'''
COL_BACKGROUND = WHITE
COL_WALL = BLACK
COL_START = PURPLE
COL_END = CYAN
COL_PATH = BLUE
COL_OPENSET = GREEN
COL_CLOSEDSET = RED
COL_INACTIVE = pygame.Color('lightskyblue3')
COL_ACTIVE = pygame.Color('dodgerblue2')
