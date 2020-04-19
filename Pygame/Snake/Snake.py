import pygame
from random import randint

RED = (255, 0, 0)
snk_size = 10
snk_list = []

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Snake')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


def showText(text, color, x, y, s=45):
    font = pygame.font.Font(None, s)
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))


def newFood():
    while True:
        x = randint(50, 650)
        y = randint(50, 650)
        if not (x, y) in snk_list: break
    return x, y


def draw_snk(win):
    for pos in snk_list:
        pygame.draw.circle(win, (0, 0, 0), pos, snk_size)


def welcome():
    exit_game = False
    while not exit_game:
        screen.fill((233, 210, 229))
        showText('Welcome to the Snake World', RED, 80, 200, 60)
        showText('Press Space Bar to Continue', RED, 150, 260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: exit_game = True
                if event.key == pygame.K_SPACE:
                    exit_game = True
                    mainloop()
        pygame.display.update()


def mainloop():
    snk_x = snk_y = 350
    snk_dx = snk_dy = 0
    snk_vel = 2
    snk_length = 1
    food_x = randint(50, 650)
    food_y = randint(50, 650)
    score = 0
    fps = 60
    running = fairplay = True
    game_over = False
    with open('hiscore.txt', 'r') as f:
        hiscore = f.read()
    while running:
        clock.tick(fps)
        screen.fill((150, 255, 255))
        # for x in range(0,700,25):
        #     pygame.draw.line(screen, (204,204,204), (x,0), (x,700), 2)
        #     pygame.draw.line(screen, (204,204,204), (0,x), (700,x), 2)
        if game_over:
            showText('Score : ' + str(score) +
                     '  High Score : ' + str(hiscore), RED, 20, 20)
            showText('GAME OVER!!!', RED, 200, 200, 64)
            showText('Press "Enter" key to Continue', RED, 150, 260)
            snk_list.clear()
            if fairplay:
                with open('snake hiscore.txt', 'w') as f:
                    f.write(str(hiscore))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: running = False
                    if event.key == pygame.K_RETURN:
                        running = False
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: running = False
                    if event.key == pygame.K_PAGEUP: fps += 10
                    if event.key == pygame.K_PAGEDOWN: fps -= 10
                    if fps < 10: fps = 10
                    if fps > 120: fps = 120
                    if event.key == pygame.K_q:
                        fairplay = False
                        score += 10
                        snk_length += 10
                    if event.key == pygame.K_RIGHT:
                        snk_dx = snk_vel
                        snk_dy = 0
                    if event.key == pygame.K_LEFT:
                        snk_dx = snk_vel * -1
                        snk_dy = 0
                    if event.key == pygame.K_UP:
                        snk_dx = 0
                        snk_dy = snk_vel * -1
                    if event.key == pygame.K_DOWN:
                        snk_dx = 0
                        snk_dy = snk_vel
            snk_x += snk_dx
            snk_y += snk_dy
            snk_list.append((snk_x, snk_y))
            if len(snk_list) > snk_length: del snk_list[0]
            if (snk_x, snk_y) in snk_list[:-
                                          1] or not 0 < snk_x < 690 or not 0 < snk_y < 690: game_over = True
            if abs(snk_x - food_x) < 10 and abs(snk_y - food_y) < 10:
                score += 10
                snk_length += 10
                food_x, food_y = newFood()
                if score % 100 == 0: snk_vel += 1
            if int(hiscore) < score: hiscore = score
            showText('Score : ' + str(score) +
                     '  High Score : ' + str(hiscore), RED, 20, 20)
            pygame.draw.circle(screen, RED, (food_x, food_y), snk_size)
            draw_snk(screen)
        pygame.display.update()


welcome()
