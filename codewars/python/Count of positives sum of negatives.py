# Title: Count of positives / sum of negatives
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
#
## Solution ##
def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    else:
        return [sum(1 for i in range(len(arr)) if arr[i] > 0), sum(i for i in arr if i < 0)]

## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
Test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
Test.assert_equals(count_positives_sum_negatives([1]),[1,0])
Test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
Test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
Test.assert_equals(count_positives_sum_negatives([]),[])