def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

two_sum([10,15,3,7], 17)
# Another way is to use a set to remember the numbers we've seen so far. 
# Then for a given number, we can check if there is another number that, 
# if added, would sum to k. This would be O(N) since lookups of sets are O(1) each.
