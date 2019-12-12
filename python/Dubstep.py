# Title: Dubstep
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Input
# The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
# Output
# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
# Examples
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
#   # =>  WE ARE THE CHAMPIONS MY FRIEND
#
## Solution ##
import re


def song_decoder(song):
    return " ".join(re.sub(r'WUB', ' ', song).split())


## Test Case ##
Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C",
                   "WUB should be replaced by 1 space")
Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
                   "A B C", "multiples WUB should be replaced by only 1 space")
Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C",
                   "heading or trailing spaces should be removed")
