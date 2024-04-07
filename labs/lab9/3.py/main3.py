import pygame

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

def drawSquare(screen, color, x1, y1, x2, y2):
    width_square = abs(x2 - x1)
    height_square = abs(y2 - y1)
    side_length = min(width_square, height_square)
    x2 = x1 + side_length * (1 if x2 > x1 else -1)
    y2 = y1 + side_length * (1 if y2 > y1 else -1)
    square = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
    pygame.draw.polygon(screen, color, square, 5)

def getTriangle(x1, y1, x2, y2):
    x3 = x1
    y3 = y2
    return [(x1, y1), (x2, y2), (x3, y3)]

pygame.init()
screen = pygame.display.set_mode((1000, 750))
another_layer = pygame.Surface((1000, 750))

done = False
clock = pygame.time.Clock()

colorCnt = 0

eventType = 0                                                       #0 - rectangle              1 - circle 


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
            eventType = (eventType + 1) % 4
            

        if pressed[pygame.K_e]:                                                     #switch to eraser 
            eventType = 4

        if pressed[pygame.K_r]:                                                     #clear screen
                screen.fill("black")
                another_layer.fill("black")

        if eventType == 0:                                                           #draw rectangle 
            pygame.draw.rect(screen, "black", (10, 10, 40, 40))
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
                        pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 5)


        if eventType == 1:                                                                      #draw circle
            pygame.draw.rect(screen, "black", (10, 10, 40, 40))
            pygame.draw.circle(screen, color, (20, 20), 10, 2)
            pygame.draw.circle(another_layer, color, (20, 20), 10, 2)

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
                        pygame.draw.ellipse(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 5)
                       
        if eventType == 4:                                                                                        #eraser
            pygame.draw.rect(screen, "black", (10, 10, 40, 40))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    x1 = event.pos[0]
                    y1 = event.pos[1]
                    x2 = x1
                    y2 = y1
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False
                    
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    x1 = x2
                    y1 = y2
                    x2 = event.pos[0]
                    y2 = event.pos[1]
                    another_layer.blit(screen, (0, 0)) 
                    pygame.draw.line(screen, "black", (x1, y1), (x2, y2), 15)

        if eventType == 2:                                                                                        #square
            pygame.draw.rect(screen, "black", (10, 10, 40, 40))
            pygame.draw.rect(screen, color, (10, 10, 20, 20), 2)
            pygame.draw.rect(another_layer, color, (10, 10, 20, 20), 2)

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
                    drawSquare(screen, color, x1, y1, x2, y2)

        if eventType == 3:                                                                                        #right triangle
            pygame.draw.rect(screen, "black", (10, 10, 40, 40))
            pygame.draw.polygon(screen, color, getTriangle(10, 10, 20, 30), 2)
            pygame.draw.polygon(another_layer, color, getTriangle(10, 10, 20, 30), 2)

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
                    triangle = getTriangle(x1, y1, x2, y2)
                    pygame.draw.polygon(screen, color, triangle, 5)

    pygame.display.flip()
    clock.tick(120)
