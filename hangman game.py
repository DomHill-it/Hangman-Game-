# Hangman game

import time
import random
from time import sleep

# Welcome and Game Rules
print("Hi player, Welcome to Hangman. I'm pretty sure you know how  the game works")
print("If your new, the game goes like this:")
print("There are 10 words, one word will be chosen at random")
print("a random word will be chosen and you can pick your letters")
print("Once the number of tries (10) run out, then you'll get")
print("the word revealed to you.")
print("Ok, ")
print("First, Let's start with your name: ")

# Player inputs their name
name = input("Enter your name")

print("Hello", name)

print("")

time.sleep(1)

print("Let's play Hangman")
time.sleep(0.5)

# List of words-randomly generated
words = ["bike", "cars", "fire", "door", "acre", "easy", "goat",
         "hand", "jets", "kite"]

# Word for Hangman game
word = random.choice(words)

ltr = ''

board = [ ]
SECRET = [ ]

for char in word:
    board = board + ['[-]']
    SECRET = SECRET + [char]

print(board)

turns = 10
bad_guess = 0


while turns > 0:
    failed = 0
    for i in board:
        print(board)

    for char in SECRET:

        if char in ltr:

            print("[" + char + "]")

        else:

            failed += 1

    if failed == 0:
        print("You Won!! Congratulations!!")
        print(name, "made", bad_guess, "bad guesses")

        break

    guess = input("Guess a Letter:")

    ltr = ltr + guess

    if guess not in word:

        turns -= 1
        bad_guess = bad_guess + 1

        print("Wrong Guess! Try Again")

        print("You have", + turns, "turns remaining ")

        if turns == 0:
            print("You Lose! Better Luck Next Time")
            print(name, "made", bad_guess, "bad guesses")

            print("The word was", SECRET, "Thanks for playing!")

