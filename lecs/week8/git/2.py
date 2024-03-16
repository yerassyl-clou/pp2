import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False
is_blue = True

x, y = 30, 30

clock = pygame.time.Clock()

while not done:    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y -= 5
    if pressed[pygame.K_DOWN]: y += 5
    if pressed[pygame.K_LEFT]: x -= 5
    if pressed[pygame.K_RIGHT]: x += 5

    screen.fill((0, 0, 0))

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 128, 0)

    r = pygame.Rect(x, y, 60, 60)

    pygame.draw.rect(screen, color, r)

    pygame.display.flip()
    clock.tick(60)