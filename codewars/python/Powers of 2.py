# Title: Powers of 2
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

## Solution ##
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]

## Test Case ##
test.describe("Example Tests")
test.assert_equals(powers_of_two(0), [1])
test.assert_equals(powers_of_two(1), [1, 2])
test.assert_equals(powers_of_two(4), [1, 2, 4, 8, 16])