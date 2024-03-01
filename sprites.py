from networkx import min_edge_cover
import pygame
from settings import *

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
  
  

