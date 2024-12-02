import sys
import re
import numpy as np
from collections import Counter

def solve(filename):
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
