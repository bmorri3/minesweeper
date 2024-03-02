import pygame
import random
from settings import *

# Types list 
# "." -> empty
# "X" -> mine
# "C" -> clue
# "/" -> unknown

class Tile:
  def  __init__(self, x, y, image, type, revealed=False, flagged=False):
    self.x, self.y = x * TILESIZE, y * TILESIZE
    self.image = image
    self.type = type
    self.revealed = revealed
    self.flagged = flagged


  def draw(self, board_surface):
    # If no flag but revealed, show what it is
    if not self.flagged and self.revealed:      
      board_surface.blit(self.image, (self.x, self.y))
    # If flagged and not revealed, show flag
    elif self.flagged and not self.revealed:
      board_surface.blit(tile_flag, (self.x, self.y))
    # Else if not revealed, show unknown
    elif not self.revealed:
      board_surface.blit(tile_unknown, (self.x, self.y))


  def __repr__(self):
      # For printing to the terminal for debugging
      return self.type



class Board:
  def __init__(self):
    self.board_surface = pygame.Surface((WIDTH, HEIGHT))
    self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
    self.place_mines()
    self.place_clues()
    self.dug = []


  def place_mines(self):
    # Repeat until all mines are placed
    for _ in range(NUM_MINES):
      # Repeat until a mine is successfully placed.
      while True:
        x = random.randint(0, ROWS - 1)
        y = random.randint(0, COLS - 1)
        
        # If the space is unknown, place a mine
        if self.board_list[x][y].image is tile_empty:
          self.board_list[x][y].image = tile_mine
          self.board_list[x][y].type = "X"
          break


  def place_clues(self):
    for row in range(ROWS): 
      for col in range(COLS):
        # If the tile is not a mine, determine how many mines are around it
        if self.board_list[row][col].type != "X":
          total_mines = self.check_neighbors(row, col)
          # Update the tile with the number of neighboring mines
          if total_mines > 0:
            self.board_list[row][col].image = tile_numbers[total_mines - 1]
            self.board_list[row][col].type = "C"


  # Ensures valid indices
  @staticmethod
  def is_inside(x, y):
     return 0 <= x < ROWS and 0 <= y < COLS

  # Determine the number of mines in neighboring cells
  def check_neighbors(self, x, y):
    total_mines = 0
    
    for row in range(x-1, x+2):
      for col in range(y-1, y+2):
        
        if self.is_inside(row, col) and self.board_list[row][col].image is tile_mine:
            total_mines += 1
    
    # This is in the event that the central square is a mine. This should never be called as we are only checking
    # neighbors if a tile is empty
    if self.board_list[x][y].image is tile_mine:
      total_mines -= 1

    return total_mines

  # Draws the tiles on the board
  def draw(self, screen):
    for row in self.board_list:
      for tile in row:
        tile.draw(self.board_surface)

    screen.blit(self.board_surface, (0, 0))
  
  # Call to determine selected tile
  def dig(self, x, y):
    # Add current tile to list of tiles already "dug"
    self.dug.append((x, y))
    # If it is a mine, set to exploded and return False to end game
    if self.board_list[x][y].image is tile_mine:
      self.board_list[x][y].revealed = True
      self.board_list[x][y].image = tile_exploded
      return False

    # If the tile is a clue, reveal it and continue
    elif self.board_list[x][y].type == "C":
      self.board_list[x][y].revealed = True
      return True

    # If the tile is not flagged, reveal it
    elif not self.board_list[x][y].flagged:
      self.board_list[x][y].revealed = True

    # For all surround tiles
    for row in range(max(0, x - 1), min(ROWS - 1, x + 1) + 1):
      for col in range(max(0, y - 1), min(COLS - 1, y + 1) + 1):
        # If the tile hasn't already been revealed
        if (row, col) not in self.dug:
          # Call dig for this tile
          self.dig(row, col)
    
    return True
  # For printing to the terminal for testing
  def display_board(self):
    for row in self.board_list:
      print(row)