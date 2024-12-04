# WARNING: The input file looks like multiple lines of code. If you treat it as such, you will get the wrong answer.
# You need to basically ignore the line endings and treat it as one big string.
import re
import sys

rgx = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
def mul(x,y):
    return x * y

def compute_line(line):
    """
    This is a really good pattern to remember. We used it in CSV Parsers as well.
    
    Loop through a bunch of symbols. 
    If the symbol is a special symbol, set whatever flags are necessary
    If it is not a special symbol (default) process the symbol, with all the currently set flags
    
    
    """
    result = 0
    active = True
    
    for match in rgx.findall(line):
        if match == "do()":
            active = True
        elif match == "don't()":
            active = False
        elif active:
            product = int(eval(match))
            result += product
    return result
    
def solve(filename = "test_input"):
    # Turn it into one big happy string
    line = "".join([line.strip() for line in open("input")])
    print(compute_line(line))

if __name__ == '__main__':
    filename = "test_input" if "t" in sys.argv else "input"
    solve(filename)

