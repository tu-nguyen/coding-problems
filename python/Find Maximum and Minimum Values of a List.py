# Title: Find Maximum and Minimum Values of a List
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
# #Examples
# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5
# minimun([42, 54, 65, 87, 0]) returns 0
# #Notes
# You may consider that there will not be any empty arrays/vectors.
#
## Solution ##
def minimun(arr):
    return min(arr)

def maximun(arr):
    return max(arr)

## Test Case ##
Test.describe("Basic tests")
Test.it("Fixed Min")
Test.assert_equals(minimun([-52, 56, 30, 29, -54, 0, -110]), -110)
Test.assert_equals(minimun([42, 54, 65, 87, 0]), 0)
Test.assert_equals(minimun([1, 2, 3, 4, 5, 10]), 1)
Test.assert_equals(minimun([-1, -2, -3, -4, -5, -10]), -10)
Test.assert_equals(minimun([9]), 9)

Test.it("Fixed Max")
Test.assert_equals(maximun([-52, 56, 30, 29, -54, 0, -110]), 56)
Test.assert_equals(maximun([4,6,2,1,9,63,-134,566]), 566)
Test.assert_equals(maximun([5]), 5)
Test.assert_equals(maximun([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
Test.assert_equals(maximun([9]), 9)