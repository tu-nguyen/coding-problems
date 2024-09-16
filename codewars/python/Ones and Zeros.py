# Title: Ones and Zeros
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# Examples:
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.
#
## Solution ##


def binary_array_to_number(arr):
    res = 0
    j = 0
    for i in arr:
        res += i * 2 ** (len(arr) - 1 - j)
        j += 1
    return res


## Test Case ##
Test.describe("One's and Zero's")
Test.it("Example tests")
Test.assert_equals(binary_array_to_number([0, 0, 0, 1]), 1)
Test.assert_equals(binary_array_to_number([0, 0, 1, 0]), 2)
Test.assert_equals(binary_array_to_number([1, 1, 1, 1]), 15)
Test.assert_equals(binary_array_to_number([0, 1, 1, 0]), 6)
