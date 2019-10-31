# Title: Convert a string to an array
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Write a function to split a string and convert it into an array of words. For example:
# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
#
## Solution ##


def string_to_array(s):
    return s.split(" ")


## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
Test.assert_equals(string_to_array("I love arrays they are my favorite"), [
                   "I", "love", "arrays", "they", "are", "my", "favorite"])
Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
Test.assert_equals(string_to_array(""), [""])
