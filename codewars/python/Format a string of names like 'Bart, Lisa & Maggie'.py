# Title: Format a string of names like 'Bart, Lisa & Maggie'.
# Rank: 6 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
# namelist([])
# # returns ''
#
## Solution ##


def namelist(names):
    res = []

    if len(names) == 1:
        return names[0].get("name")
    elif len(names) == 2:
        return names[0].get("name") + " & " + names[1].get("name")

    for i in names:
        if names.index(i) == len(names) - 1:
            break
        if names.index(i) == len(names) - 2:
            s = names[names.index(i)].get("name") + " & " + \
                names[names.index(i) + 1].get("name")
            res.append(s)
        else:
            res.append(i.get("name"))
    return ", ".join(res)


## Test Case ##
Test.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
                   "Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
                   "Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa',
                   "Must work with two names")
Test.assert_equals(namelist([{'name': 'Bart'}]),
                   'Bart', "Wrong output for a single name")
Test.assert_equals(namelist([]), '', "Must work with no names")
