import pygame
from .tile import Tile


class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30, level=0):
        print(level)
        super().__init__()
        if level == 0:
            for y in range(1):
                for i in range(1):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)

                    self.add(tile)
        elif level == 1:
            for y in range(2):
                for i in range(1,7):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)
                    self.add(tile)
        elif level == 2:
            for y in range(3):
                for i in range(8):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)
                    self.add(tile)
        elif level == 3:
            for y in range(4):
                for i in range(8):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)
                    self.add(tile)
        elif level == 4:
            for y in range(5):
                for i in range(8):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)
                    self.add(tile)
        else:
            for y in range(1):
                for i in range(1):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(i*100, 35*y)
                    self.add(tile)