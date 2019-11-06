# Title: Returning Strings
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
# *[Make sure you type the exact thing I wrote or the program may not execute properly]*
#
## Solution ##


def greet(name):
    return "Hello, " + name + " how are you doing today?"


## Test Case ##
Test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
