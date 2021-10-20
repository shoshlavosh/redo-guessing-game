"""A number guessing game"""

from random import randint

answer = randint(1, 101)

guess = int(input("Guess a number between 1 and 100. > "))

guesses = 0

def main_game(answer, guess, guesses):

    while guess != answer:
        if guess > answer:
            guess = int(input("Your guess is too high. Try again. > "))

        elif guess < answer:
            guess = int(input("Your guess is too low. Try again. > "))
        
        else:
            print("That's not a valid guess.")

        guesses += 1
    
    print(f"Correct! You figured out the answer in {guesses} guesses!")

main_game(answer, guess, guesses)
    
