# Title: altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Rank: 8 kyu
# Language Version: Python 2.7.6

## Instructions ##
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.
#
## Solution ##
def to_alternating_case(string):
    res = ""
    for c in string:
        if c.isupper():
            res += c.lower()
        elif c.islower():
            res += c.upper()
        else:
            res += c
    return res

## Test Case ##
Test.describe("Basic tests")
Test.it("should work for fixed tests (provided in the description)")
Test.assert_equals(to_alternating_case("hello world"), "HELLO WORLD")
Test.assert_equals(to_alternating_case("HELLO WORLD"), "hello world")
Test.assert_equals(to_alternating_case("hello WORLD"), "HELLO world")
Test.assert_equals(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
Test.assert_equals(to_alternating_case("12345"), "12345")
Test.assert_equals(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
Test.assert_equals(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
Test.assert_equals(to_alternating_case(to_alternating_case("Hello World")), "Hello World")
Test.it("should work for the title of this Kata")
title = "altERnaTIng cAsE"
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE")
title = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
title = to_alternating_case(title)
Test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
title = to_alternating_case(title)
Test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")