import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Funcion to check user's guess against actual answer.


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {guess}.")

# Set difficulty


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty == 'hard':
        turns = HARD_LEVEL_TURNS
    else:
        turns = EASY_LEVEL_TURNS
    return turns


def guessing_game():
    # Choosing a random number between 1 and 100
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()

    # Repeat the guessign functionality if they it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


guessing_game()
