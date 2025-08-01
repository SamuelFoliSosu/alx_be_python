"""

Challenge
Let’s create a fun game using Match Case statements! In this game, the user tries to guess a secret number chosen by the program.

Here’s what your program should do:

Import the random module: At the beginning of your code, add the line import random. This allows you to use functions from the random module, like generating random numbers.
Generate a secret number: Use random.randint(1, 10) to generate a random number between 1 and 10 (you can adjust the range if you want). Store this in a variable called secret_number.
Get user’s guess: Prompt the user to guess the number using input(). Convert the user’s input to an integer using int(). Store this in a variable called guess.
Match the guess:Use a Match Case statement to compare the user’s guess with the secret number:
If the guess is correct, display a message like “Congratulations, you guessed it!”
If the guess is too high, display a message like “Oops, your guess is a bit high. Try again!”
If the guess is too low, display a message like “Nope, your guess is a bit low. Give it another shot!”
Offer to play again: Ask the user if they want to play again using an if statement and user input.
Bonus Challenge:
Add a counter to keep track of the number of guesses the user takes.
Display the number of guesses it took the user to win the game.
Example Gameplay:
I'm thinking of a number between 1 and 10. Can you guess it?
5
Nope, your guess is a bit low. Give it another shot!
7
Congratulations, you guessed it!
Play again? (yes/no)
yes
... (new game starts)

"""
#importing the random module
import random

#secret number is any random number between 1 and 10
secret_number = random.randint(1,10)
print(secret_number)

#take user guess input
guess = int(input("\nI'm thinking of a number between 1 and 10. Can you guess it?"))

#initialize attempt counter
attempt = 0

play_again = "yes"

# """
#check user's guess against secret number
match guess:
    case guess if guess > secret_number:
        print("Oops, your guess is a bit high. Try again! :")
        attempt += 1
        guess = int(input())

    case guess if guess < secret_number:
        print("Nope, your guess is a bit low. Give it another shot! :")
        attempt += 1
        guess = int(input())

    case guess if guess == secret_number:
        attempt += 1
        print(f"Congratulations, you guessed it in {attempt} attempt(s)!")
# """