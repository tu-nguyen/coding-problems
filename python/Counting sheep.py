# Title: Counting sheep
# Rank: 8 kyu
# Language Version: 3.6.0

## Instructions ##
# Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined
#
## Solution ##
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

## Test Case ##
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
test.assert_equals(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))