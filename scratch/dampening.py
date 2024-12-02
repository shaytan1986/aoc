from itertools import tee
report = [7, 6, 4, 2, 1]

# def test_safeness(use_dampening = False):
#     is_asc_sorted = report == sorted(report)
#     is_desc_sorted = report == sorted(report, reverse=True)
#     is_asc_or_desc = is_asc_sorted or is_desc_sorted
    
#     if not is_asc_or_desc:
#         print(f"    UNSAFE: {report} is neither strictly ascending or descending")
#         return False

#     # Now do the pairwise assessment of the gaps in each item
#     a, b = tee(report, 2)
#     next(b, None)
    
#     unsafe = [ abs(a - b) for a, b in zip(a, b) if abs(a - b) < 1 or abs(a - b) > 3]
#     print(f"Unsafe pairs: {len(unsafe)}")
    
#     if len(unsafe) > 0:
#         safe_with_dampening = test_safeness_with_problem_dampening(report)
        
#     print("    SAFE")
#     return True

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
    a, b = tee(report, 2)
    next(b, None)
    
    # Now do the pairwise assessment of the gaps in each item
    a, b = tee(report, 2)
    next(b, None)
    unsafe = [ abs(a - b) for a, b in zip(a, b) if abs(a - b) < 1 or abs(a - b) > 3 ]
    
    if unsafe:
        return False
    
    return True
    