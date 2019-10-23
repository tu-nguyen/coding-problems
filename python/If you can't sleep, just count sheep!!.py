# Title: If you can't sleep, just count sheep!!
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# If you can't sleep, just count sheep!!
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
#
## Solution ##
def count_sheep(n):
    return "".join([str(i) + " sheep..." for i in range(1, n + 1)])

## Test Case ##
Test.assert_equals(count_sheep(1), "1 sheep...");
Test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
Test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")