from constants import *


class Tile(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.value = 0
        self.highlight = False
        self.font = pygame.font.SysFont('Arial', 25)

    def draw(self, screen):
        rect = (self.i+1, self.j+1, 1, 1)
        rect = [i * CELL_WIDTH for i in rect]
        pygame.draw.rect(screen, TILE_COLOR[self.value], rect, 0, 5)
        pygame.draw.rect(screen, BLACK, rect, 1, 5)
        if self.highlight:
            pygame.draw.rect(screen, PURPLE, rect, 2, 5)
        textImg = self.font.render(f'{self.value}', True, BLACK)
        textRect = textImg.get_rect()
        textRect.center = (rect[0] + CELL_WIDTH/2, rect[1] + CELL_WIDTH/2)
        screen.blit(textImg, textRect)
