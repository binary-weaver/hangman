import random

# Creates list containing my 5 favourite fruits
favourite_fruits = ["Apple", "Banana", "Mango", "Watermelon", "Pineapple"]
# Assign this list to a variable called word_list and prints
word_list = favourite_fruits
print(word_list)
# Assign a randomly extracted word from word_list to the variable word and prints
word = random.choice(word_list)
print(word)

# %% Takes user input for single letter
guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.lower() in "abcdefghijklmnopqrstuvwxyz":
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# %%
