# Title: Exes and Ohs
# Rank: 7 kyu
# Language Version: Python 2.7.6

## Instructions ##
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
#
## Solution ##


def xo(s):
    ex = 0
    oh = 0
    for i in s:
        if i == "o" or i == "O":
            oh += 1
        if i == "x" or i == "X":
            ex += 1
    if ex == oh:
        return True
    return False


## Test Case ##
Test.expect(xo('xo'), 'True expected')
Test.expect(xo('xo0'), 'True expected')
Test.expect(not xo('xxxoo'), 'False expected')
