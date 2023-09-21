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
pygame.display.set_caption("Game")

PLAYER_SPEED = 5

ground = pygame.Rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT / 2)
ground.center = (SCREEN_WIDTH / 2,0)
ground.top = SCREEN_HEIGHT / 1.25

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Rect = pygame.Rect(0,0,40,40) # Create square size 40 by 40 pixels
        self.Rect.center = (SCREEN_WIDTH / 2,0) # Change start position of player
        self.Rect.bottom = SCREEN_HEIGHT / 1.25

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.Rect.move_ip(-PLAYER_SPEED, 0)
        if key[pygame.K_d]:
            self.Rect.move_ip(PLAYER_SPEED, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.Rect)

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, BLACK, ground)
    player.draw(DISPLAYSURF)
    player.move()
    pygame.display.update()
    FramesPerSec.tick(FPS) # Puts a limit on how many FPS