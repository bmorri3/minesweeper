# Minesweeper using Pygame
# From tutorial: https://www.youtube.com/watch?v=n0jZRlhLtt0&ab_channel=Tech%26Gaming

import pygame
from settings import *
from sprites import *

class Game:
  def __init__ (self):
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    self.clock = pygame.time.Clock()

  def new(self):
    # Create new board instance
    self.board = Board()
    # Display the board to the terminal for testing purposes.
    self.board.display_board()
          
  def run(self):
    self.playing = True

    # Loop while the game hasn't ended
    while self.playing:
      self.clock.tick(FPS)
      # Start the events tracker
      self.events()
      # Update the screen
      self.draw()
    else:
      # End the game
      self.end_screen()


  def draw(self):
    # Draw the surface
    self.screen.fill(BGCOLOR)
    # Draw the board
    self.board.draw(self.screen)
    # Make everything update at once
    pygame.display.flip()


  # Check if the current game state is a win
  def check_win(self):
    for row in self.board.board_list:
      for tile in row:
        # If any of the tiles are not a mine and also not revealed, continue the game
        if tile.type != "X" and not tile.revealed:
          return False
    
    # If all of the tiles are either revealed or a mine, the user has won.
    return True
    

  def events(self):
    # Handle all event processing.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit(0)

      if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        # Adjust x and y coordinates based on TILESIZE
        mx //= TILESIZE
        my //= TILESIZE

        # Left click
        if event.button == 1:
          # If the tile isn't aflag
          if not self.board.board_list[mx][my].flagged:
            # Dig and check if exploded
            if not self.board.dig(mx, my):
              # Explode
              for row in self.board.board_list:
                for tile in row:
                  if tile.flagged and tile.type != "X":
                    # Remove the flag
                    tile.flagged = False
                    # Mark tile as revealed
                    tile.revealed = True
                    # Replace with wrong flags
                    tile.image = tile_not_mine
                  elif tile.type == "X":
                    tile.revealed = True
              self.playing = False

        # Right click
        if event.button == 3:
          # If the tile isn't revealed
          if not self.board.board_list[mx][my].revealed:
            # Toggle the flag on or off
            self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

        # Check for a win        
        if self.check_win():
          self.win = True
          # End the game
          self.playing = False
          
          for row in self.board.board_list:
            for tile in row:
              if not tile.revealed:
                # The game has been won. Tag all remaining tiles.
                tile.flagged = True


  def end_screen(self):
    # Wait until quit or mouse click
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
          return 

# Create game instance
game = Game()
while True:
  # Initiate a game
  game.new()
  # Run the game
  game.run()