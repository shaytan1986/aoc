import sys
import numpy as np
from pprint import pprint as pp
from copy import deepcopy

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
        if self.icol >= len(map[0]):
            return True
        return False
    
    def move(self, tup):
        return Coord(self.irow + tup[0], self.icol + tup[1])

    def is_wall(self, map):
        value = map[self.irow][self.icol] 
        return value == '#'

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
position = Coord(0, 0)

def solve(filename):
    map = [ list(a.strip()) for a in open(filename) ]
    direction = UP
    position = get_guard_coord(map)
    # DON'T CHANGE THIS. It's going to be used to start simulations
    original_guard_position = get_guard_coord(map)
    # Solves the first part of the puzzle
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

    # Run 
    total_loops = find_loops(map, original_guard_position)
    print(f"Total Loops: {total_loops}")
    print(f"Total Guard Positions: {count_guard_squares(map)}")
    
def find_loops(solved_map, original_guard_position):
    candidates = []
    irow = 0
    for row in solved_map:
        icol = 0
        for col in solved_map[irow]:
            
            if (irow, icol) == (original_guard_position.irow, original_guard_position.icol):
                pass
            ## I don't actually know if this is necessary/desirable
            # I might need to consider spots that aren't on the original path
            elif col == "X":
                candidates.append(Coord(irow, icol))
            
            icol += 1
        irow += 1
                
                
    total_loops = 0
    
    sim_num = 0
    for candidate in candidates:
        print(f" ** SIMULATION {sim_num} **")
        # Copy the map, with the modified obstruction
        sim_map = deepcopy(solved_map)
        sim_map[candidate.irow][candidate.icol] = "#"
        if check_simulation_results_in_loop(sim_map, original_guard_position, sim_num):
            total_loops += 1
        sim_num += 1
            
    return total_loops
            
def check_simulation_results_in_loop(map, original_guard_position, sim_num):
    guard_direction = UP
    guard_position = Coord(original_guard_position.irow, original_guard_position.icol)
    original_irow = original_guard_position.irow
    original_icol = original_guard_position.icol
    
    is_circular = False
    i = 0
    circ_ct = 0
    visit_ct = {}
    while True:
        guard_tuple = (guard_position.irow, guard_position.icol)
        map[guard_position.irow][guard_position.icol] = "@"
        next_position = guard_position.move(guard_direction)
        new_value = visit_ct.get(guard_tuple, 0) + 1
        visit_ct[guard_tuple] = new_value
        
        # if sim_num == 31:
        #     print(f"[{sim_num}][{i}]")
        #     print(f"Guard: ({guard_position.irow}, {guard_position.icol})")
        #     print(f"Next: ({next_position.irow}, {next_position.icol})")
        #     print(f"Cir Ct: {circ_ct}")
        #     pp(map)
        #     print("\n")
        map[guard_position.irow][guard_position.icol] = "o"
        # pp(map)
        if next_position.is_oob(map):
            is_circular = False
            break
        elif visit_ct.get(guard_tuple, 0) > 4:
            # circ_ct += 1
            # if next_position.is_wall(map):
            #     guard_direction = get_next_direction(guard_direction)
            # else:
            #     guard_position = next_position
            # if circ_ct > 4:
            return True
        elif next_position.is_wall(map):
            guard_direction = get_next_direction(guard_direction)
        else:
            guard_position = next_position
            
        i += 1
        
    return is_circular


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