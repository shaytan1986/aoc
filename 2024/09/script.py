import sys
import numpy as np

def solve(filename):
    ## Pre-process these as integers
    rules_list = [
            [int(i[0]), int(i[1])]
            for i in
            [ l.strip().split('|') for l in open(filename) if "|" in l ]
        ]
        
    updates = [ l.strip().split(",") for l in open(filename) if "," in l]
    rules_list.sort(key=lambda x: (x[0], x[1]), reverse=True)
    rules = np.array(rules_list)
    
    is_in_right_order(rules, updates[0])
    
def is_in_right_order(rules, update):
    correct = False
    update = [ int(i) for i in update ]
    banned_pages = set()
    for page in update:
        # subrules are all the left hand values that match the right.
        # Basically, we need to add all the subrules to a list/set
        # and as we walk through the pages, if we see a rule that disqualifies
        # the page, the whole update fails.
        sub_rules = list(map(int, rules[rules[:,1] == page][:,0]))
        banned_pages.update(sub_rules)
        print(banned_pages)
    
    # Print Result
    msg = f"{update} is "
    if not correct:
        msg += "not "
    msg += "in the correct order"
    
    print(msg)
    
    
    
if __name__ == '__main__':
    filename = 'test_input' if 't' in sys.argv else 'input'
    solve(filename)