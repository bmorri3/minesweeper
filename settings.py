import pygame
import os

# COLORS (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOR = DARKGREY

# Game Settings
TILESIZE = 32
ROWS = 15
COLS = 15
NUM_MINES = 20
WIDTH = TILESIZE * COLS + 1
HEIGHT = TILESIZE * ROWS + 1
FPS = 60
TITLE = "Minesweeper Clone"

# Tiles marking how many neighboring mines are present.
tile_numbers = []
for i in range(1, 9):
  tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

# No mine and no neighbors
tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")), (TILESIZE, TILESIZE))
# Selected mine
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (TILESIZE, TILESIZE))
# Flag
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")), (TILESIZE, TILESIZE))
# Mine
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileMine.png")), (TILESIZE, TILESIZE))
# Unselected tile
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (TILESIZE, TILESIZE))
# Revealed flag, but not mine
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")), (TILESIZE, TILESIZE))
