"""Word Guessing Game.

Guess a randomly chosen word one letter at a time.
The first and last letters are revealed as hints.
"""

import random

MAX_ATTEMPTS = 10

WORDS = [
    'apple', 'ant', 'banana', 'bear', 'cat', 'coke', 'dog', 'duck',
    'eagle', 'elephant', 'fox', 'frog', 'geeks', 'giraffe', 'hat', 'horse',
    'igloo', 'island', 'jacket', 'jelly', 'kangaroo', 'kite', 'lemon', 'lion',
    'monkey', 'moon', 'nest', 'night', 'owl', 'ox', 'panda', 'pizza',
    'queen', 'quilt', 'rabbit', 'rose', 'sparrow', 'sprite', 'tiger', 'train',
    'umbrella', 'unicorn', 'van', 'violin', 'whale', 'wolf', 'xenon', 'xylophone',
    'yacht', 'yak', 'zebra', 'zoo',
]


def show_progress(word, guessed):
    """Return the word with unguessed letters replaced by underscores."""
    return ' '.join(ch if ch in guessed else '_' for ch in word)


def is_word_guessed(word, guessed):
    """Return True when every letter of the word has been guessed."""
    return all(ch in guessed for ch in word)


def is_valid_guess(guess):
    """A valid guess is exactly one alphabetic character."""
    return len(guess) == 1 and guess.isalpha()


def game():
    """Play one round of the game."""
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    attempts = MAX_ATTEMPTS

    # Reveal first and last letters as hints (skip very short words).
    if len(word) >= 3:
        guessed.update({word[0], word[-1]})

    print("Welcome to the Word Guessing Game!")

    while attempts > 0:
        print(f"\nWord      : {show_progress(word, guessed)}")
        print(f"Attempts  : {attempts}")
        if wrong:
            print(f"Wrong     : {', '.join(sorted(wrong))}")

        guess = input("Enter a letter: ").strip().lower()

        if not is_valid_guess(guess):
            print("Please enter exactly one alphabetic character.")
            continue

        if guess in guessed or guess in wrong:
            print("You already tried that letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print("Nice guess!")
            if is_word_guessed(word, guessed):
                print(f"\n🎉 Congrats! You guessed the word: {word}")
                return
        else:
            wrong.add(guess)
            attempts -= 1
            print("Not quite, try again.")

    print(f"\nBetter luck next time 👍 The word was: {word}")


def main():
    while True:
        game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
