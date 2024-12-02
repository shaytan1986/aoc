import sys
from itertools import tee

def is_report_safe(report):
    # Build variations of the report with one item missing
    variations = [report]
    for i in range(0, len(report)):
        report_copy = report[:]
        del report_copy[i]
        variations.append(report_copy)
        
    # Loop through each variation and test if it works.
    # If some variation of the report works, we say the report is safe
    for variation in variations:
        if is_variation_safe(variation):
            return True
    return False
        
def is_variation_safe(variation):
    is_asc_sorted = variation == sorted(variation)
    is_desc_sorted = variation == sorted(variation, reverse=True)
    is_asc_or_desc = is_asc_sorted or is_desc_sorted
    
    # Test overall ordering
    if not is_asc_or_desc:
        return False
    
    # Test Gaps
    a, b = tee(variation, 2)
    next(b, None)
    
    # Now do the pairwise assessment of the gaps in each item
    a, b = tee(variation, 2)
    next(b, None)
    unsafe = [ abs(a - b) for a, b in zip(a, b) if abs(a - b) < 1 or abs(a - b) > 3 ]
    
    if unsafe:
        return False
    
    return True    
    
def solve(filename):
    """
    Load up a list of reports (lists), and pass each report through `test_report`.
    `test_report` returns True if the report is "safe", and False if it is "Unsafe"
    So all you have to do is count the number of "True" values in the list.
    """
    reports = [[int(i) for i in row.strip().split(" ")] for row in open(filename)]
    total_count = [is_report_safe(report) for report in reports].count(True)
    print(f"Total Safe Reports: {total_count}")
    
if __name__ == '__main__':
    lower_args = [arg.lower() for arg in sys.argv]
    filename = "test_input" if "t" in lower_args else "input"
    solve(filename)
    
    if "advent" in lower_args:
        write_advent()