# Title: String repeat
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Write a function called repeatString which repeats the given String src exactly count times.
# repeatStr(6, "I") // "IIIIII"
# repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
#
## Solution ##
def repeat_str(repeat, string):
    return string * repeat

## Test Case ##
test.describe("Example Tests")
test.assert_equals(repeat_str(4, 'a'), 'aaaa')
test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
