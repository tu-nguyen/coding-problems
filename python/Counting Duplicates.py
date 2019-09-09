# Title: Counting Duplicates
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
#
## Solution ##


def duplicate_count(text):
    text = sorted(text.lower())
    dup = []
    count = 0
    print(text)

    for i in text:
        if i not in dup and text.count(i) >= 2:
            dup.append(i)
            count += 1
    return count


# previous attempt
#     print(text)
#     unique = "".join(set(text))
#     repCounts = []
#     dupCount = 0
#     for i in unique:
#         c = 0
#         for j in text:
#             if i == j:
#                 c += 1
#         repCounts.append(c)
#     for i in repCounts:
#         if i > 1:
#             dupCount += 1
#     return dupCount
#
## Test Case ##
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)

test.assert_equals(duplicate_count("11122333"), 3)
test.assert_equals(duplicate_count("aabbeqqww"), 4)
test.assert_equals(duplicate_count("Aab"), 1)
