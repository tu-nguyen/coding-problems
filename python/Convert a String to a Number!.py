# Title: Convert a String to a Number!
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Note: This kata is inspired by Convert a Number to a String!. Try that one too.
# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
# Examples
# stringToNumber("1234") == 1234
# stringToNumber("605" ) == 605
# stringToNumber("1405") == 1405
# stringToNumber("-7"  ) == -7
#
## Solution ##
def string_to_number(s):
    return int(s)

## Test Case ##
test.assert_equals( string_to_number("1234"), 1234)
test.assert_equals( string_to_number("605"), 605)
test.assert_equals( string_to_number("1405"), 1405)
test.assert_equals( string_to_number("1234"), 1234)