# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of 
# all the numbers in the original array except the one at i.

# For example, if our input was[1, 2, 3, 4, 5], 
# the expected output would be[120, 60, 40, 30, 24]. 
# If our input was[3, 2, 1], 
# the expected output would be[2, 3, 6].
# Follow-up: what if you can't use division?

#------------------- Personal Solution1 -------------------
# Personal Solution 1 - Pop the variable at current index out and multiply the rest. 
# Then append to new list. This may be an O(N^2) time and space solution depending 
# on how 'np.prod' works.
import numpy as np
def exlude_multiply1 (array_ints):
    #multiplied_array = np.array([])
    multiplied_array = []
    for i in range(len(array_ints)):
        temp_array = array_ints[:]
        temp_array.pop(i)
        multiplied_array = np.append(multiplied_array, np.prod(temp_array))
    return multiplied_array

arg = [1, 2, 3, 4, 5]
print(exlude_multiply1 (arg))

#------------------- Personal Solution2 -------------------
# Multiply the list and then divide by the variable at current index.
# Then append to new list. this is an O(N) time solution depending on how
# np.prod() functions works.
def exlude_multiply2 (array_ints):
    multiplied_array = []
    for i in range(len(array_ints)):
        multiplied_array.append(np.prod(array_ints)/array_ints[i])
    return multiplied_array

arg = [1, 2, 3, 4, 5]
print(exlude_multiply2(arg))

#------------------- Given Solution -------------------
# The given solution was longer and involved spliting the list into prefix and suffix arrays.
# Which resulted in using three for-loops, one to build the suffix and prefix and a third 
# to multiply them together. This was still an O(N) solution, because no loops were nested, 
# but it looked very cumbersome. The benifit of there approach is that it did not use any 
# advanced functions like pop() or # np.prod() and didn't use division (per the challange). 
def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result
# This runs in O(N) time and space, since iterating over the input arrays takes O(N) time
# and creating the prefix and suffix arrays take up O(N) space.

arg = [1, 2, 3, 4, 5]
print(products(arg))

#------------------- Personal Solution3 -------------------
# My third solution incorporated the given solutions themes (less compelex) by steping 
# through the list and multiplying each element together, then just skip the current index.
# This is an O(N^2) because it requires two for loops to track the current element and build
# the array

def exlude_multiply3(array_ints):
    multiplied_array = []
    for i in range(len(array_ints)):
        product = 1
        for j in range(len(array_ints)):
            if j != i:
                product = product*array_ints[j]
        multiplied_array.append(product)
    return multiplied_array

arg = [1, 2, 3, 4, 5]
print(exlude_multiply3(arg))
