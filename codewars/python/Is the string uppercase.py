# Title: Is the string uppercase?
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Is the string uppercase?
# Task
# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
# is_uppercase("c") == False
# is_uppercase("C") == True
# is_uppercase("hello I AM DONALD") == False
# is_uppercase("HELLO I AM DONALD") == True
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
# is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.
#
## Solution ##


def is_uppercase(inp):
    for c in inp:
        if c.islower():
            return False
    return True
## Test Case ##


def gen_test_case(inp, res):
    test.assert_equals(is_uppercase(inp), res, inp)


test.describe("Basic Tests")

gen_test_case("c", False)
gen_test_case("C", True)
gen_test_case("hello I AM DONALD", False)
gen_test_case("HELLO I AM DONALD", True)
