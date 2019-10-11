# Title: Double Char
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  "
#
## Solution ##
def double_char(s):
    return "".join([c * 2 for c in s])

## Test Case ##
test.assert_equals(double_char("String"),"SSttrriinngg")
test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
test.assert_equals(double_char("1234!_ "),"11223344!!__  ")
