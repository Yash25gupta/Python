import pygame
from pygame.locals import *
from random import randint
# from lib import Cell
from math import floor
from lib.Cell import Cell

#CUSTOMISABLE GLOBALS
WIDTH = 800
HEIGHT = 600
FULL_SCREEN = False
DRAW_GRID = False
colours = {'black': (0 ,0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'orange': (255, 165, 0), 'True': (0, 130, 0), 'False': (130, 0, 0)}
DIAGONALS = True
GRID_SIZE = (60, 40)

#Initialise Pygame and alogrithm
pygame.init()
pygame.display.set_caption("A* Path Finder by Pstefa")
if FULL_SCREEN:
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
else:
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("arial", 12)
RUNNING = True
EXECUTING = False
CELL_SIZE = (WIDTH/GRID_SIZE[0], (HEIGHT-25)/GRID_SIZE[1])
START = Cell(0, 0)
END = Cell(GRID_SIZE[0] - 1, GRID_SIZE[1] - 1)
WALLS = []
OPEN = []
CLOSED = []
SOLUTION = []

mouse_is_down = False
w_is_down = False
r_is_down = False

#Initialize Cells


def set_wall(mouse_pos):
    x = floor(mouse_pos[0]/CELL_SIZE[0])
    y = floor(mouse_pos[1]/CELL_SIZE[1])
    for wall in WALLS:
        if wall.x == x and wall.y == y:
            return    
    WALLS.append(Cell(x, y))
            
def remove_wall(mouse_pos):
    x = floor(mouse_pos[0]/CELL_SIZE[0])
    y = floor(mouse_pos[1]/CELL_SIZE[1])
    for wall in enumerate(WALLS):
        if wall[1].x == x and wall[1].y == y:
            WALLS.pop(wall[0])
            return

def set_start(mouse_pos):
    global START
    x = floor(mouse_pos[0]/CELL_SIZE[0])
    y = floor(mouse_pos[1]/CELL_SIZE[1])
    START = Cell(x, y)

def set_end(mouse_pos):
    global END
    x = floor(mouse_pos[0]/CELL_SIZE[0])
    y = floor(mouse_pos[1]/CELL_SIZE[1])
    END = Cell(x, y)

def reset():
    global OPEN, CLOSED, SOLUTION, WALLS, START, END
    OPEN = []
    CLOSED = []
    SOLUTION = []
    START = Cell(0, 0)
    END = Cell(GRID_SIZE[0] - 1, GRID_SIZE[1] - 1)

def setup():
    global w_is_down, r_is_down, RUNNING, EXECUTING, START, OPEN, DRAW_GRID, DIAGONALS, WALLS
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_w:
                w_is_down = False
            elif event.key == K_r:
                r_is_down = False
            elif event.key == K_s and pygame.mouse.get_pos()[1] < HEIGHT-25:
                set_start(pygame.mouse.get_pos())
            elif event.key == K_e and pygame.mouse.get_pos()[1] < HEIGHT-25:
                set_end(pygame.mouse.get_pos())
            elif event.key == K_g:
                DRAW_GRID = not DRAW_GRID
            elif event.key == K_d:
                DIAGONALS = not DIAGONALS
            elif event.key == K_c:
                WALLS = []
        elif event.type == KEYDOWN:
            if len(SOLUTION) != 0:
                reset()
            if event.key == K_ESCAPE:
                RUNNING = False
            if event.key == K_w:
                w_is_down = True
            if event.key == K_r:
                r_is_down = True
            if event.key == K_SPACE and len(OPEN) == 0:
                START.f = 0
                OPEN = [START]
                EXECUTING = True
        elif event.type == QUIT:
            RUNNING = False
    
    if w_is_down and pygame.mouse.get_pos()[1] < HEIGHT-25:
        set_wall(pygame.mouse.get_pos())
    if r_is_down and pygame.mouse.get_pos()[1] < HEIGHT-25:
        remove_wall(pygame.mouse.get_pos())

def render_text():
    diagonals = FONT.render(f"Diagonals: {DIAGONALS}", True, colours[f'{DIAGONALS}'])
    draw_grid = FONT.render(f"Draw Grid: {DRAW_GRID}", True, colours[f'{DRAW_GRID}'])
    SCREEN.blit(diagonals, (0, HEIGHT - diagonals.get_height()))
    pygame.draw.line(SCREEN, colours['black'], (diagonals.get_width() + 3, HEIGHT-20), (diagonals.get_width()+3, HEIGHT))
    SCREEN.blit(draw_grid, (diagonals.get_width() + 6, HEIGHT - draw_grid.get_height()))
    controls = FONT.render("Toggle Diagonals: D, Toggle Grid: G, Remove Wall: R, Place Wall: W, Set Start: S, Set End: E, Clear: C, Start/Cancel Search: SPACE", True, colours['black'])
    lineX = diagonals.get_width() + draw_grid.get_width() + 10
    pygame.draw.line(SCREEN, colours["black"], (lineX, HEIGHT-20), (lineX, HEIGHT))
    SCREEN.blit(controls, (lineX + 5, HEIGHT - diagonals.get_height()))

def render_cells():
    SCREEN.fill((255, 255, 255))
    #Render cells
    CELLx = CELL_SIZE[0] + 1
    CELLy = CELL_SIZE[1] + 1
    for wall in WALLS:
        cell = pygame.Rect((wall.x*CELL_SIZE[0], wall.y*CELL_SIZE[1]), (CELLx, CELLy))            
        pygame.draw.rect(SCREEN, colours['black'], cell)
    for cell in OPEN:
        CELL = pygame.Rect((cell.x*CELL_SIZE[0], cell.y*CELL_SIZE[1]), (CELLx, CELLy))
        pygame.draw.rect(SCREEN, colours['green'], CELL)
    for cell in CLOSED:
        CELL = pygame.Rect((cell.x*CELL_SIZE[0], cell.y*CELL_SIZE[1]), (CELLx, CELLy))
        pygame.draw.rect(SCREEN, colours['red'], CELL)
    for cell in SOLUTION:
        CELL = pygame.Rect((cell.x*CELL_SIZE[0], cell.y*CELL_SIZE[1]), (CELLx, CELLy))
        pygame.draw.rect(SCREEN, colours['orange'], CELL)
    start = pygame.Rect((START.x*CELL_SIZE[0], START.y*CELL_SIZE[1]), (CELLx, CELLy))
    end = pygame.Rect((END.x*CELL_SIZE[0], END.y*CELL_SIZE[1]), (CELLx, CELLy))
    pygame.draw.rect(SCREEN, colours['blue'], start)
    pygame.draw.rect(SCREEN, colours['red'], end)        

    if DRAW_GRID:
        for i in range(GRID_SIZE[0]):
            pygame.draw.line(SCREEN, colours['black'], (i * CELL_SIZE[0], 0), (i * CELL_SIZE[0], HEIGHT-25))
        for j in range(GRID_SIZE[1] + 1):
            pygame.draw.line(SCREEN, colours['black'], (0, j * CELL_SIZE[1]), (WIDTH, j * CELL_SIZE[1]))

def return_f(node):
    return node.f

def in_wall(x, y):
    for wall in enumerate(WALLS):
        if wall[1].x == x and wall[1].y == y:
            return True
    return False

def in_open(x, y):
    for node in OPEN:
        if node.x == x and node.y == y:
            return (True, node)
    return (False, None)

def in_closed(x, y):
    for node in CLOSED:
        if node.x == x and node.y == y:
            return (True, node)
    return (False, None)

def find_child_nodes(Q_Node):
    children = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            new_x = Q_Node.x + x
            new_y = Q_Node.y + y
            if DIAGONALS:
                if not in_wall(new_x, new_y) and (new_x != Q_Node.x or new_y != Q_Node.y) and new_y >= 0 and new_y < GRID_SIZE[1] and new_x >= 0 and new_x < GRID_SIZE[0]:
                    children.append(Cell(new_x, new_y))
                    children[-1].calc_h(END)
                    children[-1].set_parent(Q_Node)
            else:
                if not in_wall(new_x, new_y) and (new_x == Q_Node.x or new_y == Q_Node.y) and new_y >= 0 and new_y < GRID_SIZE[1] and new_x >= 0 and new_x < GRID_SIZE[0]:
                    children.append(Cell(new_x, new_y))
                    children[-1].calc_h(END)
                    children[-1].set_parent(Q_Node)
    return children

def recurse_solution(node):
    if node.parent == None:
        return True
    SOLUTION.append(node)
    return recurse_solution(node.parent)

def execute():
    global RUNNING, OPEN, CLOSED, END, START, EXECUTING
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Path finding canceled, resetting.")
                EXECUTING = False
                reset()
    if len(OPEN) == 0:
        print("No solution, Press any key to reset!")
        EXECUTING = False
        reset()
        return
    OPEN.sort(key=return_f)
    Q_Node = OPEN[0]
    OPEN.pop(0)
    if Q_Node.x == END.x and Q_Node.y == END.y:
        print("Path found, Press any key to reset!")
        EXECUTING = False
        recurse_solution(Q_Node)
        print(f"Path length: {len(SOLUTION)}")
        OPEN = []
        CLOSED = []
    children = find_child_nodes(Q_Node)
    for child in children:
        _in_closed = in_closed(child.x, child.y)
        if _in_closed[0]:
            continue
        child.calc_g(Q_Node)
        child.calc_f()
        _in_open = in_open(child.x, child.y)
        if not _in_open[0]:
            OPEN.append(child)
    CLOSED.append(Q_Node)

while RUNNING:
    if not EXECUTING:
        setup()
    else:
        execute()
    render_cells()
    render_text()
    pygame.display.flip()
