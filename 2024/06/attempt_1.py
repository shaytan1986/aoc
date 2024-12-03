import re
sample_line = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Compile some regexes
## Capture the word "don't()"
rgx_dont = re.compile(r"don't\(\)")
## Capture mul(x,y) groups
rgx_mul = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
## Capture initial section
rgx_init_section = re.compile(r"^(.*)don't\(\)")
## Capture all subsequent valid groups
rgx_sub_section = re.compile(r"do\(\)(.*)(don't\(\)|$)")


def get_subsections(line):
    # Handle the special case where the line doesn't contain the word "don't".
    # In that case, return the original line as the only member of the list
    if not rgx_dont.search(line):
        return [line]
    
    # In all other cases, start getting dirty
    # First, check the initial case, from the start of the line.
    init_section = rgx_init_section.findall(line)
    sub_sections = [ m[0] for m in rgx_sub_section.findall(line) ]
    all_sections = [match for match in init_section + sub_sections if match ]
    return all_sections

def mul(x, y):
    """A really dumb function which I can call using `eval()`"""
    return x * y

def parse_line(line):
    sub_sections = get_subsections(line)
    total = 0
    for sect in sub_sections:
        total += sum([int(eval(expr)) for expr in rgx_mul.findall(sect)])
    return total
    
def solve(filename = "test_input"):
    print(sum([parse_line(line) for line in open(filename)]))
    
    
solve("input")