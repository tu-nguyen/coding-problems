# Title: Who is going to pay for the wall?
# Rank: 8 kyu 
# Language Version: Python 3.4.3

## Instructions ##
# Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to pay for it. He begins to solicit his neighbors to petition to get the association to build the wall. Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and can only remember two letters from each of his neighbors’ names. As he collects signatures, he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.
#
# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is equal or less than two, it will return an array containing only the name as is"
#
## Solution ##
def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0] + name[1]]
    else:
        return [name]

## Test Case ##
Test.describe("Basic tests")
Test.assert_equals(who_is_paying("Mexico"),["Mexico", "Me"])
Test.assert_equals(who_is_paying("Melania"),["Melania", "Me"])
Test.assert_equals(who_is_paying("Melissa"),["Melissa", "Me"])
Test.assert_equals(who_is_paying("Me"),["Me"])
Test.assert_equals(who_is_paying(""), [""])
Test.assert_equals(who_is_paying("I"), ["I"])