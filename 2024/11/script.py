import sys
import numpy as np
from pprint import pprint as pp

class Coord:
    def __init__(self, irow, icol):
        self.irow = irow
        self.icol = icol

    def is_oob(self, map):
        if self.irow < 0:
            return True
        if self.irow >= len(map):
            return True
        if self.icol < 0:
            return True
        if self.icol > len(map[0]):
            return True
        return False
    
    def move(self, tup):
        return Coord(self.irow + tup[0], self.icol + tup[1])

    def is_wall(self, map):
        return map[self.irow][self.icol] == '#'

# If the dude is facing one of these directions, this shows where you move him
# If he's facing up, each step will reduce his row by 1
# If he's facing down, each step will increase his row by 1
# Etc.
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def get_next_direction(direction):
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    else:
        return UP

direction = UP
position = (0, 0)
def solve(filename):
    map = [ list(a.strip()) for a in open(filename) ]
    direction = UP
    position = get_guard_coord(map)

    while True:
        map[position.irow][position.icol] = "X"
        next_position = position.move(direction)

        # If we left the map, we're done
        if next_position.is_oob(map):
            break
        elif next_position.is_wall(map):
            direction = get_next_direction(direction)
        else:
            position = next_position

    print(count_guard_squares(map))

def count_guard_squares(map):
    return sum([ row.count("X") for row in map ])

def get_guard_coord(map):
    irow = 0
    for row in map:
        icell = 0
        for cell in row:
            if cell == "^":
                return Coord(irow, icell)
            icell += 1
        irow += 1
    # If there was no guard found, return a dummy dictionary
    return {
            "irow": None,
            "icell": None,
            "dir": None
        }

if __name__ == '__main__':
    filename = 'test_input' if 't' in sys.argv else 'input'
    solve(filename)