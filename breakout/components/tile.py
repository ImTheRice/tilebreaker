import pygame
from .sprite import MySprite
import random

class Tile(MySprite):
    """Tile - meant to be hit with the ball"""

    def __init__(self, *args, color=(0,0,0), colors=[], width=100, height=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.colors = colors
        if self.colors == []:
            self.colors = [(247, 37, 133), (114, 9, 183), (58, 12, 163), (67, 97, 238), (76, 201, 240)]
        self.image = pygame.Surface((width, height))
        if color == (0,0,0):
            self.image.fill(random.choice(self.colors))
        else:
            self.image.fill(color)
        self.rect = self.image.get_rect()
