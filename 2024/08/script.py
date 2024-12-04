import sys
    
def solve(filename):
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
    center = data[irow][icell]
    
    # It has to be centered around an "A". If not, don't even bother.
    if center != "A":
        return False
    
    

    if irow < 1:
        return False
    if irow > len(data) - 2:
        return False
    if icell < 1:
        return False
    if icell > len(data[irow]) - 2:
        return False
    

    top_left = data[irow - 1][icell - 1]
    top_right = data[irow - 1][icell + 1]
    bottom_left = data[irow + 1][icell - 1]
    bottom_right = data[irow + 1][icell + 1]
    

    
    # if irow == 3 and icell == 4:
    #     print("boo")
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
