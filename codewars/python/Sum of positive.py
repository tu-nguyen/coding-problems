# Title: Sum of positive
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
#
## Solution ##
def positive_sum(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res

## Test Case ##
Test.describe("positive_sum")

Test.it("works for some examples")
Test.assert_equals(positive_sum([1,2,3,4,5]),15)
Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

Test.it("returns 0 when array is empty")
Test.assert_equals(positive_sum([]),0)

Test.it("returns 0 when all elements are negative")
Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

