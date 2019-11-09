# Title: String ends with?
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
#
## Solution ##


def solution(string, ending):
    string = string[::-1]
    ending = ending[::-1]
    i = 0
    if len(ending) > len(string):
        return False
    for c in ending:
        if c == string[i]:
            i += 1
        elif c != string[i]:
            return False
    return True


## Test Case ##
test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
