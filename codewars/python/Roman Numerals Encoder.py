# Title: Roman Numerals Encoder
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:
# solution(1000) # should return 'M'
# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.
# More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
#
## Solution ##


def reverse(string):
    string = "".join(reversed(string))
    return string


def split(word):
    res = []
    z = len(word) - 1
    for i in word:
        res.append(i + ("0"*z))
        z -= 1
    return res

# ro = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
# will use on reattempt eventually


def solution(n):
    # s = reverse(str(n))
    l = split(str(n))
    res = ""

    for i in l:
        print(i)
        if int(i) >= 1000:
            res = "M" * int(int(i)/1000)
        else:
            if int(i) == 900:
                res = res + "CM"
            elif int(i) >= 500:
                res = res + "D" + "C" * int((int(i) - 500)/100)
            elif int(i) == 400:
                res = res + "CD"
            elif int(i) < 400 and int(i) >= 100:
                res = res + "C" * int(int(i)/100)
            else:
                if int(i) == 90:
                    res = res + "XC"
                elif int(i) >= 50:
                    res = res + "L" + "X" * int((int(i) - 50)/10)
                elif int(i) == 40:
                    res = res + "XL"
                elif int(i) < 40 and int(i) >= 10:
                    res = res + "X" * int(int(i)/10)
                else:
                    if int(i) == 9:
                        res = res + "IX"
                    elif int(i) >= 5:
                        res = res + "V" + "I" * int((int(i) - 5)/1)
                    elif int(i) == 4:
                        res = res + "IV"
                    elif int(i) < 4 and int(i) >= 1:
                        res = res + "I" * int(int(i)/1)
    return res


## Test Case ##
test.assert_equals(solution(1), 'I', "solution(1),'I'")
test.assert_equals(solution(4), 'IV', "solution(4),'IV'")
test.assert_equals(solution(6), 'VI', "solution(6),'VI'")
test.assert_equals(solution(14), 'XIV', "solution(14),'XIV")
test.assert_equals(solution(21), 'XXI', "solution(21),'XXI'")
test.assert_equals(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
test.assert_equals(solution(91), 'XCI', "solution(91),'XCI'")
test.assert_equals(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
test.assert_equals(solution(1000), 'M', 'solution(1000), M')
test.assert_equals(solution(1889), 'MDCCCLXXXIX',
                   "solution(1889),'MDCCCLXXXIX'")
test.assert_equals(solution(1989), 'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
