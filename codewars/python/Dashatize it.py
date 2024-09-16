# Title: Dashatize it
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.
# Ex:
# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'
#
## Solution ##


def dashatize(num):
    if num is 0 or num is 1 or num is None:
        return str(num)
    elif num is -1:
        return "1"

    num = abs(num)

    s = str(num)
    res = ""
    for c in range(len(s)):
        if c + 1 == len(s):
            res += (s[c])
            break
        elif int(s[c]) % 2 != 0:
            res += (s[c] + "-")
        elif int(s[c]) % 2 == 0 and int(s[c + 1]) % 2 != 0:
            res += (s[c] + "-")
        elif int(s[c]) % 2 == 0 and int(s[c + 1]) % 2 == 0:
            res += (s[c] + "")

    return res


## Test Case ##
test.describe('Basic')
test.assert_equals(dashatize(274), "2-7-4", "Should return 2-7-4")
test.assert_equals(dashatize(5311), "5-3-1-1", "Should return 5-3-1-1")
test.assert_equals(dashatize(86320), "86-3-20", "Should return 86-3-20")
test.assert_equals(dashatize(974302), "9-7-4-3-02", "Should return 9-7-4-3-02")
test.describe('Weird')
test.assert_equals(dashatize(None), "None", "Should return None")
test.assert_equals(dashatize(0), "0", "Should return 0")
test.assert_equals(dashatize(-1), "1", "Should return 1")
test.assert_equals(dashatize(-28369), "28-3-6-9", "Should return 28-3-6-9")
