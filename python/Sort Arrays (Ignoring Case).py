# Title: Sort Arrays (Ignoring Case)
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Sort the given strings in alphabetical order, case insensitive. For example:
# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

## Solution ##


def sortme(words):
    words = sorted(words, key=str.lower)
    return words


## Test Case ##
Test.assert_equals(sortme(["Hello", "there", "I'm", "fine"]), [
                   "fine", "Hello", "I'm", "there"])
Test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
Test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])
