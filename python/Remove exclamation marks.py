# Title: Remove exclamation marks
# Rank: 8 kyu 
# Language Version: Python 3.4.3

## Instructions ##
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
#
## Solution ##
def remove_exclamation_marks(s):
    return s.replace("!", "")

## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(remove_exclamation_marks("Hello World!"), "Hello World")
Test.assert_equals(remove_exclamation_marks("Hello World!!!"), "Hello World")
Test.assert_equals(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
Test.assert_equals(remove_exclamation_marks(""), "")
Test.assert_equals(remove_exclamation_marks("Oh, no!!!"), "Oh, no")