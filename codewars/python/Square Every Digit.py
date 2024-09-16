# Title: Square Every Digit
# Rank: 7 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
#
## Solution ##
def square_digits(num):
    res = ""
    for c in str(num):
        res += str(int(c) ** 2)
    return int(res)

## Test Case ##
test.assert_equals(square_digits(9119), 811181)