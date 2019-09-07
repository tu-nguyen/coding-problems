# Title: Create Phone Number
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:
# create_phone_number(phnum, (const unsigned char[]){1,2,3,4,5,6,7,8,9,0});
#     /* phnum <- "(123) 456-7890" */
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!
#
## Solution ##


def create_phone_number(n):
    # your code here
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(create_phone_number(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number(
    [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
