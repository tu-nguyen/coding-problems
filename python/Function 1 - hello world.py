# Title: Function 1 - hello world
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Make a simple function called greet that returns the most-famous "hello world!".
# Style Points
# Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?
#
## Solution ##
def greet():
    return "hello world!"

## Test Case ##
test.describe("Greet function")
test.it("Making sure greet exists")
test.assert_equals(greet(), "hello world!", "Greet doesn't return hello world!")