# Title: Opposites Attract
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
#
## Solution ##


def lovefunc(flower1, flower2):
    return True if (flower1 - flower2) % 2 != 0 else False


## Test Case ##
Test.assert_equals(lovefunc(1, 4), True)
Test.assert_equals(lovefunc(2, 2), False)
Test.assert_equals(lovefunc(0, 1), True)
Test.assert_equals(lovefunc(0, 0), False)
