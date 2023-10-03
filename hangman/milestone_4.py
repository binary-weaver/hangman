import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize a new Hangman game.

        Args:
            word_list (list): A list of words to choose from.
            num_lives (int, optional): The number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self._choose_random_word()
        self._initialise_word_guessed()
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def _choose_random_word(self):
        """Choose a random word from the word list."""
        self.word = random.choice(self.word_list)

    def _initialise_word_guessed(self):
        """Initialise the list to represent the hidden word with underscores."""
        self.word_guessed = ['_' for characters in self.word]
    
    def _update_word_guessed(self, guess):
        """Updates the word_guessed list with the correct guesses."""
        for index, letter in enumerate(self.word_guessed):
                if guess == letter:
                    self.word_guessed[index] = guess

    def _decrease_num_lives(self):
        """Decrease the number of lives when a guess is correct"""
        self.num_lives -= 1
    
    def check_guess(self, guess):
        """
        Check whether or not a guessed letter is correct.

        Args:
            guess (str): The letter guessed by the player.
        
        Returns:
            bool: True if the guess is correct, False otherwise.
        """
        guess = guess.lower()
        
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
            self.num_letters -= self.word.count(guess) # Reduce num_letters by the count of correct guess in word
            return self.word_guessed
        else:
            self._decrease_num_lives()
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left")
        
    def ask_for_input(self):
        """Repeatedly ask the player for their guesses and handle invalid inputs."""
        while True:
            guess = input("Guess a letter: ")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                return self.check_guess(guess)
                
