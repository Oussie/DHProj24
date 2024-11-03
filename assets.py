import pygame
import os
import random

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

class _Cloud:
    def __init__(self):
        # No need to initialize Pygame here, it's done in render2.py
        self.surface = None
        self.tile_size = 16
    def load(self):
        self.surface = self.image = pygame.Surface(
            (self.tile_size, self.tile_size), pygame.SRCALPHA
        )  # Transparent surface for the cloud
        self.image.fill((255, 255, 255)) 
    def get(self, alpha):
        if not self.surface:
            raise RuntimeError(
                "Surface not loaded. Call load() after Pygame display is set."
            )
    
        

        cloud_colour = (
            random.randint(240, 255), 
            random.randint(240, 255),
            random.randint(240, 255),
            alpha,
        )
                
        self.surface.fill(cloud_colour)
        return self.surface

    def get_size(self):
        return self.tile_size
    
AssetManager = _AssetManager()
Cloud = _Cloud()