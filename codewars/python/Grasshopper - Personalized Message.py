# Title: Grasshopper - Personalized Message
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Personalized greeting
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
# Use conditionals to return the proper message:
# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'
#
## Solution ##


def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


## Test Case ##
test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')
