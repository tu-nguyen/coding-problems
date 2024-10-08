# Title: Convert a Boolean to a String
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# In this programming exercise, you're going to learn about functions, boolean (true/false) values, strings, and the if-statement.
# A function is a block of code that takes an input and produces an output. In this example, boolean_to_string is a function whose input is either true or false, and whose output is the string representation of the input, either "true"/"True" or "false"/"False" (check the sample tests about what capitalization to use in a given language).
# A common idea we often want to represent in code is the concept of true and false. A variable that can either be true or false is called a boolean variable. In this example, the input to boolean_to_string (represented by the variable b) is a boolean.
# Lastly, when we want to take one action if a boolean is true, and another if it is false, we use an if-statement.
# For this kata, don't worry about edge cases like where unexpected input is passed to the function. You'll get to worry about these enough in later exercises.
#
## Solution ##
def boolean_to_string(b):
    return "True" if b else "False"

## Test Case ##
Test.assert_equals(boolean_to_string(True), "True", 'When we pass in true, we want the string "true" as output')
Test.assert_equals(boolean_to_string(False), "False", 'When we pass in false, we want the string "false" as output')