import pygame
pygame.init()

display = pygame.display.set_mode((600, 800))
color = (200, 200, 0)
cond = True

left, top, width, height = 50, 50, 100, 100
r = pygame.Rect(left, top, width, height)

pygame.draw.rect(display, color, r, 20)
pygame.draw.circle(display, color, (300, 95), 60, 20)

while cond:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False
 
    pygame.display.flip()