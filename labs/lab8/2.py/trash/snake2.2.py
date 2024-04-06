import pygame
import random
from game_object import GameObject
from game_object import Point  
from worm import Worm
from food import Food
from wall import Wall

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

foodPoints = [Point(120, 20)]
wallPoints = [Point(20, 200)]

worm = Worm(20)
food = Food(20, foodPoints)
wall = Wall(20, wallPoints)

score = 0
level = 1

def generateFood():
    if food.can_eat(worm.points[0]):                                                            #if function can_eat passes is already means that points are matched
        x1 = food.eat_points(worm.points[0]).X
        y1 = food.eat_points(worm.points[0]).Y
        
        index = 0
        for x in foodPoints:                                                                        #searching the index of eaten food in foodPoints list
            if x.X == x1 and x.Y == y1:
                break
            else:
                index += 1

    warmCheck = False
    wallsCheck = False

    point = Point

    while not warmCheck and not wallsCheck:
        p1 = random.randrange(0, 39) * 20
        p2 = random.randrange(0, 29) * 20

        for x in worm.points:
                if x.X == p1 and x.Y == p2:
                    warmCheck = True

        for x in wallPoints:
                if x.X == p1 and x.Y == p2:
                    wallsCheck = True

        warmCheck = not warmCheck
        wallsCheck = not wallsCheck

        point = Point(p1, p2)              
        
    foodPoints.pop(index)                                                                       #deliting old food point
    foodPoints.append(point)                                                                    #appending new food point

    return 0

while not done:
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        else:
            filtered_events.append(event)

    worm.process_input(filtered_events)
    worm.move()



    eaten = False

    pos1 = food.can_eat(worm.points[0])
    if(pos1 != None):
        worm.increase(pos1)                                                 #increasing worm is food eaten    
        score += 1                                                          #score counting
        eaten = True

    if eaten:       
        generateFood()                                                      #calling generateFood function if food is eaten
        eaten = False                                                       #
        


    pos2 = wall.collision(worm.points[0])
    if(pos2 != None): 
        pygame.quit()                                                       #quiting the game if wall was hitted 

    
    create_background(screen, 800, 600)
        
    food.draw(screen)
    wall.draw(screen)
    worm.draw(screen)

    font = pygame.font.Font(None, 35)                               
    scoreTxt = font.render(str(score), True, "black")
    levelTxt = font.render(str(level), True, "black")
    screen.blit(scoreTxt, [760, 20])                                        #score counter display 
    screen.blit(levelTxt, [10, 20])                                                 
        
    pygame.display.flip()
    clock.tick(8)