def majority_vote(lst):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i