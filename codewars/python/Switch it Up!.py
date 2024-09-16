# Title: Switch it Up!
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# If your language supports it, try using a switch statement.
#
## Solution ##
def switch_it_up(number):
    nums = {0:"Zero",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine"}
    return nums[number]

## Test Case ##
Test.describe('Example tests')
Test.assert_equals(switch_it_up(0), "Zero")
Test.assert_equals(switch_it_up(9), "Nine")