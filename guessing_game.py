import math
from msilib.schema import MsiAssemblyName

def guessingGame():
    guessingGame = True
    bottom = 0
    top = 100
    # Note: Python's official style guide recommends 'snake_case' (as opposed to camelCase). https://peps.python.org/pep-0008/
    bottomRange = bottom
    topRange = top # Redeclared bottomRange and TopRange -> if you declared it here, you don't need it up top
    print('Choose a number between 0 and 100: ')
    myNumber = int(input())
    max_tries = math.ceil(math.log2((topRange - bottomRange) + 1))
    print("Max Tries: " + str(max_tries))
    tries = 1
    computersGuess = None
    # is the number greater than or less than the guess
    # if the computer guesses incorrectly, we want it to make another guess (as far as maxTries lets it).
    # we have a max number of tries defined by max_tries.
    while myNumber != computersGuess and max_tries > 0:
        # Initial computer's guess is right in the middle.
        # the computer should guess differently, based on the feedback we give it (larger/smaller)
        computersGuess = int((topRange + bottomRange) / 2)
        # we want to figure see what the computer's guesses are
        print('My guess is...', computersGuess)
        # HOWTO? Binary Search
        # in order to find something, we will split to see if it is in a left half (guess > middle) or right half (guess < middle)
        # we keep going with each half until we find the number in the middle.
        if myNumber > computersGuess:
            print('my Number was larger than the guess.')
            bottomRange = computersGuess + 1
            max_tries -= 1
        elif myNumber < computersGuess:
            print('my Number was less than the guess.')
            topRange = computersGuess - 1
            max_tries -= 1
        tries += 1
    # Computer guessed correctly, and now we escaped the while loop!
    if myNumber == computersGuess:
        print(f'the computer guessed myNumber correctly in {tries - 1} tries! Computer wins!')
    else:
        print(f'computer failed to guess in {tries - 1} tries')
    print(f'tries left: {max_tries}')

def main():
    print('Alvin\'s guessing game')
    guessingGame()

main()