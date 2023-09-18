from settings import *
from map import Map
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.playing = True
        self.load_data()

    def load_data(self):
        self.map = Map(self, 1)
        self.player = Player(self)

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                self.playing = False
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
                dx = event.pos[0] - HALF_WIDTH
                self.player.angle += dx * MOUSE_SENSITIVITY
                self.player.angle %= 360
            
    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    g = Game()
    while g.playing:
        g.run()
    pygame.quit()
