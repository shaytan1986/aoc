import sys
import re
import numpy as np
from collections import Counter

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
        
    So `items` is a numpy array of tuples with the first item being the left number being tuple[0]
        and the right number being tuple[1]
        
    I'm then using numpy slicing to extract the first and second columns of `items` and casting them as 
        regular old python lists. That way values like `np.Int64` will be returned as regular python its.    
    
    Searching for a way to get the counts of items in a list, I came across the stack overflow post
        [How do i count the occurrences of a list item?](https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item)
        which pointed me to a construct in `collections` called a `Counter` which basically returns a dictionary of [item, count]
        
    At this point I got lazy and decided to abandon LCs and just did a loop over all the left number, multiplying them 
        by the found count in the `second_freq` dictionary.
    
    I used `second_freq.get(v, 0)` to make sure I got a number no matter if it existed in the lookup dictionary, and if
        it didn't exist, to treat that as a zero.
        
    Finally, I just build up `sim_total` item by item until I'm done.    
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
    
    first_values = items[:,0].tolist()
    second_values = items[:,1].tolist()
    second_freq = Counter(second_values)
    sim_total = 0
    for v in first_values:
        factor = second_freq.get(v, 0)
        sim_total += v * factor
    
    print(sim_total)
if __name__ == '__main__':
    filename = "test_input" if len(sys.argv) > 1 and sys.argv[1].lower() == "t" else "input"
    solve(filename)
