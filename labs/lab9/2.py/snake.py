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

worm = Worm(20)
food = Food(20, foodPoints)
wall = Wall(20)
            
score = 0
level = 1

foodWeight = 0

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


    while True:                                                                               # checking to wall and food collision 
            p1 = random.randrange(0, 39) * 20
            p2 = random.randrange(0, 29) * 20

            warmCheck = False
            wallsCheck = False

            for x in worm.points:
                if x.X == p1 and x.Y == p2:
                    warmCheck = True                                                            #warm

            for x in wall.points:                                                               #wall
                if x.X == p1 and x.Y == p2:
                    wallsCheck = True

            if not warmCheck and not wallsCheck:
                break    
        
    foodPoints.pop(index)                                                                       #deliting old food point
    foodPoints.append(Point(p1, p2))                                                            #appending new food point

    return 0

l1, l2, l3 = True, True, True

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
        foodWeight = random.randrange(1,3)
        score += foodWeight                                                 #score counting
        eaten = True

        if (score == 5 or score == 6) and l1:                                                  #going to next level if score is increased by 5
            wall.next_level()
            level += 1
            l1 = False
        elif (score == 10 or score == 11) and l2:                                                  #going to next level if score is increased by 5
            wall.next_level()
            level += 1
            l2 = False
        elif (score == 15 or score == 16) and l3:                                                  #going to next level if score is increased by 5
            wall.next_level()
            level += 1
            l3 = False

    if foodWeight == 1:
        #foodColor = (100, 255, 100)
        foodColor = (0, 140, 0)
    else: 
        #foodColor = (0, 140, 0)
        foodColor = (100, 255, 100)

    if eaten:       
        generateFood()                                                      #calling generateFood function if food is eaten
        eaten = False
                                                               
    pos2 = wall.collision(worm.points[0])
    if(pos2 != None): 
        pygame.quit()                                                       #quiting the game if wall was hitted 

    
    create_background(screen, 800, 600)
        
    food.draw(screen, foodColor)
    wall.draw(screen)
    worm.draw(screen)

    font = pygame.font.Font(None, 35)                               
    scoreTxt = font.render(str(score), True, "black")
    levelTxt = font.render(str(level), True, "black")
    screen.blit(scoreTxt, [760, 20])                                        #score counter display 
    screen.blit(levelTxt, [20, 20])                                         #level counter display
        
    pygame.display.flip()
    clock.tick((level) + 5)