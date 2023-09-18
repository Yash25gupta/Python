from Constants import *
from random import randint


class Spot(object):
    def __init__(self, row, col, game):
        self.row = row
        self.col = col
        self.game = game
        self.x = row * game.SPOT_WIDTH
        self.y = col * game.SPOT_WIDTH
        self.isWall = (randint(0, 100) < WALL_PERCENTAGE)
        self.parent = None
        self.gCost = self.hCost = 0

    def fCost(self):
        return self.gCost + self.hCost

    def draw(self, win, color=COL_BACKGROUND):
        w = self.game.SPOT_WIDTH//2   # // 2
        if self.isWall:
            pygame.draw.circle(win, COL_WALL, (self.x + w + 1, self.y + w + 1), w)
            # pygame.draw.rect(win, COL_WALL, (self.x, self.y, w, w))
        else:
            pygame.draw.circle(win, color, (self.x + w, self.y + w), w)
            # pygame.draw.rect(win, color, (self.x, self.y, w, w))
            if self.game.SHOW_F_VALUE:
                draw_text(win, '{:.0f}'.format(self.fCost()), 10, COL_WALL, self.x + w, self.y + w)


class Button(object):
    def __init__(self, x=0, y=0, width=100, height=100, text_normal='', text_clicked='', command=None):
        self.command = command
        self.imgNormal = pygame.Surface((width, height))
        self.imgNormal.fill(GREEN)
        self.imgClicked = pygame.Surface((width, height))
        self.imgClicked.fill(GRAY)

        self.image = self.imgNormal
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 15)
        text_image_normal = font.render(text_normal, True, BLACK)
        text_rect_normal = text_image_normal.get_rect(center=self.rect.center)
        text_image_clicked = font.render(text_clicked, True, WHITE)
        text_rect_clicked = text_image_clicked.get_rect(center=self.rect.center)

        self.imgNormal.blit(text_image_normal, text_rect_normal)
        self.imgClicked.blit(text_image_clicked, text_rect_clicked)
        self.imgClicked = self.imgNormal if text_normal == text_clicked else self.imgClicked

        self.rect.center = (x, y)
        self.state = False

    def draw(self, win):
        win.blit(self.image, self.rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.state = not self.state
            self.image = self.imgClicked if self.state else self.imgNormal
            if self.command:
                self.command()


class TextBox(object):
    def __init__(self, game, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COL_INACTIVE
        self.text = text
        self.game = game
        self.font = pygame.font.Font(None, 24)
        self.textSurface = self.font.render(text, True, self.color)
        self.active = False

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COL_ACTIVE if self.active else COL_INACTIVE
        if event.type == pygame.KEYDOWN and self.active:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.game.ROWS = int(self.text)
                self.game._resetBtn()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.textSurface = self.font.render(self.text, True, self.color)

    def draw(self, win):
        win.blit(self.textSurface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(win, self.color, self.rect, 2)


def draw_text(win, text, size, color, x, y):
    font = pygame.font.SysFont('arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surface, text_rect)
