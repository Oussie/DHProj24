import pygame
import numpy as np
import os

print(os.getcwd())

# Initialize Pygame
pygame.init()

# Set up display
GRID_SIZE = 64       # 64x64 grid
TILE_SIZE = 16       # Each image tile is 16x16 pixels
screen_width = GRID_SIZE * TILE_SIZE
screen_height = GRID_SIZE * TILE_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid of Images")

# Load the image to use as a tile
tile_image = pygame.image.load("/Users/oscarlihou-smith/Desktop/durhack/DHProj24/src/test_texture.jpg")

# Generate a 64x64 grid with random numbers from 1 to 5
matrix = np.random.randint(1, 6, size=(GRID_SIZE, GRID_SIZE))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen background (optional, for clearing previous frame)
    screen.fill((0, 0, 0))

    # Draw the grid using blit
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Calculate position
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            # Blit the image at the calculated position
            screen.blit(tile_image, (x, y))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()