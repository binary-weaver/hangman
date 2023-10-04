# Hangman

## Table of contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure) 
- [License](#license)

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

- **Project Organization:** Organizing the project with clear file structure and documentation taught me the importance of project organization and documentation practices for code maintainability and collaboration.

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
    python hangman.py
    ```

### Usage

- To play the Hangman game, you can run the `hangman.py` script using Python.  
- Enter a single alphabetical character as your guess and press Enter.       
- If your guess is correct, the letter will be revealed in the word, beneath a "Good guess!" message.
- If your guess is incorrect, you lose a life, and the game will display the updated number of lives.
- Continue guessing until you either guess the entire word or run out of lives.

## File Structure

The project directory is organised as follows:

``` bash
hangman/
│
├── hangman/ # Subfolder containing project milestone
│ ├── milestone_1.py 
│ ├── milestone_2.py 
│ ├── milestone_3.py 
│ ├── milestone_4.py 
│ ├── milestone_5.py 
├── hangman.py # Complete version of the Hangman game
└── README.md # Documentation and project description 
```

## License

MIT License

Copyright (c) 2023 Moez Abdu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.