# Title: Your order, please
# Rank: 8 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""
#
## Solution ##
def order(sentence):
    li = sentence.split()
    res = []
    if sentence == "":
        return ""
    else:
        for i in range(1, len(li) + 1):
            for j, v in enumerate(li):
                if str(i) in v:
                    res.append(v)  
    return " ".join(res)

## Test Case ##
Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
Test.assert_equals(order(""), "")