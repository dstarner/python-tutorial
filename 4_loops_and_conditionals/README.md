## Loops and Conditionals

Now I know that up to this point its been a lot of learning and not terribly a lot of doing, *BUT THAT ALL CHANGES NOW!*

Once we learn a few things in this section, you'll have most of the basics down to build some cool games and programs, 
and that is exactly what we are going to do! We are going to build a very basic version of *Hangman* to use what 
we already learned coupled with the new topic of Loops and Conditionals.

#### Don't Get HUNG up on the Details
(ah, I'm so funny!)

Before we begin programming, let's break down the game of Hangman in the same way we broke down making pancakes in the 
introduction. Instead of physical objects this time though, we need to think of how the game is played, and what is 
needed to play it. I have a small list below of what I could think of...

Things needed:

1. A random, unknown word
2. A number of wrong guesses before a loss

Gameplay Instructions:

1. Computer picks a random word.
2. The game begins a loop
    1. The user will pick a letter.
    2. If the letter was already said, restart loop.
    3. If the letter is in the word, add it.
    4. If the letter is not in the word, add 1 to bad guess count.
    5. If the word is finished, the player wins
    6. If the player used all the wrong guesses, then end the games.
    
    
#### Starting with the Variables
So before we can begin playing the game, we have to set up the all the variables using the types of variables from the 
previous lesson. Lets start with the unknown word. To pick from a word, we will need a **list** of words...Hm, see any 
words stick out in that last sentence that we should thing about?? OH YEA! A list of strings would be cool! Lets start 
there and move on... *Note that you can code this in `4_loops_and_conditionals/hangman.py`*

```python
# Create a list of strings for possible words to guess
# Your list can have any words you can think of
# To make life easier, set all the characters to uppercase or lowercase
word_list = ["pizza", "tomato", "pepper", "gingersnap", "oreos"]
```

Okay, so now we have a pretty decent sized list. We can worry about word choices after we get the rest running. Now to 
pick a random word, we are going to use a **function** that is already built into Python by default. We are going to 
introduce the **import** syntax, which lets you use code/functions for another python file, but we will go more indepth 
with it later. The Python `random` module - a module is a group of python code in a directory together - contains useful 
functions to come up with random values for most types such as booleans, numbers, and indexes of a list. We are going to 
take advantage of `random.choice( list )` which when input a list, will return a random value in the list. Let's use it 
to pick a random word from our list. *Note that `import` statements should always be at the top of a file before any 
executable code just for formality and clean code.*

```python
# New code
# Import the module named 'random' to have access to its functions
import random

# Create a list of strings for possible words to guess
# Your list can have any words you can think of
# To make life easier, set all the characters to uppercase or lowercase
word_list = ["pizza", "tomato", "pepper", "gingersnap", "oreos"]

# New code
# Pick a random word from the list
chosen_word = random.choice(word_list)
```

We now have a random word from our list!

In order to set the number of incorrect guesses and the total guesses before losing the game, we need two integer values.
We will compare the number of wrong guesses to the total guesses before losing to make sure the former is less. We also 
need a list of characters they have guessed that will start as an empty list.

```python
# ...Previous code from above...

incorrect_guesses = 0  # Start this at zero and +1 each wrong guess
total_incorrect_allowed = 6  # After 6 incorrect guesses, you lose

guessed_letters = []  # Will hold the previously guessed characters
```

Sweet, so now we have most of the stuff set up to play the game, but we aren't actually doing anything with this stuff! 
Time to take a short interlude and talk about **loops** and **conditionals**.

### Loops
>In general, statements are executed sequentially: The first statement in a function is executed first, followed by the 
>second, and so on. There may be a situation when you need to execute a block of code several number of times.
>Programming languages provide various control structures that allow for more complicated execution paths.
>A loop statement allows us to execute a statement or group of statements multiple times.
> - TutorialsPoint

The above summarizes loops. They let you perform the same block of code over and over again. The types of loops are 
below. Note that the block of code you want run should be indented with 4 spaces from the indentation of the loop 
statement.

#### While Loops
A `while` loop repeats a statement or group of statements while a given condition is TRUE. It tests the condition 
before executing the loop body. **BE CAREFUL OF INFINITE LOOPS THAT NEVER EXIT**, although sometimes they can be good.

```python
# Basic abstract usage
while BOOLEAN_EXPRESSION:
    code_block
    code_block
code_outside_of_loop

# This increments and prints out a counter
count = 0
while count <= 10:
    print(count)
    count += 1
# Will print 1 -> 10 on different lines


# This will print "Haha" forever
# Infinite loops are really only useful for game loops
while True:
    print("Haha")

```

#### For Loops
A `for` loop executes a sequence of statements multiple times and abbreviates the code that manages the loop variable. A 
for loop will take a list and go through each index in it, or it will go through each character in a string, or iterate 
through some sequence it is given.

```python

for VARIABLE in SEQUENCE | STRING | ITERATOR:
    code_block
    code_block
code_outside_of_loop

# Will run 3 times
# Will print:
# We're on time 0
# We're on time 1
# We're on time 2
for x in range(0, 3):
    print "We're on time %d" % (x)
    
    
# Iterate through a list
names = ["Dan", "Joe", "Jared"]

for name in names:
    # Each index will be the 'name' variable for its runthrough of the codeblock
    # The '%s' will get replaced by the variable after the '%' outside of the string.
    print("Hello, %s" % name)
```


    

