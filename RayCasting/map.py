from settings import *

_ = False
map1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, 1, _, _, 1, _, 1, 1, _, 1],
        [1, _, _, _, 1, _, 1, 1, _, 1],
        [1, _, 1, _, 1, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, 1, _, 1, 1, 1, _, 1, 1],
        [1, _, 1, _, 1, _, _, _, _, 1],
        [1, _, _, _, _, _, _, 1, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

map2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

map3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maps = [map1, map2, map3]

class Map:
    def __init__(self, game, level=1):
        self.game = game
        self.map_data = maps[level-1]
        self.map_width = len(self.map_data[0])
        self.map_height = len(self.map_data)
        self.width = self.map_width * TILESIZE
        self.height = self.map_height * TILESIZE
        self.walls = self.get_walls()

    def get_walls(self):
        walls = []
        for row in range(self.map_height):
            for col in range(self.map_width):
                if self.map_data[row][col] == 1:
                    walls.append(pygame.Rect(col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
        return walls

    def draw(self, screen):
        for row in range(self.map_height):
            for col in range(self.map_width):
                if self.map_data[row][col] == 1:
                    pygame.draw.rect(screen, WHITE, (col * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE), 1)
