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
    if not self.flagged and self.revealed:      
      board_surface.blit(self.image, (self.x, self.y))
    elif self.flagged and not self.revealed:
      board_surface.blit(tile_flag, (self.x, self.y))
    elif not self.revealed:
      board_surface.blit(tile_unknown, (self.x, self.y))



class Board:
  def __init__(self):
    self.board_surface = pygame.Surface((WIDTH, HEIGHT))
    self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
    self.place_mines()
    self.place_clues()
    
  def place_mines(self):
    for _ in range(NUM_MINES):
      while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        
        if self.board_list[x][x].image is tile_empty:
          self.board_list[x][y].image = tile_mine
          self.board_list[x][y].type = "X"
          break

  def place_clues(self):
    for col in range(COLS):
      for row in range(ROWS):        
        if self.board_list[col][row].image is tile_empty:
          total_mines = self.check_neighbors(col, row)
          if total_mines != 0:
            self.board_list[col][row].image = tile_numbers[total_mines - 1]
            self.board_list[col][row].type = "C"


  @staticmethod
  def is_inside(x, y):
     return 0 <= x < ROWS and 0 <= y < COLS

  def check_neighbors(self, x, y):
    total_mines = 0
    
    for col in range(x-1, x+2):
      for row in range(y-1, y+2):
        
        if self.is_inside(col, row) and self.board_list[col][row].image == tile_mine:
            total_mines += 1
    
    # This is in the event that the central square is a mine. This should never be called as we are only checking
    # neighbors if a tile is empty
    if self.board_list[x][y].image == tile_mine:
      total_mines -= 1

    return total_mines
        
   
  def display_board(self):
    for i in self.board_list:
      print(i)

  def draw(self, screen):
    for row in self.board_list:
      for tile in row:
        tile.draw(self.board_surface)

    screen.blit(self.board_surface, (0, 0))


