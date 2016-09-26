import random


word_list = ["pizza", "tomato", "pepper", "gingersnap", "oreos"]
chosen_word = random.choice(word_list)

guessed_letters = []

total_incorrect_allowed = 6
incorrect_guesses = 0

while incorrect_guesses < total_incorrect_allowed:
   
    has_won = True
    for letter in chosen_word:
        if letter.upper() in guessed_letters:
             print(letter.upper(), end=" ")
        else:
             has_won = False
             print("_ ", end=" ")

    print("\n\nYou have %s bad guesses left.\n" % (total_incorrect_allowed - incorrect_guesses))

    if has_win:
        print("You have won!!")
        exit()

    letter = input(“Please enter a single letter”).replace(“ ”, “”)

    if len(letter) > 1 or letter.upper() in guessed_letters:
        print("Bad input!")
    else:
        if letter.upper() in chosen_word.upper():
            print("%s is in the word!" % letter.upper())
        else:
            print("%s is not in the word!" % letter.upper())
            incorrect_guesses = incorrect_guesses + 1
        guessed_letters.append(letter.upper())

print(“YOU LOST! The word was %s.” chosen_word)
