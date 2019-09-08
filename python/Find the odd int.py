# Title: Find the odd int
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
#
## Solution ##


def find_it(seq):
    for i in range(len(seq)):
        if(seq.count(seq[i]) % 2 != 0):
            return seq[i]
    return -1


## Test Case ##
test.describe("Example")
test.assert_equals(
    find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
