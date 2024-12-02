import sys
from itertools import tee

def is_report_safe(report):
    """
    Tests if a given report (directly from the input file) is safe (with a result of True)
    
    Since we have to take into account the Problem Dampener, We'll turn that one report into 
        _n_ reports, where we have one row for each variation to test (the full report, plus
        one for each omitted level)
    """
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
    """
    Test a specific report variation. 
    
    This method doesn't care about report dampening, it just answers the question of
        whether or not a given report variation is safe.
        
    It first tests the overall ordering of the list (asc/desc)
    Then it checks if any of the pairs of items have a gap not between 1 and 3
    
    If none of that disqualifies the variation, it returns True.
    """
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
    # If none of the above disqualifying conditions are met, we return that it is safe (True)
    return True    
    
def solve(filename):
    """
    Load up a list of reports (lists), and pass each report through `is_report_safe`.
    `is_report_safe` returns True if the report is "safe", and False if it is "unsafe"
    So all you have to do is count the number of "True" values in the list to get the 
        number of "safe" reports.
    """
    # Parse input data
    reports = [[int(i) for i in row.strip().split(" ")] for row in open(filename)]
    # Get the count of safe reports
    total_count = [is_report_safe(report) for report in reports].count(True)
    print(f"Total Safe Reports: {total_count}")
    
if __name__ == '__main__':
    lower_args = [arg.lower() for arg in sys.argv]
    filename = "test_input" if "t" in lower_args else "input"
    solve(filename)
