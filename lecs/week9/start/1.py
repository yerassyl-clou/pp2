import pygame
pygame.init()

pygame.display.set_mode((500, 700))
pygame.display.set_caption("First programm on pygame")

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            go = False