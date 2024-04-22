import pygame
import random
import time

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

foodColors = [(100,255,100), (0,140,0), (0,0,0)]                                                    #list of food colors
foodWeight = 1                                                                                      #starting food weight and color
foodColor = foodColors[foodWeight - 1]

def generateFood():                                                                                 #function to generate new food and delete old
    if food.can_eat(worm.points[0]):                                                            
        x1 = food.eat_points(worm.points[0]).X
        y1 = food.eat_points(worm.points[0]).Y
        
        index = 0                                           #finding the index of old food to pop
        for x in foodPoints:                                                                    
            if x.X == x1 and x.Y == y1:
                break
            else:
                index += 1

    while True:                                             #checking for intersection with worm and walls                                                    
        p1 = random.randrange(0, 39) * 20
        p2 = random.randrange(0, 29) * 20

        warmCheck = False
        wallsCheck = False

        for x in worm.points:
            if x.X == p1 and x.Y == p2:
                warmCheck = True                                                            

        for x in wall.points:                                                              
            if x.X == p1 and x.Y == p2:
                wallsCheck = True

        if not warmCheck and not wallsCheck:
            break    
        
    foodPoints.pop()                                                                                                                                                        #foodPoints.pop(index) for many foods on the screen
    foodPoints.append(Point(p1, p2))

    return 0

l1, l2, l3 = True, True, True                                                       #flags for next levels 

TimerActive = False                                                           #timer flag 
TimerStart = 0

while not done:
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)

    if done:
        break  

    worm.process_input(filtered_events)
    worm.move()

    eaten = False
    pos1 = food.can_eat(worm.points[0])
    if(pos1 != None):
        worm.increase(pos1)                                                
        score += foodWeight                                                 
        eaten = True

        if (score == 5 or score == 6 or score == 7) and l1:                                 #switching to next levels                                      
            wall.next_level()
            level += 1
            l1 = False
        elif (score == 10 or score == 11 or score == 12) and l2:                                                
            wall.next_level()
            level += 1
            l2 = False
        elif (score == 15 or score == 16 or score == 17) and l3:                                                
            wall.next_level()
            level += 1
            l3 = False

    if foodWeight == 3:                                                                                 #3 second timer for black food
        if not TimerActive:                                           
            TimerActive = True
            TimerStart = time.time()

        currentTime = time.time()  
        elapsedTime = currentTime - TimerStart
        if elapsedTime >= 3:
            generateFood()
            TimerActive = False

    if eaten:       
        eaten = False

        foodWeight = random.randrange(1,4)                                                              #generating new food weight (1-3)                                                      
        foodColor = foodColors[foodWeight - 1]

        generateFood()                                                     
    
    pos2 = wall.collision(worm.points[0])
    if(pos2 != None): 
        pygame.quit()                                                       

    create_background(screen, 800, 600)
        
    food.draw(screen, foodColor)
    wall.draw(screen)
    worm.draw(screen)

    font = pygame.font.Font(None, 35)                                                                   #displaying score and level info       
    scoreTxt = font.render(str(score), True, "black")
    levelTxt = font.render(str(level), True, "black")
    screen.blit(scoreTxt, [760, 20])                                        
    screen.blit(levelTxt, [20, 20])                                         
        
    pygame.display.flip()
    clock.tick((level * 3) + 5)                                                                         #increasing speed by 3 for every next level
