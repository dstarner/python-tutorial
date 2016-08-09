import random
import urllib.request

# Create a list of strings for possible words to guess
# Your list can have any words you can think of
# To make life easier, set all the characters to uppercase or lowercase

word_list = []

print("\nFetching words, this may take a few seconds...")
url = "http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt"
text = urllib.request.urlopen(url).read()

print("Building word list...")
for line in text.splitlines():
    word_list.append(line.decode('utf-8'))

print("There are %s word options" % len(word_list))


# New code
# Pick a random word from the list
chosen_word = random.choice(word_list)

incorrect_guesses = 0  # Start this at zero and +1 each wrong guess
total_incorrect_allowed = 8  # After 6 incorrect guesses, you lose

guessed_letters = []

# Keep playing until the incorrect guesses max out
while incorrect_guesses < total_incorrect_allowed:
    print()

    has_win = True
    for letter in chosen_word:
        if letter.upper() in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            has_win = False
            print("_ ", end="")

    print("\n\nYou have %s bad guesses left.\n" % (total_incorrect_allowed - incorrect_guesses))

    if has_win:
        print("You have won!!")
        exit()

    letter = input("Please enter a single letter: ").replace(" ", "")
    if len(letter) > 1 or letter.upper() in guessed_letters:
        print("Bad input!")
    else:
        if letter.upper() in chosen_word.upper():
            print("%s is in the word!" % letter.upper())
        else:
            print("%s is not in the word!" % letter.upper())
            incorrect_guesses += 1
        guessed_letters.append(letter.upper())


print("You lost! Your man is dead! The word was %s." % chosen_word)