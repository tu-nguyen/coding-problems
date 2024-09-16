# Title: Descending Order
# Rank: 7 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 21445 Output: 54421
# Input: 145263 Output: 654321
# Input: 1254859723 Output: 9875543221
#
## Solution ##
def Descending_Order(num):
    return int(''.join(reversed(str(num))))
    
## Test Case ##
test.assert_equals(Descending_Order(0), 0)
test.assert_equals(Descending_Order(15), 51)
test.assert_equals(Descending_Order(123456789), 987654321)