import re

# Compile the regex for reuse
rgx = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

def mul(x, y):
    """A really dumb function which I can call using `eval()`"""
    return x * y

def parse_line(line ):
    """
    Using a regular expression, extract all the mul(x,y) expressions.
    Then just use a straight eval() on them. 
    finally, sum them up
    """
    return sum([eval(expr) for expr in rgx.findall(line)])
    
def solve(filename = "input"):
    print(sum([parse_line(line) for line in open(filename)]))
    
solve()