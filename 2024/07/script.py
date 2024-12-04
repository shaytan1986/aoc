import sys
import numpy as np
from pprint import pprint as pp
    
def solve(filename, **kwargs):
    data =  [ list(i.strip()) for i in open(filename).readlines() ]
    
    checks = []
    irow = 0
    for row in data:
        row_checks = []
        icell = 0
        for cell in row:
            new_checks = get_cell_matches(irow, icell, data, **kwargs)
            if new_checks:
                # Really this should be addition, but I want them broken out for now
                row_checks += new_checks
            icell += 1
        print(row_checks)
        checks += row_checks
        # checks.append(row_checks)
        irow += 1
        
    pp(len(checks))
    # pp(len([ c for c in checks if c.lower() == 'xmas' ]))
        
def get_cell_matches(irow, icell, data, **kwargs):
    
    if not kwargs:
        do_u, do_ur, do_r, do_dr, do_d, do_dl, do_l, do_ul = True, True, True, True, True, True, True, True
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
    # TESTED: l, r, u, d, ur, ul, dl
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
