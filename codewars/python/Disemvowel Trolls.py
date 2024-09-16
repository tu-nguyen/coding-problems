# Title: Disemvowel Trolls
# Rank: 7 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
#
## Solution ##
def disemvowel(string):
    return "".join(c for c in string if c not in "aeiouAEIOU")

## Test Case ##
test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")