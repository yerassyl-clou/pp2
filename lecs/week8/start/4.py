import pygame
from pygame.color import THECOLORS

screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['white'])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()