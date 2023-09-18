import pygame

# Screen Constants
WIDTH = 800
HEIGHT = 600
TITLE = "Platformer Game"
FONT_NAME = 'arial'

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game Constants
FPS = 60
COL_BG = GREEN
SCALE = 1.3
ANIMATION_SPEED = 0.18
FRIC = -0.12


# Player Constants
PLAYER_SPEED = 0.5
PLAYER_JUMP_SPEED = 12
PLAYER_GRAVITY = 0.5

ENEMY_SPEED = 0.3
ENEMY_GRAVITY = 0.6
AMMO = 30
SHOOT_COOLDOWN = 300

# Bullet Constants
BULLET_SPEED = 2.5

# Platform Constants
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = GREEN
