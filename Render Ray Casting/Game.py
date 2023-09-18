from Particle import *
from random import sample
from math import tan


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.walls = []
        self.walls.extend([Boundary(*sample(range(0, HEIGHT), 4))
                          for _ in range(5)])
        for i in ((0, 0, 0, HEIGHT), (0, 0, WIDTH, 0), (WIDTH-1, HEIGHT-1, WIDTH, 0), (WIDTH-1, HEIGHT-1, 0, HEIGHT), (HEIGHT, 0, HEIGHT, HEIGHT)):
            self.walls.append(Boundary(*i))
        self.s = None
        self.particle = Particle(HEIGHT//2, HEIGHT//4)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = False
                elif event.key == pygame.K_q:
                    self.particle.updateFOV(45)
                elif event.key == pygame.K_e:
                    self.particle.updateFOV(-45)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if self.s is None:
                    self.s = pygame.Vector2(*event.pos)
                else:
                    self.walls.append(Boundary(self.s.x, self.s.y, *event.pos))
                    self.s = None

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.particle.rotate(-1)
        elif keys[pygame.K_RIGHT]:
            self.particle.rotate(1)
        elif keys[pygame.K_UP]:
            self.particle.move(2)
        elif keys[pygame.K_DOWN]:
            self.particle.move(-2)

    def draw(self):
        self.screen.fill(BLACK)
        for wall in self.walls:
            wall.draw(self.screen)
        if self.s:
            b = Boundary(self.s.x, self.s.y, *pygame.mouse.get_pos())
            b.draw(self.screen)
        pos = pygame.mouse.get_pos()
        if pos:
            self.particle.update(pos)
        distProjPlane = HEIGHT / 2 / tan(self.particle.fov//2)
        scenes = self.particle.look(self.walls)
        w = HEIGHT // len(scenes)
        wsq = HEIGHT*HEIGHT
        for i, scene in enumerate(scenes):
            sq = scene*scene
            b = sMap(sq, 0, wsq, 255, 0)
            print(b, sq, scene, i)
            h = int((HEIGHT/scene) * distProjPlane)
            c = (b, b, b)
            r = pygame.Rect(0, 0, w+1, h)
            r.center = (HEIGHT+i*w + w//2, HEIGHT//2)
            pygame.draw.rect(self.screen, c, r)
        self.particle.draw(self.screen)
        pygame.display.update()


def sMap(n, start1, stop1, start2, stop2):
    return int(start2 + ((n-start1) / (stop1-start1) * (stop2-start2)))


if __name__ == '__main__':
    game = Game()
    while game.running:
        game.run()
    pygame.quit()
