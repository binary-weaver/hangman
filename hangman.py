import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    _choose_random_word()
        Chooses a random word from the word list.
    _initialise_word_guessed()
        Initialises a list to represent the hidden word with underscores.
    _update_word_guessed
        Updates the word_guessed list with a correct guess.
    _decrease_number_lives
        Decreases the number of lives remaining.
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self._choose_random_word()
        self._initialise_word_guessed()
        self.list_of_guesses = []
        pass
    
    def _choose_random_word(self):
        '''Choose a random word from the word list.'''
        self.word = random.choice(self.word_list).lower()
        pass

    def _initialise_word_guessed(self):
        '''Initialise the list to represent the hidden word with underscores.'''
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word)) # Initialise variable that stores the number of unique letters in the word.
        pass

    def _update_word_guessed(self, guess):
        '''Updates the word_guessed list with a correct guess.
        
        Parameters:
        ---------
        guess: str
            The letter guessed by the player.
        '''
        updated = False
        for index, letter in enumerate(self.word):
            if letter == guess and self.word_guessed[index] != guess:
                self.word_guessed[index] = guess
                updated = True
        if updated: 
            self.num_letters -= 1
        pass

    def _decrease_num_lives(self):
        '''Decreases the number of lives when a guess is correct'''
        self.num_lives -= 1
        pass

    def check_guess(self, guess):
        '''
        Check whether or not a guessed letter is correct.

        Parameters:
        ---------
        guess: str
            The letter guessed by the player.
        '''
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self._decrease_num_lives()
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left.")
        
        self.list_of_guesses.append(guess)
        print(" ".join(self.word_guessed))
        pass

    def ask_for_input(self):
        '''Repeatedly ask the player for their guesses and handle invalid inputs.'''
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                return guess
            pass

def play_game(word_list):
    '''
    Play a Hangman game using the given word list.

    Parameters:
    ---------
    word_list: list
      A list of words to choose from in game.

    This function initialises a Hangman game with a word randomly chosen from the word list.
    The player is allowed a certain number of lives to guess the word.
    The game continues until the player either guesses all the letters in the word or runs out of lives.

    Returns:
        None
    '''
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_letters > 0:
            guess = game.ask_for_input()
            game.check_guess(guess)
        else:
            print("Congratulations. You won the game!")
            break
    pass
        
if __name__ == '__main__':
    word_list = ["Apple", "Banana", "Mango", "Watermelon", "Pineapple"]
    play_game(word_list)