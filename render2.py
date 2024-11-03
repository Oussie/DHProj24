import pygame
import numpy as np
import os
from assets import AssetManager
from random import randint
from tiles import TileManager
from generation import generate

# Initialize Pygame
pygame.init()

# Set up display
GRID_SIZE = 40       # 64x64 grid
TILE_SIZE = 16       # Each image tile is 16x16 pixels
screen_width = GRID_SIZE * TILE_SIZE
screen_height = GRID_SIZE * TILE_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid of Images")
AssetManager.load()
screen.fill((0, 0, 0))

arr = generate((GRID_SIZE, GRID_SIZE))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # Draw the grid using blit
    for y,row in enumerate(arr):
        for x,id in enumerate(row):
            index = TileManager.get(id)["index"]
            tile = AssetManager.get(*index)

            # Blit the image at the calculated position
            screen.blit(tile, (x*TILE_SIZE, y*TILE_SIZE))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()