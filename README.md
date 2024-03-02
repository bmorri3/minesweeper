# minesweeper

Followed a minesweeper tutorial in preparation for an interview.
I'm practicing with the basic implementation of the game and classes along with separating components into appropriate
files. I did most of the logic before the respective part of the video played and used the video to check.

main.py contains the class Game and implements running the code while checking for events.
settings.py contains the color constants and the file imports
sprites.py contains the classes Tile and Board and their methods.
/assets contains the images for the tiles

python3 main.py to run the code

Future features that could be added:
1. Timer
2. Counter for flags
3. Easy, Medium, Hard levels with varying board sizes and number of mines
4. Implement simultaneous left and right click for searching all adjacent tiles to that clicked
5. High scores (best times)
