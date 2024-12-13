import sys
from itertools import product, tee
from math import ceil
def solve(filename):
    input_lines = 0
    solvable_equation_count = 0
    for puzzle_line in get_puzzle_input(filename):
        is_solvable, result = process_puzzle_line(puzzle_line, input_lines)
        if is_solvable:
            solvable_equation_count += result
        input_lines += 1
            
    print(f"{solvable_equation_count} of {input_lines} equations are solvable.")

def get_puzzle_input(filename):
    """
    Yield returns tuples consisting of (total, operands)
    """
    for line in open(filename):
        split_line = [l.strip() for l in line.strip().split(":")]
        total = int(split_line[0])
        operands = list(map(int, split_line[1].split(' ')))
        yield (total, operands)
        
def process_puzzle_line(puzzle_line, line_id):
    """
    Processes a single (total, operand) tuple
    """
    total, operands  = puzzle_line
    
    operand_slots = len(operands) - 1
    operator_sets = product(["+", "*"], repeat=operand_slots)
    op_set_id = 0

    for op_set in operator_sets:
        is_solvable, result = check_operator_set(total, operands, op_set, line_id, op_set_id)
        if is_solvable:
            return (is_solvable, result)
        op_set_id += 1
        
    # print(f'operands: {operands}')
    # print(f'operand_slots: {operand_slots}')
    return (False, 0)

def check_operator_set(total, operands, operator_set, line_id, op_set_id):
    """Test if a specific configuration of operators satisfies the total"""
    # print(f" ** [{line_id}][{op_set_id}] **")
    # print(f'    total: {total}')
    # print(f'    operands: {operands}')
    # print(f'    operator_set: {operator_set}')
    
    running_total = operands[0]
    operator_id = 0
    for i, operand in enumerate(operands[0:-1]):
        next_operand = operands[i+1]
        operator = operator_set[operator_id]
        eval_str = f"{running_total} {operator} {next_operand}"
        # print(f'running_total: {running_total}')
        # print(f'i: {i}')
        # print(f'operand: {operand}')
        # print(f'next_operand: {next_operand}')
        # print(f'operator: {operator}')
        running_total = int(eval(eval_str))
        # print(f'    eval_str: {eval_str} = {running_total}')
        
        operator_id += 1
        
    retval = False
    if running_total == total:
        # print(f"    Correct!")
        # print(f'    operands: {operands}')
        # print(f'    operator_set: {operator_set}')
        retval = True
    else:
        # print(f"    Incorrect!")
        # print(f"    Total = {running_total}")
        retval = False
    return (retval, total)
        
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
if __name__ == '__main__':
    filename = 'test_input' if 't' in sys.argv else 'input'
    solve(filename)
