import pygame
import os

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (window)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Load Image Between Two Points")

# Load and resize image
image_path = os.path.join(os.path.dirname(__file__), 'ima.jpeg')
image = pygame.image.load(image_path).convert_alpha()  # Convert for better rendering
image = pygame.transform.scale(image, (100, 100))

# Define starting and ending points
start_point = (100, 100)
end_point = (500, 400)

# Create a rectangle to represent the image position and size
image_rect = pygame.Rect(start_point[0], start_point[1], image.get_width(), image.get_height())

# Calculate the velocity components
velocity_x = (end_point[0] - start_point[0]) / 100.0  # Adjust the divisor to control the speed
velocity_y = (end_point[1] - start_point[1]) / 100.0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Move the image rectangle
    image_rect.x += velocity_x
    image_rect.y += velocity_y

    # Render the image at the current position
    screen.blit(image, image_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
