import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
FramesPerSec = pygame.time.Clock()

WHITE = (255,255,255)

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 400

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # (0,0) is in top-left corner, (300,300) in bottom-right corner
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    pygame.display.update()
    FramesPerSec.tick(FPS) # Puts a limit on how many FPS