# Title: Complementary DNA
# Rank: 7 kyu
# Language Version: Python 3.6.0

## Instructions ##
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# If you want to know more http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#
## Solution ##
def DNA_strand(dna):
    compl = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"}
    res = ""
    
    for i in range(len(dna)):
        res += compl[dna[i]]
        
    return res

## Test Case ##
Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")