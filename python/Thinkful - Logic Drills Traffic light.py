# Title: Thinkful - Logic Drills: Traffic light
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# For example, update_light('green') should return 'yellow'.
#
## Solution ##


def update_light(current):
    update = {"red": "green",
              "yellow": "red",
              "green": "yellow"}
    return update[current]


## Test Case ##
Test.assert_equals(update_light('green'), 'yellow')
Test.assert_equals(update_light('yellow'), 'red')
Test.assert_equals(update_light('red'), 'green')
