import pygame
from .tile import Tile

colors = [(247, 37, 133), (114, 9, 183), (58, 12, 163), (67, 97, 238), (76, 201, 240)]

class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30, level=0):
        super().__init__()
        if level == 0:
            for y in range(1):
                for x in range(8):
                    tile = Tile(width=tile_width, height=tile_height, color=colors[0])
                    tile.move_to(x*100, 35*y+35+35)

                    self.add(tile)
        elif level == 1:
            for y in range(2):
                for x in range(1,7):
                    tile = Tile(width=tile_width, height=tile_height, color=colors[1])
                    tile.move_to(x*100, 35*y+35)
                    self.add(tile)
        elif level == 2:
            for y in range(3):
                for x in range(8):
                    tile = Tile(width=tile_width, height=tile_height, color=colors[2])
                    tile.move_to(x*100, 35*y+35)
                    self.add(tile)
        elif level == 3:
            for y in range(4):
                for x in range(8):
                    tile = Tile(width=tile_width, height=tile_height, color=colors[3])
                    tile.move_to(x*100, 35*y+35)
                    self.add(tile)
        elif level == 4:
            for y in range(5):
                for x in range(8):
                    tile = Tile(width=tile_width, height=tile_height, color=colors[4])
                    tile.move_to(x*100, 35*y+35)
                    self.add(tile)
        else:
            for y in range(1):
                for x in range(1):
                    tile = Tile(width=tile_width, height=tile_height)
                    tile.move_to(x*100, 35*y+35)
                    self.add(tile)