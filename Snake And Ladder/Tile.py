from Constants import *


class Tile(object):
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i
        self.snadder = 0
        self.color = LIGHT_GRAY if i % 2 == 0 else DARK_GRAY

    def getCenter(self):
        return (self.x + TILE_WIDTH // 2, self.y + TILE_WIDTH // 2)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, TILE_WIDTH, TILE_WIDTH))
        pos = self.getCenter()
        draw_text(win, f'{self.i+1}', 20, BLACK, pos[0], pos[1])

    def highlight(self, win):
        pygame.draw.rect(win, BLUE, (self.x, self.y, TILE_WIDTH, TILE_WIDTH))

    def drawSnadder(self, win, tiles):
        if self.snadder != 0:
            myc = self.getCenter()
            nextC = tiles[self.i + self.snadder].getCenter()
            color = RED if self.snadder < 0 else GREEN
            pygame.draw.line(win, color, (myc[0], myc[1]), (nextC[0], nextC[1]), 5)




def draw_text(win, text, size, color, x, y):
    font = pygame.font.SysFont('arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surface, text_rect)