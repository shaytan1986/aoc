import sys
from itertools import product, tee
from math import ceil


def solve(filename):
    input_lines = 0
    solvable_equation_count = 0
    equations = get_equations(filename)
            
    print(f"{solvable_equation_count} of {input_lines} equations are solvable.")
    
    operators = [
        lambda a, b: a + b,
        lambda a, b: a * b
    ]

def eval
def get_equations(filename):
    """
    Yield returns tuples consisting of (total, operands)
    """
    for line in open(filename):
        split_line = [l.strip() for l in line.strip().split(":")]
        total = int(split_line[0])
        operands = list(map(int, split_line[1].split(' ')))
        yield (total, operands)
        
        
if __name__ == '__main__':
    filename = 'test_input' if 't' in sys.argv else 'input'
    solve(filename)
