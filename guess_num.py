import random
from art.guess import logo

continue_game = True

def guess_num():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    number_to_guess = random.randint(1, 100)
    guess = None

    while guess != number_to_guess and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return

        attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses. The number was {number_to_guess}.")


while continue_game:
    print("\n" * 100)
    print(logo)
    guess_num()
    if input("Do you want to play again? Type 'y' or 'n': ").lower() != "y":
        continue_game = False
        print("Thanks for playing! Goodbye.")
