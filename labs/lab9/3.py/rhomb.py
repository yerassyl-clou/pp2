import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rhombus")

# Variables
done = False
clock = pygame.time.Clock()
color = (255, 255, 255)
isMouseDown = False
rhombus = []

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
                # Calculate width and height of the rhombus
                width_rhombus = abs(x2 - x1)
                height_rhombus = abs(y2 - y1)
                rhombus = [(x1 + width_rhombus // 2, y1), (x2, y1 + height_rhombus // 2), (x1 + width_rhombus // 2, y2), (x1, y1 + height_rhombus // 2)]  # Define the vertices of the rhombus
        elif event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2, y2 = pygame.mouse.get_pos()
                width_rhombus = abs(x2 - x1)
                height_rhombus = abs(y2 - y1)
                rhombus = [(x1 + width_rhombus // 2, y1), (x2, y1 + height_rhombus // 2), (x1 + width_rhombus // 2, y2), (x1, y1 + height_rhombus // 2)]

    # Draw the rhombus if it contains at least 4 points
    if len(rhombus) >= 4:
        pygame.draw.polygon(screen, color, rhombus, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
