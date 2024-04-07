import pygame
import sys
import math

def getEquilateralTriangle(x1, y1, x2, y2):
    # Calculate the length of the side of the equilateral triangle
    side_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # Calculate the coordinates of the third vertex based on the mouse position
    x3 = x1 + side_length * math.cos(math.radians(30))  # 30 degrees for equilateral triangle
    y3 = y1 - side_length * math.sin(math.radians(30))
    return [(x1, y1), (x2, y2), (x3, y3)]

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 1000, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Resizable Equilateral Triangle")

# Variables
done = False
clock = pygame.time.Clock()
color = (255, 255, 255)
isMouseDown = False
triangle = []

while not done:
    screen.fill((0, 0, 0))  # Fill the screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x1, y1 = pygame.mouse.get_pos()
                isMouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isMouseDown = False
                x2, y2 = pygame.mouse.get_pos()
                triangle = getEquilateralTriangle(x1, y1, x2, y2)
        elif event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2, y2 = pygame.mouse.get_pos()
                triangle = getEquilateralTriangle(x1, y1, x2, y2)

    # Draw the triangle if it contains at least 3 points
    if len(triangle) >= 3:
        pygame.draw.polygon(screen, color, triangle, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
