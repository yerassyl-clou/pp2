import pygame 
pygame.init()

screen = pygame.display.set_mode((400, 300))

done = False

pygame.font.init()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
    
    font = pygame.font.Font(None, 25)
    text = font.render(str(score), True, "white")
    screen.blit(text, [25, 25])

    pygame.display.flip()
