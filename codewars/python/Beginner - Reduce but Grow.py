# Title: Beginner - Reduce but Grow
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
#
## Solution ##
def grow(arr):
    res = 1
    for i in arr:
        res *= i
    return res

## Test Case ##
test.describe("Example Tests")
tests = [
    [6 , [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
]

for exp, inp in tests:
    test.assert_equals(grow(inp), exp)