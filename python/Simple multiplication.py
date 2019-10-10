# Title: Simple multiplication
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
#
## Solution ##
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

## Test Case ##
Test.describe("Tests")
Test.it("Fixed tests")
test.assert_equals(simple_multiplication(2), 16)
test.assert_equals(simple_multiplication(1), 9)
test.assert_equals(simple_multiplication(8), 64)
test.assert_equals(simple_multiplication(4), 32)
test.assert_equals(simple_multiplication(5), 45)