import random

# Creates list containing my 5 favourite fruits
word_list = ["Apple", "Banana", "Mango", "Watermelon", "Pineapple"]
# Assign a randomly extracted word from word_list to the variable word and prints
word = random.choice(word_list)
print("The randomly chosen word is: ", word)

# Takes user input for a single letter
guess = input("Enter a single letter: ")
# Checks if input is a single character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")