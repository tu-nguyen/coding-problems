# Title: The Book of Mormon
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# The Mormons are trying to find new followers and in order to do that they embark on missions.
# Each time they go on a mission, every Mormons converts a fixed number of people (reach) into followers. This continues and every freshly converted Mormon as well as every original Mormon go on another mission and convert the same fixed number of people each. The process continues until they reach a predefined target number of followers (input into the model).
# Converted Mormons are unique so that there's no duplication amongst them.
# Create a function Mormons(startingNumber, reach, target) that calculates how many missions Mormons need to embark on, in order to reach their target. While each correct solution will pass, for more fun try to make a recursive function.
# All model inputs are valid positive integers.
#
## Solution ##
def mormons(starting_number, reach, target):
    conv = starting_number
    iter = 0
    
    while conv < target:
        iter += 1
        conv += conv * reach
        
    return iter

## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(mormons(10,3,9),0)#No missions are needed because the number of followers already exceeds target
Test.assert_equals(mormons(99,2,99),0)
Test.assert_equals(mormons(40,2,120),1)
Test.assert_equals(mormons(40,2,121),2)
Test.assert_equals(mormons(20000,2,7000000000),12)#Mormons dominate the world!