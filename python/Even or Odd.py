# Title: Even or Odd
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
## Solution ##
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

## Test Case ##
test.expect(even_or_odd(2) == "Even")
test.expect(even_or_odd(0) == "Even")
test.expect(even_or_odd(7) == "Odd")
test.expect(even_or_odd(1) == "Odd")
test.expect(even_or_odd(-1) == "Odd")