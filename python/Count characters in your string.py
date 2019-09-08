# Title: Count characters in your string
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }
# What if the string is empty ? Then the result should be empty object literal { }
# For C#: Use a Dictionary<char, int> for this kata!
#
## Solution ##


def count(string):
    res = {}
    for c in string:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


## Test Case ##
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
