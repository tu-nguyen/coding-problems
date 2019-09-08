# Title: Simple transposition
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Simple transposition is a basic and simple cryptography technique. We make 2 rows and put first a letter in the Row 1, the second in the Row 2, third in Row 1 and so on until the end. Then we put the text from Row 2 next to the Row 1 text and thats it.
# Complete the function that recieves a string and encrypt it with this simple transposition.
# Example
# For example if the text to encrypt is: "Simple text", the 2 rows will be:
# Row 1	S	m	l		e	t
# Row 2	i	p	e	t	x
# So the result string will be: `"Sml etipetx"`
#
## Solution ##


def simple_transposition(text):
    row1 = ""
    row2 = ""
    for i in range(len(text)):
        if i % 2 == 0:
            row1 += text[i]
        else:
            row2 += text[i]
    return row1 + row2


## Test Case ##
Test.assert_equals(simple_transposition("Sample text"), "Sml etapetx")
Test.assert_equals(simple_transposition(
    "Simple transposition"), "Sml rnpstoipetasoiin")
