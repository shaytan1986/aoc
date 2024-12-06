import sys
    
def solve(filename):
    """
    Similar to the previous puzzle, load up the data as a 2d array.
    Pass each point into a function to check the kernel around the point
    for the requested shape. 
    
    Since each centroid can only match 1 "X" pattern, I just have `check_kernel` 
        return a True or False. Finally, I sum up how many True values we got.
    """
    # Parse file as a 2d array
    data = [ list(i.strip()) for i in open(filename).readlines() ]
    
    total = 0
    
    irow = 0
    for row in data:
        icell = 0
        for cell in row:
            if check_kernel(irow, icell, data):
                total += 1
            icell += 1
        irow += 1
        
    print(f"Total XMAS: {total}")
    
def check_kernel(irow, icell, data):
    """
    Checks to see if the current kernel (the "X" shape) matches.
    
    First, I'm checking that the center is "A". If it's not, don't even bother.
    Then I'm checking to make sure it's within the bounds that would not overrun the lists
    
    Then I'm getting the tl, tr, bl, br values
    
    Finally, I'm checking to make sure some combination of the letters forms the pattern.
    """
    center = data[irow][icell]
    
    # It has to be centered around an "A". If not, don't even bother.
    if center != "A":
        return False
    
    # Make sure we won't overrun the list
    if irow < 1:
        return False
    if irow > len(data) - 2:
        return False
    if icell < 1:
        return False
    if icell > len(data[irow]) - 2:
        return False
    
    # Get the other characters in the kernel
    top_left = data[irow - 1][icell - 1]
    top_right = data[irow - 1][icell + 1]
    bottom_left = data[irow + 1][icell - 1]
    bottom_right = data[irow + 1][icell + 1]

    # Check that MAS is spelled out across both axes
    if (
        ((top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M") )
        and ((top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"))
        ):
        print(f"({irow},{icell}) Found!")
        return True
    
    return False
        

if __name__ == "__main__":
    filename = "test_input" if "t" in sys.argv else "input"
    solve(filename)
