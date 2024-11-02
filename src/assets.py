import pygame

class AssetManager:

    def __init__(self):
        pygame.init()
        self.surface = pygame.image.load('/Users/oscarlihou-smith/Desktop/durhack/DHProj24/assets/tileset.png').convert()
    
    def get(self, x, y):
        square = pygame.Rect(x, y, 16, 16)
        sub_surface = self.surface.subsurface(square)
        return sub_surface