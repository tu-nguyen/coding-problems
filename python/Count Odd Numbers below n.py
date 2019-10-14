# Title: Count Odd Numbers below n
# Rank: 8 kyu 
# Language Version: Python 3.4.3

## Instructions ##
# Given a number n, return the number of positive odd numbers below n, EASY!
# oddCount(7) //=> 3, i.e [1, 3, 5]
# oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
# Expect large Inputs!
# 
## Solution ##
import math
def odd_count(n):
    return math.floor(n / 2)

## Test Case ##
Test.it("Basic tests")
Test.assert_equals(odd_count(15),7)
Test.assert_equals(odd_count(15023),7511)