import sys
import numpy
from itertools import tee

def test_report(report):
    """
    I just _know_ this is going to bite me when I see the second part of the challenge, but here's what I did.
    
    First, I compared the report against both its sorted/reverse-sorted variants. As long as nothing changed, we're good
        (I don't care if consecutive 2's get swapped because it immaterial)
        If that fails, immediately return a False
        
    Then, I compare each item against it's next item in the list. I used `itertools.tee` based on a cool SO post:
        [How can I iterate over overlapping (current, next) pairs of values from a list?](https://stackoverflow.com/questions/5434891/how-can-i-iterate-over-overlapping-current-next-pairs-of-values-from-a-list)
        You basically create two copies of the list (with `tee`) and advance one of them by one (using `next`).
        Take the resulting two lists and zip them together. 
        Finally, do a comparison of each item and if any value is unsafe, have the function return false
        
    If neither of the above conditions was met, we return true.
    """
    # print(f" ** TESTING REPORT: {report} ** ")
    # First check that the list is either ascending or descending.
    # I can do that by checking if the original report is the same as either the sorted or reverse sorted list.
    is_asc_sorted = report == sorted(report)
    is_desc_sorted = report == sorted(report, reverse=True)
    is_asc_or_desc = is_asc_sorted or is_desc_sorted
    
    if not is_asc_or_desc:
        print(f"    UNSAFE: {report} is neither strictly ascending or descending")
        return False

    # Now do the pairwise assessment of the gaps in each item
    a, b = tee(report, 2)
    next(b, None)
    unsafe = [ abs(a - b) for a, b in zip(a, b) if abs(a - b) < 1 or abs(a - b) > 3]
    if unsafe:
        print(f"    UNSAFE: Found unacceptable gaps: {unsafe}")
        return False

    print("    SAFE")
    return True
        
    
    
def solve(filename):
    """
    Load up a list of reports (lists), and pass each report through `test_report`.
    `test_report` returns True if the report is "safe", and False if it is "Unsafe"
    So all you have to do is count the number of "True" values in the list.
    """
    reports = [[int(i) for i in row.strip().split(" ")] for row in open(filename)]
    total_count = [test_report(report) for report in reports].count(True)
    print(f"Total Safe Reports: {total_count}")
    
def write_advent():
    """Waldorf Throwback Bay-Bee!"""
    print("The first light of Advent is the light of stones.")
    print("    The light that shines in seashells, crystals, and bones.")
    print("The second light of Advent is the light of plants.")
    print("    Plants that reach up to the sun and in the breezes dance.")
    print("The third light of Advent is the light of beasts.")
    print("    The light of hope that we see in the greatest and in the least.")
    print("The fourth light of Advent is the light of man.")
    print("    The light of love, the light of thought, to give and understand.")
    
if __name__ == '__main__':
    lower_args = [arg.lower() for arg in sys.argv]
    filename = "test_input" if "t" in lower_args else "input"
    solve(filename)
    
    if "advent" in lower_args:
        write_advent()