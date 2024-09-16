# Title: Sum Arrays
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.
# Examples
# print sum_array([1 2 3])
# > 6
# print sum_array([])
# > 0
# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.
#
## Solution ##
def sum_array(a):
    return sum(a)

## Test Case ##
test.describe("Testing sum_array")

test.assert_equals(sum_array([]), 0)
test.assert_equals(sum_array([1, 2, 3]), 6)
test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
test.assert_equals(sum_array([4, 5, 6]), 15)
test.assert_equals(sum_array(range(101)), 5050)