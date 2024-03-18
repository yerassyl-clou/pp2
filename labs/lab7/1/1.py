import pygame
import datetime
pygame.init()

color = (255, 255, 255)
screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("Mickey Clock")

clock_image = pygame.image.load("labs/lab7/1/mainclock.png")
clock_rect = clock_image.get_rect(center=(700, 525))

hourArm = pygame.image.load("labs/lab7/1/rightarm.png")
minuteArm = pygame.image.load("labs/lab7/1/leftarm.png")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    hour = int(datetime.datetime.now().strftime("%I")) + 1.6                  
    minute = int(datetime.datetime.now().strftime("%M")) + 0.53                                     #Погрешность картинки

    hour_angle = -(hour * 30 + minute * 0.5)  
    minute_angle = -(minute * 6)  

    hourArmRotated = pygame.transform.rotate(hourArm, hour_angle)               
    hourArmRect = hourArmRotated.get_rect()                                                             #Получить прямоугольник из png
    hourArmRect.center = clock_rect.center                                                              #Точка вращения 

    rotated_minute_hand = pygame.transform.rotate(minuteArm, minute_angle)
    minuteArmRect = rotated_minute_hand.get_rect()                                                      #Получить прямоугольник из png
    minuteArmRect.center = clock_rect.center                                                            #Точка вращения

    screen.fill(color)
    screen.blit(clock_image, clock_rect)
    screen.blit(hourArmRotated, hourArmRect)
    screen.blit(rotated_minute_hand, minuteArmRect)

    pygame.display.flip()
