# Title: Logical calculator
# Rank: 8 kyu
# Language Version: Python 2.7.4

## Instructions ##


## Solution ##
# Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their size is in the range 1-50.
# Links referring to logical operations: AND, OR and XOR.
# You should begin at the first value, and repeatedly apply the logical operation across the remaining elements in the array sequentially.
# First Example:
# Input: true, true, false, operator: AND
# Steps: true AND true -> true, true AND false -> false
# Output: false
# Second Example:
# Input: true, true, false, operator: OR
# Steps: true OR true -> true, true OR false -> true
# Output: true
# Third Example:
# Input: true, true, false, operator: XOR
# Steps: true XOR true -> false, false XOR false -> false
# Output: false
# Input:
# boolean array, string with operator' s name: 'AND', 'OR', 'XOR'.
# Output:
# calculated boolean
#
## Test Case ##
Test.describe('Basic tests')
Test.assert_equals(logical_calc([True, False], "AND"), False)
Test.assert_equals(logical_calc([True, False], "OR"), True)
Test.assert_equals(logical_calc([True, False], "XOR"), True)

Test.assert_equals(logical_calc([True, True, False], "AND"), False)
Test.assert_equals(logical_calc([True, True, False], "OR"), True)
Test.assert_equals(logical_calc([True, True, False], "XOR"), False)
