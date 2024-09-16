# Title: Where my anagrams at?
# Rank: 5 kyu
# Language Version: Python 3.6.0

## Instructions ##
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
#
## Solution ##


def isAna(word1, word2):
    for c in word2:
        if word2.count(c) != word1.count(c):
            return False
    return True


def anagrams(word, words):
    res = []

    for i in range(len(words)):
        if isAna(word, words[i]):
            res.append(words[i])
    return res


## Test Case ##
Test.assert_equals(
    anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams(
    'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
