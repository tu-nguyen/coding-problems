# Title: Rock Paper Scissors!
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
# Examples:
# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!
#
## Solution ##
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    if p1 == "rock":
        if p2 == "scissors":
            return "Player 1 won!"
        elif p2 == "paper":
            return "Player 2 won!"
    if p1 == "paper":
            if p2 == "rock":
                return "Player 1 won!"
            elif p2 == "scissors":
                return "Player 2 won!"
    if p1 ==  "scissors":
            if p2 == "paper":
                return "Player 1 won!"
            elif p2 == "rock":
                return "Player 2 won!"

## Test Case ##
Test.describe('rock paper scissors')
Test.it('player 1 win')
Test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
Test.assert_equals(rps('scissors', 'paper'), "Player 1 won!")
Test.assert_equals(rps('paper', 'rock'), "Player 1 won!")

Test.it('player 2 win')
Test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
Test.assert_equals(rps('paper', 'scissors'), "Player 2 won!")
Test.assert_equals(rps('rock', 'paper'), "Player 2 won!")

Test.it('draw')
Test.assert_equals(rps('rock', 'rock'), 'Draw!')
Test.assert_equals(rps('scissors', 'scissors'), 'Draw!')
Test.assert_equals(rps('paper', 'paper'), 'Draw!')