# Title: Find numbers which are divisible by given number
# Rank: 8 kyu 
# Language Version: Python 3.6.0

## Instructions ##
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.
# Example
# divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
# 
## Solution ##
def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]

## Test Case ##
Test.describe("Fixed tests")
Test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
Test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
Test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
Test.assert_equals(divisible_by([0], 4), [0])
Test.assert_equals(divisible_by([1,3,5], 2), [])
