import re

rgx = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

def mul(x, y):
    return x * y

def parse_line(line ):
    return sum([eval(expr) for expr in rgx.findall(line)])
    
print(sum([parse_line(line) for line in open("input")]))