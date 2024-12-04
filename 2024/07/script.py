import sys
import numpy as np
from pprint import pprint as pp
    
def solve(filename):
    data =  [ list(i.strip()) for i in open(filename).readlines() ]
    
    irow = 0
    for row in data:
        icell = 0
        for cell in row:
            get_cell_matches(irow, icell, data)
            icell += 1
        return
        irow += 1
        
def get_cell_matches(irow, icell, data):
    
    cell = data[irow][icell]
    print(f"Current cell: ({irow},{icell}): {cell}")
    sub_arrays = []
    ## SOLVE UPWARDS
    # Make sure we're at least on the 4th row
    # if irow >= 3:
    #     # Solve straight Up
    #     straight_up = []
    #     for i in range(4):
    #         straight_up.append(data[irow - i][icell])
    #         sub_arrays.append(straight_up)
            
    #     # Solve Diagonal Up/Left
    #     if icell >= 3:
    #         up_left = []
    #         for i in range(4):
    #             up_left.append(data[irow - i][icell - i])
    #             sub_arrays.append(up_left)
    #         pass
        
    #     # Solve Diagonal Up/Right
    #     if icell <= len(data[irow] - 3):
    #         up_right = []
    #         for i in range(4):
    #             up_right.append(data[irow - i][icell + i])
    #             sub_arrays.append(up_right)
    
    # ## SOLVE DOWNWARDS
    # # Make sure we're at least for rows from the bottom
    # if irow <= len(data) - 3:
    #     straight_down = []
    #     for i in range(4):
    #         straight_down.append(data[irow + i][icell])
    #         sub_arrays.append(straight_down)
            
    #     # Solve Diagonal down/Left
    #     if icell >= 3:
    #         down_left = []
    #         for i in range(4):
    #             down_left.append(data[irow + i][icell - i])
    #             sub_arrays.append(down_left)
        
    #     # Solve Diagonal down/Right
    #     if icell <= len(data[irow] - 3):
    #         down_right = []
    #         for i in range(4):
    #             down_right.append(data[irow + i][icell + i])
    #             sub_arrays.append(down_right)

    # SOLVE LEFT
    if icell > 3:
        start = icell
        stop = icell - 4
        left = data[irow][start:stop:-1]
        sub_arrays.append(left)
    
    # SOLVE RIGHT
    if icell < len(data[irow]) - 3:
        start = icell
        stop = icell+4
        right = data[irow][start:stop]
        sub_arrays.append(right)
        
    if sub_arrays:
        print(sub_arrays)
    
    
if __name__ == '__main__':
    filename = "numeric_input" if "t" in sys.argv else "input"
    solve(filename)
