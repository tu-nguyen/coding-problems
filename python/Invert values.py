# Title: Invert values
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.
#
## Solution ##
def invert(lst):
    return list(map(lambda x: -x, lst))

## Test Case ##
Test.it("Basic Tests")
Test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
Test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
Test.assert_equals(invert([]), [])