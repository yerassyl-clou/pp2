import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60 
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)  
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400                                                                                              #Other Variables for use in the program
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

font = pygame.font.SysFont("Verdana", 60)                                                                       #Setting up Fonts
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/AnimatedStreet.png")
coin_image = pygame.image.load("/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/coin.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1, 2)                                       #Random weight (1 or 2)
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

P1 = Player()                                                                   # Setting up Sprites
E1 = Enemy()

enemies = pygame.sprite.Group()                                                 #Creating Sprites Groups
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1                                                # Adding a new User event
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(ADD_COIN, 3000)

while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.25
        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coins_collected_text = font_small.render("Coins: " + str(COINS_COLLECTED), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected_text, (10, 30))

    for entity in all_sprites:                                                                              #Moves and Re-draws all Sprites
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):                                                         #To be run if collision occurs between Player and Enemy
        pygame.mixer.Sound('/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)                                          #Check for collision between Player and coins
    if coin_collisions:
        for coin in coin_collisions:
            COINS_COLLECTED += coin.weight                                                                  #Increase score by coin weight
            pygame.mixer.Sound('/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/1.py/coin_sound.wav').play()
        
        if COINS_COLLECTED % 2 == 0:
            SPEED += 0.25

    pygame.display.update()
    FramePerSec.tick(FPS)
