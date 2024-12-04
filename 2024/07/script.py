import sys
import numpy as np
from pprint import pprint as pp
    
def solve(filename, **kwargs):
    """
    We have a 2D array of characters and we need to get all possible 4-length strings.
    
    So we parse the file input as a 2D array and then loop over every cell getting the matches
        adjacent to that cell.
    
    It's not the most elegant solution, but it does work.
    
    I also allowed this function to be parameterized with a dictionary which says which checks you
        actually want to run. That's only useful for debugging, butt ust so you know what it is.
    """
    # Parse file as a 2d array
    data = [ list(i.strip()) for i in open(filename).readlines() ]
    
    # We'll build this up with checks
    checks = []
    
    # Since I need to pass indexes to `get_cell_matches` I'm iterating them here
    irow = 0
    # Loop over rows
    for row in data:
        # We could add directly to `checks` but during debugging it was easier to have an intermediate list
        row_checks = []
        icell = 0
        # loop over cells
        for cell in row:
            new_checks = get_cell_matches(irow, icell, data, **kwargs)
            # As long as we got _some_ matches, append them to `row_checks`
            if new_checks:
                # Really this should be addition, but I want them broken out for now
                row_checks += new_checks
            icell += 1
        # append all the checks from the current row to the total list
        checks += row_checks
        irow += 1
        
    pp(f"Number of Matching Checks: {len(checks)}")
    # pp(len([ c for c in checks if c.lower() == 'xmas' ]))
        
def get_cell_matches(irow, icell, data, **kwargs):
    """
    This function takes a set of x,y coords, the raw data, and an optional **kwargs indicating which 
        checks to actually run. That last one is really only useful for debugging.
        
    So for every single cell, I'm checking in all the cardinal directions
    * Up
    * Up-Right
    * Right
    * Down-Right
    * Down
    * Down-Left
    * Left
    * Up-Left
    
    Anything that says "XMAS" then gets output for consumption by the outer method.
    """
    
    # Figure out which tests to run
    # By default, everything
    if not kwargs:
        do_u, do_ur, do_r, do_dr, do_d, do_dl, do_l, do_ul = True, True, True, True, True, True, True, True
    # If anything is passed, default everything to false.
    else:
        do_u = kwargs.get('u', False)
        do_ur = kwargs.get('ur', False)
        do_r = kwargs.get('r', False)
        do_dr = kwargs.get('dr', False)
        do_d = kwargs.get('d', False)
        do_dl = kwargs.get('dl', False)
        do_l = kwargs.get('l', False)
        do_ul = kwargs.get('ul', False)
        
    
    # print(f"Current cell: ({irow},{icell}): {data[irow][icell]}")
    sub_arrays = []
    # SOLVE UPWARDS
    # Make sure we're at least on the 4th row
    if irow >= 3:
        # Solve straight Up
        if do_u:
            straight_up = []
            for i in range(4):
                straight_up.append(data[irow - i][icell])
            sub_arrays.append(straight_up)
                
        # Solve Diagonal Up/Left
        if do_ul:
            if icell >= 3:
                up_left = []
                for i in range(4):
                    up_left.append(data[irow - i][icell - i])
                sub_arrays.append(up_left)
            
        # Solve Diagonal Up/Right
        if do_ur:
            if icell < len(data[irow]) - 3:
                up_right = []
                for i in range(4):
                    up_right.append(data[irow - i][icell + i])
                sub_arrays.append(up_right)
        
    # SOLVE DOWNWARDS
    # Make sure we're at least for rows from the bottom 
    if irow < len(data) -3:
        if do_d:
            straight_down = []
            for i in range(4):
                straight_down.append(data[irow + i][icell])
            sub_arrays.append(straight_down)
                
        # Solve Diagonal down/Left
        if do_dl:
            if icell >= 3:
                down_left = []
                for i in range(4):
                    down_left.append(data[irow + i][icell - i])
                sub_arrays.append(down_left)
                
        # Solve Diagonal down/Right
        if do_dr:
            if icell < len(data[irow]) - 3:
                down_right = []
                for i in range(4):
                    down_right.append(data[irow + i][icell + i])
                sub_arrays.append(down_right)

    # SOLVE LEFT
    if do_l:
        if icell >= 3:
            left = []
            for i in range(4):
                left.append(data[irow][icell - i])
            sub_arrays.append(left)
                

    # SOLVE RIGHT
    if do_r:
        if icell < len(data[irow]) - 3:
            right = []
            for i in range(4):
                right.append(data[irow][icell + i])
            sub_arrays.append(right)
            
    #  I could do the word checking here, but I'm assuming it's going to be better to have a separate checker
    retval =  [ "".join(c) for c in sub_arrays if "".join(c).lower() == "xmas"]
    # print(f"   {retval}")
    return retval
    
    
if __name__ == '__main__':
    # Controls which directions to look. Mostly for debugging

    kwargs = {
        "u": False,
        "ur": False,
        "r": False,
        "dr": True,
        "d": False,
        "dl": True,
        "l": False,
        "ul": False
    }
    filename = "test_input" if "t" in sys.argv else "input"
    solve(filename)
