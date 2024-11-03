import pygame
import numpy as np
import os
from assets import AssetManager, Cloud
from random import randint
from tiles import TileManager
from generation import generate
from render import render

#DEBUG
ALPHA = 50
# Initialize Pygame
pygame.init()

# Set up display
GRID_SIZE = 40  # 64x64 grid
TILE_SIZE = 16  # Each image tile is 16x16 pixels
RADIUS = 3  # Radius of the cloud
screen_width = GRID_SIZE * TILE_SIZE
screen_height = GRID_SIZE * TILE_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid of Images")
AssetManager.load()
Cloud.load()
screen.fill((0, 0, 0))

world_arr = generate((GRID_SIZE, GRID_SIZE))
cloud_arr = np.full((GRID_SIZE, GRID_SIZE), ALPHA, dtype=np.int16)

s=0.5 #GLOBAL ALERT
# Main loop - away from here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            centre_x = i * TILE_SIZE + TILE_SIZE // 2
            centre_y = j * TILE_SIZE + TILE_SIZE // 2
            distance = ((centre_x - mouse_x) ** 2 + (centre_y - mouse_y) ** 2) ** 0.5
            cloud_arr[j][i] -= int(max(0,(RADIUS*TILE_SIZE - distance)*s))
            cloud_arr[j][i] = min(255,max(0, cloud_arr[j][i]))

    render(screen, world_arr, cloud_arr )

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
