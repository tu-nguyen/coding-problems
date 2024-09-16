# Title: Friend or Foe?
# Rank: 7 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
# i.e.
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.
#
## Solution ##


def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res


## Test Case ##
Test.assert_equals(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
