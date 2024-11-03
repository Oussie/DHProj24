import pygame
import os


class _AssetManager:
    def __init__(self):
        # No need to initialize Pygame here, it's done in render2.py
        self.surface = None
        self.tile_size = 16
    def load(self):
        self.surface = pygame.image.load("assets/tileset.png").convert()
    def get(self, x, y):
        if not self.surface:
            raise RuntimeError(
                "Surface not loaded. Call load() after Pygame display is set."
            )
        square = pygame.Rect(
            x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size
        )
        sub_surface = self.surface.subsurface(square)
        return sub_surface

    def get_size(self):
        return self.tile_size


AssetManager = _AssetManager()
