import sys
import numpy as np

def solve(filename):
    ## Pre-process these as integers
    rules_list = [
            [int(i[0]), int(i[1])]
            for i in
            [ l.strip().split('|') for l in open(filename) if "|" in l ]
        ]
        
    updates = [ 
            [ int(u) for u in l.strip().split(",") ]
            for l in open(filename) 
            if "," in l
            ]
    rules_list.sort(key=lambda x: (x[0], x[1]), reverse=True)
    rules = np.array(rules_list)
    
    result = 0
    for update in updates:
        if is_in_right_order(rules, update):
            middle_item = get_middle_item(update)
            result += middle_item
    print(f"There are {result} correct updates")
    
def get_middle_item(items):
    return items[int((len(items) - 1) / 2)]

def is_in_right_order(rules, update):
    correct = True
    banned_pages = set()
    for page in update:
        # subrules are all the left hand values that match the right.
        # Basically, we need to add all the subrules to a list/set
        # and as we walk through the pages, if we see a rule that disqualifies
        # the page, the whole update fails.
        sub_rules = list(map(int, rules[rules[:,1] == page][:,0]))
        banned_pages.update(sub_rules)
        
        if page in banned_pages:
            correct = False
            break
    
    
    # Print Result
    msg = f"{update} is "
    if not correct:
        msg += "not "
    msg += "in the correct order"
    
    print(msg)
    return correct
    
    
    
if __name__ == '__main__':
    filename = 'test_input' if 't' in sys.argv else 'input'
    solve(filename)