# Question Day 4
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative 
# numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


#------------- Personal Solution ------------
# count up from 1 unitl reaching the maximum integer in the array.
# The first count not in the array is the missing lowest positive integer. 
# this runs in O(N) time and space and could be made slightly more efficient
# by only running for the length of the array+1 instead of max(array)+1. 
# 
# The solution has to exists within the length of the array+1 because we are
# looking at any possible positive integer. so for length 4. the soution would
# have to be 1, 2, 3, 4, or 5.

a = [3, 4, -1, 1] 
#a = [1, 2, 0]
def first_missing(a):
    i = 1
    while i < max(a)+1:
        i += 1
        if i not in a:
            return i
print(first_missing(a))


#------------- Given Solution 1 ------------
# Add all the numbers to a set, and then use a counter initialized to 1.
# Then continuously increment the counter and check whether the value is in the set.
# This is very similar to my solution but only looks at numbers within the array, 
# not the 'Max' member of the given array 

def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i
# runs in O(N) time and space, whereas the next algorithm uses no extra space.


#------------- Given Solution 2 ------------
# Our lives would be easier without the linear time constraint: we would just sort the array,
# while filtering out negative numbers, and iterate over the sorted array and return the first 
# number that doesn't match the index. However, sorting takes O(n log n), so we can't use that here.

# Clearly we have to use some sort of trick here to get it running in linear time. Since the first 
# missing positive number must be between 1 and len(array) + 1 (why?), we can ignore any negative 
# numbers and numbers bigger than len(array). The basic idea is to use the indices of the array 
# itself to reorder the elements to where they should be. We traverse the array and swap elements 
# between 0 and the length of the array to their value's index. We stay at each index until we find 
# that index's value and keep on swapping.

# By the end of this process, all the first positive numbers should be grouped in order at the beginning 
# of the array. We don't care about the others. This only takes O(N) time, since we swap each element at 
# most once.

# Then we can iterate through the array and return the index of the first number that doesn't match, 
# just like before.

nums = [3, 4, -1, 1] 
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

first_missing_positive(nums)