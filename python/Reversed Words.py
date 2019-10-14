# Title: Reversed Words
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"
#
## Solution ##
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

## Test Case ##
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])