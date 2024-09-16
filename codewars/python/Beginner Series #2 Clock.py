# Title: Beginner Series #2 Clock
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to miliseconds.
# #####Example:
# past(0, 1, 1) == 61000
# Note! h, m and s will be only Natural numbers! Waiting for translations and Feedback! Thanks!
#
## Solution ##


def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)


## Test Case ##
test.assert_equals(past(0, 1, 1), 61000)
test.assert_equals(past(1, 1, 1), 3661000)
test.assert_equals(past(0, 0, 0), 0)
test.assert_equals(past(1, 0, 1), 3601000)
test.assert_equals(past(1, 0, 0), 3600000)
