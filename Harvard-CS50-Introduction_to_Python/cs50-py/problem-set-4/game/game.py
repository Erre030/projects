
#description: random number guessing game, where you input a "Level" (upper_bound). Random int gets generated from 1 to upper_bound included.
            # User guesses int and gets hints if guess too small/large. Program exits if user guesses right.
            # A counter is counting the attempts the user needed.

import random
import sys

def main():
    guessing_game()




























def guessing_game():

    upper_bound = input("Level: ")

    while True:
        try:
            upper_bound = int(upper_bound)
            if upper_bound >= 1:
                break
            else:
                raise ValueError
        except ValueError:
            upper_bound = input("Level: ")

    number = random.randint(1,upper_bound)

    guess = input("Guess: ")

    counter = 0

    while True:
        try:
            guess = int(guess)
            if guess < number:
                counter += 1
                print("Too small!")
                guess = input("Guess: ")
            elif guess > number:
                counter += 1
                print("Too large!")
                guess = input("Guess: ")
            elif guess == number:
                counter += 1
                print("Just right!")
                print(f"You needed {counter} attempts.")
                sys.exit()
        except ValueError:
            guess = input("Guess: ")



main()
