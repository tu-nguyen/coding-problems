# Title: Removing Elements
# Rank: 8 kyu
# Language Version: Python

## Instructions ##
# Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.
# Example:
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!
#
## Solution ##


def remove_every_other(my_list):
    return [my_list[l] for l in range(len(my_list)) if l % 2 == 0]


## Test Case ##
test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                   ['Hello', 'Hello Again'])
test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   [1, 3, 5, 7, 9])
test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                   [['Goodbye']])
