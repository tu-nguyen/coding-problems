# Title: Square(n) Sum
# Rank:
# Language Version:

## Instructions ##
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
#
## Solution ##
def square_sum(numbers):
    res = 0
    for i in numbers:
        res += i**2
    return res

## Test Case ##
Test.expect(square_sum([1,2]), 'squareSum did not return a value')
Test.assert_equals(square_sum([1,2]), 5)
Test.assert_equals(square_sum([0, 3, 4, 5]), 50)