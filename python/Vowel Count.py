# Title: Vowel Count
# Rank: 7 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.
#
# def getCount(inputStr):
#     num_vowels = 0
#     # your code here
#
#     return num_vowels
#
## Solution ##


def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = ["a", "e", "i", "o", "u"]
    for i in inputStr:
        if i in vowels:
            num_vowels += 1

    return num_vowels


## Test Case ##
test.assert_equals(getCount("abracadabra"), 5)
