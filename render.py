import numpy as np
import pygame


def render():
    GRID_SIZE = 64
    SQUARE_SIZE = 16  # Size of each square in pixels

    # Map numbers to colors (R, G, B)
    color_map = {
        1: (255, 0, 0),   # Red
        2: (0, 255, 0),   # Green
        3: (0, 0, 255),   # Blue
        4: (255, 255, 0), # Yellow
        5: (255, 0, 255)  # Magenta
    }

    # Generate a 64x64 grid with random integers from 1 to 5
    matrix = np.random.randint(1, 6, size=(GRID_SIZE, GRID_SIZE))

    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Procedural Generation Game')

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                number = matrix[row, col]  # Get the number from the matrix
                color = color_map[number]    # Map to color
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()