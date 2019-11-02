# Title: Reversing Words in a String
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# reverse('Hello World') == 'World Hello'
# reverse('Hi There.') == 'There. Hi'
#
## Solution ##


def reverse(st):
    return " ".join(st.split()[::-1])


## Test Case ##
test.describe('The Tests Given in the Instructions')
test.assert_equals(reverse('Hello World'), 'World Hello')
test.assert_equals(reverse('Hi There.'), 'There. Hi')
