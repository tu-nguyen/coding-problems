# Title: Convert number to reversed array of digits
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Convert number to reversed array of digits
# Given a random number:
# C#: long;
# C++: unsigned long;
# You have to return the digits of this number within an array in reverse order.
# Example:
# 348597 => [7,9,5,8,4,3]
#
## Solution ##
def digitize(n):
    return [int(i) for i in str(n)[::-1]]

## Test Case ##
Test.assert_equals(digitize(35231),[1,3,2,5,3])