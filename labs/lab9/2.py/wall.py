import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):
    def __init__(self, tile_width):                             #, points
        super().__init__([], (255,0,0), tile_width)             #points
        self.level = 1
        self.load_level()

    def collision(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
    
    def load_level(self):
        f = open("/Users/yerassyl/vscode/kbtu/pp2/labs/lab9/2.py/levels/level{}.txt".format(self.level), "r")                      #/Users/yerassyl/vscode/kbtu/pp2/labs/lab8/2.py/levels/level{}.txt
        row = -1
        col = -1
        for line in f:
            row = row + 1
            col = -1
            for c in line:
                col = col + 1
                if c == '#':
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        f.close()

    def next_level(self):
        self.points = []
        
        if self.level == 4:
            self.level = 1
        else:
            self.level += 1
        
        self.load_level()