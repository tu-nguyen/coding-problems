# Title: Beginner Series #3 Sum of Numbers
# Rank: 7 kyu
# Language Version: Python 3.6.0
## Instructions ##
# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!
# Examples
# GetSum(1, 0) == 1   // 1 + 0 = 1
# GetSum(1, 2) == 3   // 1 + 2 = 3
# GetSum(0, 1) == 1   // 0 + 1 = 1
# GetSum(1, 1) == 1   // 1 Since both are same
# GetSum(-1, 0) == -1 // -1 + 0 = -1
# GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
## Solution ##


def get_sum(a, b):
    if a == b:
        return a
    elif a > b:
        return sum(range(b, a + 1))
    else:
        return sum(range(a, b + 1))


## Test Case ##
Test.assert_equals(get_sum(0, 1), 1)
Test.assert_equals(get_sum(0, -1), -1)
