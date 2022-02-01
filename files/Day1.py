#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def two_sum1(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
  return False
#Brute force way would involve a nested iteration to check for every pair of numbers:
#This would take O(N^2)

def two_sum2(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

two_sum1([10,15,3,7], 17)
# Another way is to use a set to remember the numbers we've seen so far. 
# Then for a given number, we can check if there is another number that, 
# if added, would sum to k. This would be O(N) since lookups of sets are O(1) each.
