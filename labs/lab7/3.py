import pygame
pygame.init()

w, h = 800, 600                                         #размеры окна 
x, y = 400, 300                                         #начальные координаты шара 

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

cond  = True
while cond:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cond = False
        
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y > 25: 
        y -= 20
    if pressed[pygame.K_DOWN] and y < h - 25:
        y += 20
    if pressed[pygame.K_LEFT] and x > 25: 
        x -= 20
    if pressed[pygame.K_RIGHT]and x < w - 25: 
        x += 20

    screen.fill(("white"))
    pygame.draw.circle(screen, "red", (x, y), 25)

    pygame.display.flip()
    clock.tick(120)