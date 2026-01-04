# Guess the number game

import random  # Import random module

secret_number = random.randint(1, 20)  # Generate random secret number
print('I am thinking of a number between 1 and 20.')

# Give the player 6 guesses
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))  # Convert input to integer

    if guess < secret_number:  # Guess too low
        print('Your guess is too low.')
    elif guess > secret_number:  # Guess too high
        print('Your guess is too high.')
    else:  # Correct guess
        break

# Print result
if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))
