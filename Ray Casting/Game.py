from Particle import *
from random import sample


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.walls = []
        # self.walls.extend([Boundary(*sample(range(0, HEIGHT), 4)) for _ in range(5)])
        for i in ((0, 0, 0, HEIGHT), (0, 0, WIDTH, 0), (WIDTH-1, HEIGHT-1, WIDTH, 0), (WIDTH-1, HEIGHT-1, 0, HEIGHT)):
            self.walls.append(Boundary(*i))
        self.s = None
        self.particle = Particle()
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = False
                # elif event.key == pygame.K_UP:
                #     pass
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if self.s is None:
                    self.s = pygame.Vector2(*event.pos)
                else:
                    self.walls.append(Boundary(self.s.x, self.s.y, *event.pos))
                    self.s = None

    def draw(self):
        self.screen.fill(BLACK)
        for wall in self.walls:
            wall.draw(self.screen)
        if self.s:
            b = Boundary(self.s.x, self.s.y, *pygame.mouse.get_pos())
            b.draw(self.screen)
        self.particle.update(pygame.mouse.get_pos())
        self.particle.look(self.walls)
        self.particle.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
