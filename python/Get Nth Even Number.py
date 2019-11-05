# Title: Get Nth Even Number
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Return the Nth Even Number
# nthEven(1) //=> 0, the first even number is 0
# nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)
# nthEven(100) //=> 198
# nthEven(1298734) //=> 2597466
# The input will not be 0.
#
## Solution ##


def nth_even(n):
    return n * 2 - 2


## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(nth_even(1), 0)
Test.assert_equals(nth_even(2), 2)
Test.assert_equals(nth_even(3), 4)
Test.assert_equals(nth_even(100), 198)
Test.assert_equals(nth_even(1298734), 2597466)
