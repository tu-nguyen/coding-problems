# Title: Persistent Bugger
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# For example:
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.
#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
#  persistence(4) => 0   # Because 4 is already a one-digit number.
#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit
#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
#                   # 1*2*6=12, and finally 1*2=2
#  persistence(4) # returns 0, because 4 is already a one-digit number
#
## Solution ##
count = 0
def mul(n):
    res = 0
    if n > 10:
        res = 1
        for i in range(len(str(n))):           
            res = res * int(str(n)[i])
    return res

def persistence(n):
    global count
    if len(str(n)) > 1:
        count += 1
        print("count: ", count, " n: ", n)
        return persistence(mul(n))
    else: 
        res = count
        count = 0 # for some reason global var carry to next test
        return res
    print(mul(n))

## Test Case ##
Test.it("Basic tests")
Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
