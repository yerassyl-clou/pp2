import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1000, 800))           #Задать экран
r = pygame.Rect(150, 150, 250, 200)                     #Создать прямоугольник с начальныим координатами и размерами 

pygame.draw.rect(screen, (255, 200, 255), r, 0)         #Отображение функцией rect() На поверхности screen, определенным цветом прямоугольника r, толщиной 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()                               #отображение изменений


"""

rect(Surface, color, Rect, width=0)                                 Прямоугольник

line(Surface, color, start_pos, end_pos, width=1)                   Линия

lines(Surface, color, closed, pointlist, width=1)                   Линия, соединяющую точки из последовательности pointlist        (Каждая точка представлена парой координат. Если параметр closed равен True, конечная точка соединяется с начальной.)

circle(Surface, color, pos, radius, width=0)                        Окружность

ellipse(Surface, color, Rect, width=0)                              Эллипс

polygon(Surface, color, pointlist, width=0)                         Многоугольник по точкам из последовательности pointlist


"""