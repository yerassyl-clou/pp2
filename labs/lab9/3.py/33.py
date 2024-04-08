import pygame

def getRhombus(x1, x2, y1, y2):
    height = abs(y2 - y1)

    return [(x1, (y1 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y2), (x2, (y1 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y1)]

pygame.init()
screen = pygame.display.set_mode((1000, 750))
another_layer = pygame.Surface((1000, 750))

done = False
clock = pygame.time.Clock()

colorCnt = 0

eventType = 0                                                      


x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100

colors = ["white", "yellow", "red", "blue", "purple", "orange", "green", "cyan"]
isMouseDown = False
screen.fill((0, 0, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        pressed = pygame.key.get_pressed()

        color = colors[colorCnt]

        if pressed[pygame.K_c]:                                                     #change colors 
            colorCnt += 1
            color = colors[colorCnt]
            if colorCnt >= len(colors) - 1:
                colorCnt = 0

        if pressed[pygame.K_SPACE]:                                                 #switch between rect and circle 
            eventType = (eventType + 1) % 5
            

        if pressed[pygame.K_e]:                                                     #switch to eraser 
            eventType = 5

        if pressed[pygame.K_r]:                                                     #clear screen
                screen.fill("black")
                another_layer.fill("black")

        if eventType == 0:                                                           #draw rectangle 
            pygame.draw.rect(screen, "black", (0, 0, 40, 40))
            pygame.draw.rect(another_layer, "black", (0, 0, 40, 40))
            pygame.draw.rect(screen, color, (10, 10, 20, 30), 2)
            pygame.draw.rect(another_layer, color, (10, 10, 20, 30), 2)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                    another_layer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                    if isMouseDown:
                        x2 = event.pos[0]
                        y2 = event.pos[1]
                        screen.blit(another_layer, (0, 0))
                        pygame.draw.polygon(screen, color, getRhombus(x1, x2, y1, y2), 5)


    pygame.display.flip()
    clock.tick(120)
