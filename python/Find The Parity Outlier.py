# Title: Find The Parity Outlier
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
#
## Solution ##
c = []
 odd = ""
  res = 0
   for i in integers:
        if i % 2 == 0:
            c.append("even")
        else:
            c.append("odd")
    print(c)
    if c.count("even") > c.count("odd"):
        print("odd")
        res = integers[c.index("odd")]
    else:
        print("even")
        res = integers[c.index("even")]

    return res

## Test Case ##
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
