import pygame
pygame.init()

screen = pygame.Surface((100, 100), pygame.SRCALPHA)
image = pygame.image.load('lecs/week8/ball.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
