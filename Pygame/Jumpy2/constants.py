# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 155, 155)

BGCOLOR = LIGHTBLUE


# GAME CONSTANTS
WIDTH = 480
HEIGHT = 600
SCREENSIZE = (WIDTH, HEIGHT)
TITLE = 'Game Sprite Example'
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
FPS = 60
FONT = 'arial'
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet.png'

PLAT_LAYER = 1
POWER_LAYER = 1
PLAYER_LAYER = 2
ENEMY_LAYER = 2

# Player
PLAYER_ACCELERATION = 0.6
PLAYER_FRICTION = -0.12
GRAVITY = 0.9
PLAYER_JUMP = 20

# Platforms
PLATFORM_LIST = [(0, HEIGHT - 60), (200, 450), (125, 250),
                 (350, 200), (175, 100), (20, 20)]
PLAT_NUMBERS = 7

# Game properties
JET_POWER = 80
WING_POWER = 40
POW_SPAWN_PCT = 7
