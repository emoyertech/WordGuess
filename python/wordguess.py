"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""

import random

word_list = ["python", "hangman", "challenge", "programming", "developer"]

class WordGuess:
    """WordGuess game class - ready for implementation."""
    pass
def main():
    """Main method for WordGuess game."""
    pass

def random_choice(sequence):
    """Random choice method for WordGuess game."""
    return random.choice(sequence)

def get_random_word(word_list):
    """Get random word method for WordGuess game."""
    return random_choice(word_list)

def get_user_guess():
    """Get user guess method for WordGuess game."""
    return input("Enter your guess: ")

def display_word_progress(word, guessed_letters):
    """Display word progress method for WordGuess game."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

def get_user_information():
    """Get user information method for WordGuess game."""
    Person = input("Enter your name: ")
    return Person

def play_game():
    """Play game method for WordGuess game."""
    word = get_random_word(word_list)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display_word_progress(word, guessed_letters)
        guess = get_user_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            print("Incorrect!")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()