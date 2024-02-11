import pygame
import random
from MyFunctions import *

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_width = 40
player_height = 20
player_x = 50
player_y = SCREEN_HEIGHT - player_height
player_vel_y = 0
jump_height = 10
gravity = 0.5
is_jumping = False

# Set up obstacles
obstacle_width = 20
obstacle_height = 40
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height
obstacle_vel_x = -5
obstacle_gap = 100
next_obstacle_distance = random.randint(200, 300)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_vel_y = -jump_height

    # Update player position
    if is_jumping:
        player_y += player_vel_y
        player_vel_y += gravity
        if player_y >= SCREEN_HEIGHT - player_height:
            player_y = SCREEN_HEIGHT - player_height
            is_jumping = False

    # Update obstacle position
    obstacle_x += obstacle_vel_x
    if obstacle_x < -obstacle_width:
        obstacle_x = SCREEN_WIDTH
        next_obstacle_distance = random.randint(200, 300)

    # Check collision
    if checkCollision(player_width, player_height, player_x, player_y,\
                    obstacle_width, obstacle_height, obstacle_x, obstacle_y
    ):
        running = False

    # Draw player and obstacle
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, 0, obstacle_width, obstacle_y))
    # pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y + obstacle_gap, obstacle_width, SCREEN_HEIGHT - (obstacle_y + obstacle_gap)))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
