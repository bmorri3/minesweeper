import pygame
import random
from settings import *
from sprites import *

# Types list 
# "." -> unknown
# "X" -> mine
# "C" -> clue
# "/" -> empty

class Tile:
  def  __init__(self, x, y, image, type, revealed=False, flagged=False):
    self.x, self.y = x * TILESIZE, y * TILESIZE
    self.image = image
    self.type = type
    self.revealed = revealed
    self.flagged = flagged

  def __repr__(self):
      return self.type

  def draw(self, board_surface):
    board_surface.blit(self.image, (self.x, self.y))


class Board:
  def __init__(self):
    self.board_surface = pygame.Surface((WIDTH, HEIGHT))
    self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
    self.place_mines()
    
  def place_mines(self):
    for _ in range(NUM_MINES):
      while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        
        if self.board_list[x][x].type == ".":
          self.board_list[x][y].image = tile_mine
          self.board_list[x][y].type = "X"
          break
        
	def place_clues(self):
		pass

	@staticmethod
  def is_inside(self, x, y):
     return 0 <= x < ROWS and 0 <= y < COLS

	def check_neighbors(self, x, y):
    for 
   
  def display_board(self):
    for i in self.board_list:
      print(i)

  def draw(self, screen):
    for row in self.board_list:
      for tile in row:
        tile.draw(self.board_surface)

    screen.blit(self.board_surface, (0, 0))


