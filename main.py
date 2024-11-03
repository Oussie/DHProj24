import pygame
import numpy as np
import os
from src.assets import AssetManager, Cloud
from random import randint
from src.tiles import TileManager
from src.generation import generate
from src.render import render
from settings import *
# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

screen_width = GRID_SIZE * TILE_SIZE
screen_height = GRID_SIZE * TILE_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid of Images")

AssetManager.load()
Cloud.load()
screen.fill(BACKGROUND_COLOR) #Initialisation of board

WORLD_POSITION = 0
WORLDS_ARR = dict()

while True:
    try:
        world_arr = generate((GRID_SIZE, GRID_SIZE))
        WORLDS_ARR[WORLD_POSITION] = world_arr
        break
    except:
        print("Error")

cloud_arr = np.full((GRID_SIZE, GRID_SIZE), ALPHA, dtype=np.int16)

# BUTTON CODE####################################

# Button settings
RIGHT_BUTTON_POS = (630, 20)
LEFT_BUTTON_POS = (570, 20)  
RIGHT_BUTTON_RECT = pygame.Rect(RIGHT_BUTTON_POS[0] - 20, RIGHT_BUTTON_POS[1] - 10, 20, 20)
LEFT_BUTTON_RECT = pygame.Rect(LEFT_BUTTON_POS[0], LEFT_BUTTON_POS[1] - 10, 20, 20)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Arrow drawing function
def draw_arrow(surface, position, direction):
    # Define points for arrows
    x, y = position
    arrow_dict = {
        "right": [(x, y), (x - 20, y - 10), (x - 20, y + 10)],
        "left": [(x, y), (x + 20, y - 10), (x + 20, y + 10)],
        "bottom": [(x, y), (x + 10, y - 20), (x - 10, y - 20)],
        "top": [(x, y), (x + 10, y + 20), (x - 10, y + 20)]
    }

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if mouse is over the arrow
    if direction == "right":
        arrow_color = WHITE if RIGHT_BUTTON_RECT.collidepoint(mouse_x, mouse_y) else BLACK
        pygame.draw.polygon(surface, arrow_color, arrow_dict["right"])
    elif direction == "left":
        arrow_color = WHITE if LEFT_BUTTON_RECT.collidepoint(mouse_x, mouse_y) else BLACK
        pygame.draw.polygon(surface, arrow_color, arrow_dict["left"])

# END BUTTON CODE ####################################

s = 1  # GLOBAL ALERT
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # BUTTON CODE####################################
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button down
            if RIGHT_BUTTON_RECT.collidepoint(event.pos):  # Check if mouse is over the right button
                WORLD_POSITION += 1
                if WORLD_POSITION in WORLDS_ARR:
                    world_arr = WORLDS_ARR[WORLD_POSITION]
                else:
                    while True:
                        try:
                            world_arr = generate((GRID_SIZE, GRID_SIZE))
                            cloud_arr = np.full((GRID_SIZE, GRID_SIZE), ALPHA, dtype=np.int16)
                            WORLDS_ARR[WORLD_POSITION] = world_arr
                            break
                        except:
                            print("Error")  # Exit the loop if the button is pressed
            elif LEFT_BUTTON_RECT.collidepoint(event.pos):  # Check if mouse is over the left button
                WORLD_POSITION -= 1
                if WORLD_POSITION in WORLDS_ARR:
                    world_arr = WORLDS_ARR[WORLD_POSITION]
                else:
                    while True:
                        try:
                            world_arr = generate((GRID_SIZE, GRID_SIZE))
                            cloud_arr = np.full((GRID_SIZE, GRID_SIZE), ALPHA, dtype=np.int16)
                            WORLDS_ARR[WORLD_POSITION] = world_arr
                            break
                        except:
                            print("Error")  # Exit the loop if the button is pressed

        # END BUTTON CODE ####################################

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            centre_x = i * TILE_SIZE + TILE_SIZE // 2
            centre_y = j * TILE_SIZE + TILE_SIZE // 2
            distance = ((centre_x - mouse_x) ** 2 + (centre_y - mouse_y) ** 2) ** 0.5
            cloud_arr[j][i] -= int(max(0, (RADIUS * TILE_SIZE - distance) * s))
            cloud_arr[j][i] = min(255, max(0, cloud_arr[j][i]))

    render(screen, world_arr, cloud_arr)

    # BUTTON CODE####################################
    draw_arrow(screen, RIGHT_BUTTON_POS, "right")
    draw_arrow(screen, LEFT_BUTTON_POS, "left")
    # END BUTTON CODE ####################################

    # Update display
    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
