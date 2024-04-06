import pygame
import random
from game_object import GameObject 
from game_object import Point 

class Food(GameObject):
    def __init__(self, tile_width, points):
        super().__init__(points, (0, 255, 0), tile_width)
    
    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
    
    def eat_points(self, head_location):
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                break
        return Point(point.X, point.Y)
    
    def draw(self, screen, color):
        for point in self.points:
            pygame.draw.rect(screen, color, pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width), 1)
    