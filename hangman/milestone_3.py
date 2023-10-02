def check_guess(guess):
    guess = guess.lower()    

    if guess in word:  
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")   

def ask_for_input():
    while True:
        guess = input("Guess a letter: ") # Ask user to input letter

        if guess.isalpha() and len(guess) == 1:  # Checks if guess is a single letter alphabetical character
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()