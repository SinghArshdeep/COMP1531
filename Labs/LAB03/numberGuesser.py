'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    list = values.copy()
    for number in values:
        if (int(number) == int(guess)):
            list.remove(int(guess))
    return list

def find_closest(guess, values):
    list1 = []
    for number in values:
        list1.append(abs(int(guess)-int(number)))
    
    ref = list1.index(min(list1))
    return values[ref]
    # This function should return the value that is closest to `guess`

def run_game(values):
    # While there are values to be guessed and the user hasn't quit (with 'q'), 
    # the game should wait for the user to input their guess and then 
    # reveal whether the closest number is lower or higher.

    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    guess = input('Guess: ')
    while ( guess != 'q') and len(values) != 0:
        values1 = handle_guess(guess, values)
        if ( len(values) != len(values1)):
            print("You found ", guess, "! It was in the list")
        else:
            x = find_closest(guess, values)
            if(int(x) > int(guess)):
                print("The closest to ", guess , " is higher")
            else:
                print("The closest to ", guess , " is lower")

        if len(values1) != 0:
            guess = input(f'There are {len(values1)} values left. Guess: ')
        else:
            print('Congratulations! You won!')
        
        values = values1
    # Your code goes here.
    
    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    # Generate a random list and run the game
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)


