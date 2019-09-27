# Title: Convert boolean values to strings 'Yes' or 'No'.
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
#
## Solution ##
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

## Test Case ##
Test.assert_equals(bool_to_word(True), 'Yes')
Test.assert_equals(bool_to_word(False), 'No')