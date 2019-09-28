# Title: Sum of Digits / Digital Root
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# In this kata, you must create a digital root function.
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
# Here's how it works:
# digital_root(16)
# => 1 + 6
# => 7
#
## Solution ##
def digital_root(n):
    if n < 10:
        return n
    else:
        n = sum(int(str(n)[i]) for i in range(len(str(n))) )       
        return digital_root(n)

## Test Case ##
test.assert_equals( digital_root(16), 7 )
test.assert_equals( digital_root(456), 6 )