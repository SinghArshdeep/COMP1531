print('Hello World')


def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    b = values.copy()
    for x in values:
        if int(x) == int(guess):
            b.remove(x)
    return b

def find_closest(guess, values):
    # This function should return the value that is closest to guess
    list1 = []
    for number in values:
        list1.append(abs(int(guess)-int(number)))
    min_index = list1.index(min(list1))
    return values[min_index]

def run_game(values):
    # While there are values to be guessed and the user hasn't quit (with 'q'),
    # the game should wait for the user to input their guess and then
    # reveal whether the closest number is lower or higher.
    
    print(f'Numbers are between {MIN} and {MAX} inclusive')
    guess = input(f'There are {len(values)} values left. Guess: ')
    # Your code goes here.
    
    while guess != 'q' and len(values) != 0:
        values2 = handle_guess(guess , values)
        if len(values2) == len(values):
            number = find_closest(guess , values)
            if int(number) < int(guess):
                print(f'The  closest to {guess} is lower')
            else:
                print(f'The closest to {guess} is higher')
        else:
            print(f'You found {guess}! It was in the list')
        if len(values2) != 0:
            guess = input(f'There are {len(values2)} values left. Guess: ')
        
        else:
            print('Congratulations! You won!')
        
        values = values2

print('Thanks for playing! See you soon')
