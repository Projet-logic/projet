import pygame
from pygame.locals import *
from formula_d import *
from connector_d import *
from Variable_constant_d import *

# pygame initialization
pygame.init()

# monitor settings and game parameters
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hashiwokakero")
font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()

# load images for the game
img_background = pygame.image.load("background.png")            #we gonna find a background on GG and add it
img_island = pygame.image.load("island.png")
img_bridge = pygame.image.load("bridge.png")

# function of game grid drawing
def draw_grid():
    for x in range(50, width, 50):
        pygame.draw.line(screen, GRAY, (x, 50), (x, height-50))
    for y in range(50, height, 50):
        pygame.draw.line(screen, GRAY, (50, y), (width-50, y))

# island (cercle) drawing function
def draw_island(node):
    screen.blit(img_island, (node.position[0]-25, node.position[1]-25))    
    text = font.render(str(node.weight), True, BLACK)
    screen.blit(text, (node.position[0]-10, node.position[1]-10))

# bridge drawing function
def draw_bridge(bridge):
    x1 = bridge.node1.position[0]
    y1 = bridge.node1.position[1]
    x2 = bridge.node2.position[0]
    y2 = bridge.node2.position[1]
    
    if x1 == x2:
        if y1 < y2:
            y1 += 25
            y2 -= 25
        else:
            y1 -= 25
            y2 += 25
        screen.blit(pygame.transform.rotate(img_bridge, 90), (x1-25, y1))
    elif y1 == y2:
        if x1 < x2:
            x1 += 25
            x2 -= 25
        else:
            x1 -= 25
            x2 += 25
        screen.blit(img_bridge, (x1, y1-25))

# game state update function
def update_game():
    screen.blit(img_background, (0, 0))
    draw_grid()

    for node in nodes:
        draw_island(node)

    for bridge in bridges:
        draw_bridge(bridge)

    pygame.display.update()

# game event handler function
def game_loop():
    running = True
    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        update_game()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
