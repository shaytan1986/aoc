import sys
import re
import numpy as np

def solve(filename):
    """
    The first hairy part is the assignment of `items`. There is a lot going on here.
    
    The Inner-Most LC takes each line of the file, strips line endings, and replaces spaces or tabs with a single space.
        The reason for that is that when I copied the output to my machine, it wasn't clear it was using one or the other.
        So I used a `re.sub()` to make sure that split worked smoothly with either tab(s) or space(s)
        
        The return of that LC is a list of 2d arrays
        
    The outer LC just casts the split terms as integers and outputs them as a list of tuples.
    
    Finally, I'm wrapping the whole thing in a `np.array()` because numpy has some really slick 
        slicing capabilites where I can extract all the item 0s or item 1s
        [Numpy Slicing](https://numpy.org/devdocs/user/basics.indexing.html)
        
    I use `np.sort()` to sort a numpy array, then I use the fact that numpy arrays are awesome to just do
        element-wise differencing, taking the absolute value of each difference, and summing them up.
    """
    items = np.array([
        (int(a[0]), int(a[1]))
        for a in
        [
            # To account for cases where the file has either tabs or spaces
            re.sub(r"[ \t]+", " ", item.strip()).split(" ")
            for item in open(filename)
        ]
    ])

    first_values = np.sort(items[:,0])
    second_values = np.sort(items[:,1])

    print(sum(abs(first_values - second_values)))

    
    # for a, b in items:
    #     distance = abs(a - b)
    #     print(f"[{i}]: abs({a} - {b}) = {distance}")
    #     i += 1
    

if __name__ == '__main__':
    filename = "test_input" if len(sys.argv) > 1 and sys.argv[1].lower() == "t" else "input"
    solve(filename)

    