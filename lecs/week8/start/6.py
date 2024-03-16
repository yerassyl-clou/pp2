import pygame 
pygame.init()

screen = pygame.display.set_mode((500,800))
r = pygame.Rect(50, 50, 100, 100)

is_blue = False



cond = True
while cond:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cond = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    if is_blue:
        color = ((0, 0, 255))
    else:
        color = (255, 128, 0)

    pygame.draw.rect(screen, color, r)

    pygame.display.flip() 

    
