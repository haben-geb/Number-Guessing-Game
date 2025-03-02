"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random



def start_game():
    print("Welcome to the Number Guessing Game!")
    print("-" * 41)
    hidden_number = random.randint(1, 10)
    tries = 0
    highscore = []
    
    # Prompts user for a number and gives hints until
    # user guesses the correct number while tracking
    # the number of attempts made by the user
    while True:
        try:
            guess = int(input("Guess the hidden number between 1 and 10: "))
            if guess not in range(1, 11):
                raise ValueError()
        except ValueError:
            print(f"Enter a valid input: a whole number between 1 and 10")
        else:
            tries += 1
            if guess > hidden_number:
                print("It's lower")
            elif guess < hidden_number:
                print("It's higher")
            else:
                # Prompts user if they would like to play again
                # while storing the user's highest score
                print("You got it!")
                print(f"It took you {tries} tries to guess the number {hidden_number}.\n")
                highscore.append(tries)
                playAgain = input("Do you want to play again? (y/n): ")
                if playAgain == "y":
                    print(f"\nTHE CURRENT HIGHSCORE IS: {min(highscore)}\n")
                    tries = 0
                    hidden_number = random.randint(1, 10)
                    continue
                elif playAgain == "n":
                    break
    print("Thank you for playing! Game closing...")

start_game()
