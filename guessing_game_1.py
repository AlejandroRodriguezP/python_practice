'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

def guess_machine():
    guess = int(input("please enter a number from 1-9 "))
    robot = random.choice(range(1,10))

    if guess < robot:
        print("you're too low! ")
    elif guess > robot:
        print("you're too high!")
    else:
        print("you got it! ")

guess_machine()