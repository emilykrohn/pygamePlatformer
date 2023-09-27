import pygame, sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

FPS = 60
FramesPerSec = clock

delta = clock.tick(FPS) / 1000

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
        self.Rect.centerx = (SCREEN_WIDTH / 2.0)
        self.Rect.centery = (SCREEN_HEIGHT / 1.25 - self.Rect.height / 2)

        self.isJump = False
        self.velocity = 0
        self.GRAVITY = 9
        self.JUMPHEIGHT = 4

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.Rect.move_ip(-PLAYER_SPEED, 0)
        if key[pygame.K_d]:
            self.Rect.move_ip(PLAYER_SPEED, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.Rect)

    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.isJump: # Doesn't let the player jump again until they touch the ground
            self.isJump = True
            self.velocity = -self.JUMPHEIGHT # Initial velocity

        if self.isJump:
            self.velocity += self.GRAVITY * delta # Decrease the velocity over time
            self.Rect.bottom += self.velocity

        if self.Rect.bottom >= ground.top: # Stop the player from falling through the ground
            self.isJump = False # Lets the player jump again
            self.velocity = 0

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    player.jump()
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, BLACK, ground)
    player.draw(DISPLAYSURF)
    player.move()
    pygame.display.update()
    FramesPerSec.tick(FPS) # Puts a limit on how many FPS