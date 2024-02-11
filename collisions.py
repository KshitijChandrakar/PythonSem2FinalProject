import pygame
import sys
from MyFunctions import *

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Draw Rectangle at Mouse Position")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up rectangle
rect_width = 50
rect_height = 50
rect_color = BLACK
rect = pygame.Rect(0, 0, rect_width, rect_height)
rect1 = pygame.Rect(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 - 50 , 100, 100)
# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update rectangle position to mouse position
    rect.x, rect.y = pygame.mouse.get_pos()
    if checkCollision(\
        rect.width, rect.height, rect.x, rect.y,\
        rect1.width, rect1.height, rect1.x, rect1.y
        ):
        print("Colliding")
        pass
        # Draw rectangle
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.rect(screen, rect_color, rect1)
    pygame.display.flip()
    # clock.tick(60)

pygame.quit()
sys.exit()
