# Title: Abbreviate a Two Word Name
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot seperating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F
#
## Solution ##
def abbrevName(name):
    return ".".join(i[0] for i in name.split()).upper()

## Test Case ##
Test.assert_equals(abbrevName("Sam Harris"), "S.H");
Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
Test.assert_equals(abbrevName("Evan Cole"), "E.C");
Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
Test.assert_equals(abbrevName("David Mendieta"), "D.M");