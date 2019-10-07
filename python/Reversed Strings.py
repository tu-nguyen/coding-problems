# Title: Reversed Strings
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Complete the solution so that it reverses the string value passed into it.
# solution('world') # returns 'dlrow'
#
## Solution ##
def solution(string):
    return string[::-1]

## Test Case ##
Test.expect(solution('world') == 'dlrow')
Test.expect(solution('hello') == 'olleh')
Test.expect(solution('') == '')
Test.expect(solution('h') == 'h')