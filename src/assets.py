import pygame
import os

class _AssetManager:

    def __init__(self):
        # No need to initialize Pygame here, it's done in render2.py
        self.surface = None

    def load(self):
        # Load image here after display is set
        self.surface = pygame.image.load('../assets/tileset.png').convert()

    def get(self, x, y):
        if not self.surface:
            raise RuntimeError("Surface not loaded. Call load() after Pygame display is set.")
        square = pygame.Rect(x, y, 16, 16)
        sub_surface = self.surface.subsurface(square)
        return sub_surface

AssetManager = _AssetManager()