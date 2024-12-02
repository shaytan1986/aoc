import sys
import re
import numpy as np

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

    