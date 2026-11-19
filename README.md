# Word Guessing Game

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-5%20passing-brightgreen.svg)](#run-the-tests)
[![Dependencies](https://img.shields.io/badge/dependencies-none-blue.svg)](#requirements)

A small, dependency-free terminal game written in Python. A random word is selected, and you uncover it one letter at a time before running out of attempts. It is a clean example of a beginner-friendly command-line application with unit tests.

## Why this project

- **Zero setup** - only the Python standard library is required.
- **Quick to play** - one command starts a full game with a play-again loop.
- **Easy to learn from** - small, readable functions with focused unit tests.
- **Fair gameplay** - hints are revealed up front, and only wrong guesses cost an attempt.

## Features

- Random word selected from an A-Z word list (`apple`, `ant`, `banana`, ..., `zoo`)
- First and last letters revealed as starting hints
- 10 attempts; repeated and invalid guesses do not cost an attempt
- Case-insensitive input with validation for a single alphabetic character
- Tracks wrong letters and ignores repeated guesses
- Play-again option after every round

## Quick start

```bash
git clone https://github.com/sarveshkamdi7-collab/word-guessing-game.git
cd word-guessing-game
python word_guessing_game.py
```

Python 3.8 or newer is all you need. There is nothing to install.

## How to play

1. Start the game; the first and last letters of the hidden word are already revealed.
2. Type one letter and press Enter. Correct letters are filled in automatically.
3. Each wrong letter costs one attempt. You have **10 attempts** in total.
4. Guess the whole word before the attempts run out to win.
5. Choose `y` when asked to play again, or anything else to exit.

### Example session

```text
Welcome to the Word Guessing Game!

Word      : p _ z _ a
Attempts  : 10
Enter a letter: i
Not quite, try again.

Word      : p _ z _ a
Attempts  : 9
Wrong     : i
Enter a letter: p
Nice guess!
```

## Run the tests

The test suite covers the helper functions and runs in under a second.

```bash
python -m unittest -v
```

Expected result: `Ran 5 tests ... OK`.

## Project structure

```text
word-guessing-game/
├── word_guessing_game.py        # game logic and command-line entry point
├── test_word_guessing_game.py   # unit tests for the helper functions
├── README.md                    # project overview and usage guide
├── LICENSE                      # MIT license
└── .gitignore                   # Python cache and environment ignores
```

## Requirements

- Python 3.8+
- No external libraries (standard library only)

## Possible improvements

- Load words from a JSON or text file
- Add difficulty levels with different attempt counts
- Draw an ASCII hangman as attempts are used
- Keep score across rounds

## License

Released under the [MIT License](LICENSE). Free to use, modify, and share.

## Author

[Sarvesh Kamdi](https://github.com/sarveshkamdi7-collab)
