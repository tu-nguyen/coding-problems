# Title: Build Tower
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *
# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Ruby: returns an Array;
# Have fun!
# for example, a tower of 3 floors looks like below
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
# and a tower of 6 floors looks like below
# [
#   '     *     ',
#   '    ***    ',
#   '   *****   ',
#   '  *******  ',
#   ' ********* ',
#   '***********'
# ]
#
## Solution ##


def tower_builder(n_floors):
    res = []
    for i in range(n_floors):
        if i == 0:
            res.append(' ' * (n_floors - 1) + '*' *
                       (i+1) + ' ' * (n_floors - 1))
        else:
            res.append(' ' * (n_floors - i-1) + '*' *
                       (i*2+1) + ' ' * (n_floors - i-1))
    return res


## Test Case ##
test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
