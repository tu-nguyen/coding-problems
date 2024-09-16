# Title: Calculate average
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Write function avg which calculates average of numbers in given list.
# Python:
# Due to rounding issues please do not use statistics.mean or such.
# If the array is empty, return 0.
#
## Solution ##
def find_average(arr):
    return sum(arr)/len(arr)

## Test Case ##
Test.describe('Example test')
array = [ 1, 2, 3 ]
Test.assert_equals(find_average(array), 2)