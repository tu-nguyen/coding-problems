# Title: Reverse List Order
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples
# reverse_list([1,2,3,4]) == [4,3,2,1]
# reverse_list([3,1,5,4]) == [4,5,1,3]
#
## Solution ##


def reverse_list(l):
    return l[::-1]


## Test Case ##
test.assert_equals(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
test.assert_equals(reverse_list([3, 1, 5, 4]), [4, 5, 1, 3])
