# Hangman

## Table of contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage) 

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

### Project Aim
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### What I Learned
- **Basic Python syntax and programming concepts:** This project reinforced my understanding of Python's syntax, data types, variables, loops, and conditional statements. It provided a practical context for applying these foundational concepts.
- **Random word selection and string manipulation:** Utilizing the random module to handle the game's word selection process provided me with insights into working with randomness in Python. The task of manipulating strings to depict both the word to be guessed and the player's progress proved to be a valuable exercise in honing my string manipulation skills.
- **User interaction and input validation:** Developing the user interface for the game, including prompting the user for guesses and handling input validation, taught me how to interact with users effectively. I learned how to validate user input to ensure that it meets specific criteria, such as being a single alphabetical character.
- **Object-Oriented Programming (OOP):** The project's structure, with a `Hangman` class that encapsulates the game's logic and state, introduced me to the principles of object-oriented programming (OOP). I gained experience in defining classes, methods, and attributes to create organized and maintainable code.
- **Error Handling and Exception Handling:** Dealing with potential errors, such as invalid input, and providing informative error messages enhanced my knowledge of error handling and exception handling in Python.

## Installation

The `hangman.py` file contains the Python code for the Hangman game implementation. This code includes the following components:

- A `Hangman` class that manages the game's logic.
- Methods for checking guesses, asking for user input, and initializing the game.
- Integration with a list of words to choose from randomly.

1. Clone this repository to your local machine using:

   ```shell
   git clone https://github.com/binary-weaver/hangman

2. Navigate to the project directory:
    ```shell
    cd hangman 
3. Run the game by executing the following command:
    ```shell
    python milestone_5.py
### Usage

- To play the Hangman game, you can run the `milestone_5.py` script using Python.  
- Follow the prompts to guess letters and try to uncover the hidden word.        
- The game will provide feedback after each guess and inform you of the outcome.