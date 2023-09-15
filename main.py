import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
FramesPerSec = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 400

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # (0,0) is in top-left corner, (300,300) in bottom-right corner
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, BLACK, pygame.Rect(30,30,60,60))

P1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    P1.draw()
    pygame.display.update()
    FramesPerSec.tick(FPS) # Puts a limit on how many FPS