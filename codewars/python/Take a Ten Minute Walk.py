# Title: Take a Ten Minute Walk
# Rank: 6 kyu
# Language Version: Python 3.6.0

## Instructions ##

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


## Solution ##
def is_valid_walk(walk):
    print(len(walk))
    if len(walk) != 10:
        return False
    else:
        long = 0
        lat = 0
        for i in walk:
            if i == 'n':
                long += 1
            if i == 's':
                long -= 1
            if i == 'w':
                lat += 1
            if i == 'e':
                lat -= 1
        if long == 0 and lat == 0:
            return True
        else:
            return False


## Test Case ##
# some test cases for you...
test.expect(is_valid_walk(['n', 's', 'n', 's', 'n',
                           's', 'n', 's', 'n', 's']), 'should return True')
test.expect(not is_valid_walk(
    ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']), 'should return False')
test.expect(not is_valid_walk(['w']), 'should return False')
test.expect(not is_valid_walk(
    ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), 'should return False')
