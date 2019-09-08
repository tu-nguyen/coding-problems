# Title: Bit Counting
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
#
## Solution ##


def countBits(n):
    bit = bin(n)
    return bit.count("1")


## Test Case ##
test.assert_equals(countBits(0), 0)
test.assert_equals(countBits(4), 1)
test.assert_equals(countBits(7), 3)
test.assert_equals(countBits(9), 2)
test.assert_equals(countBits(10), 2)
