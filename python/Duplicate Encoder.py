# Title: Duplicate Encoder
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes

# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

## Solution ##


def duplicate_encode(word):
    res = ""
    for i in word.lower():
        if word.lower().count(i) > 1:
            res = res + ")"
        else:
            res = res + "("
    return res


## Test Case ##
Test.assert_equals(duplicate_encode("din"), "(((")
Test.assert_equals(duplicate_encode("recede"), "()()()")
Test.assert_equals(duplicate_encode("Success"), ")())())",
                   "should ignore case")
Test.assert_equals(duplicate_encode("(( @"), "))((")
