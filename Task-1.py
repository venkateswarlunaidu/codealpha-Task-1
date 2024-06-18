
import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        else:
            guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts += 1
            print(f"Attempts left: {max_attempts - attempts}")

        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        if attempts == max_attempts:
            print("You've run out of attempts! The word was:", word)
            break

if __name__ == "__main__":
    hangman()
