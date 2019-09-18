# Title: Third Angle of a Triangle
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# You are given two angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
#
## Solution ##
def other_angle(a, b):
    return 180 - a - b
    
## Test Case ##
Test.assert_equals(other_angle(30, 60), 90)
Test.assert_equals(other_angle(60, 60), 60)
Test.assert_equals(other_angle(43, 78), 59)
Test.assert_equals(other_angle(10, 20), 150)