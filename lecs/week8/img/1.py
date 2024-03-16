import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
cond = True
clock = pygame.time.Clock()

image = pygame.image.load("lecs/week8/img/ball.png")

surface = pygame.Surface((100, 100))

while cond:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False

    screen.fill((255, 255, 255))

    screen.blit(image, (20, 20))

    pygame.display.flip()
    clock.tick(60)