# Functions and Files 
>A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide 
>better modularity for your application and a high degree of code reusing.
>
>As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own 
>functions. These functions are called user-defined functions.
>- TutorialsPoint

In Math, a function is a pre-defined equation where you pass an input - usually **X** - and get *returned* an output. 
In programming, a function works the same way, but instead of an equation, the function is a code block.

Examples of functions you have already seen are `print()`, `input()`, and `random.choice()`. Like the quote above, you 
can also define your own functions like these, and they can save a lot of rewriting code! :D


## User Defined Functions

You will learn most of Python's built in functions, but to define your own function, follow the code structure below.

```
def functionname( parameters ):
   "function_docstring"
   code_block
   return [expression]
```

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

  * Function blocks begin with the keyword `def` followed by the function name and parentheses - ( ).
  * Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside 
  these parentheses. Parameters are the inputs that you will pass to the function. You can pass anything you want, but 
  make sure you check it in the function for the correct type/usability.
  * The code block within every function starts with a colon (:) and is indented.
  * The first statement of a function can be an optional statement - the documentation string of the function or 
  docstring. This lets other programmers know what the function does.
  * The statement `return [expression]` exits a function, optionally passing back an expression to the caller. A return 
  statement with no arguments is the same as return None.

An example of a function would be:
```python
def print_oddly(myString):
    """
    The function prints each letter of a string on a new line.
    myString: String variable of any size
    """
    for letter in myString:
        print(letter)

print("I am outside the function!")

myName = "Dan Starner"

print_oddly(myName)
```

* We define the function on the first line with the `def` keyword, followed by the name we want to give it - in this case `print_oddly`.
* In the parenthesis, we list what variables we want to be passed when the function is called. Here it is `myString`.
* We then declare the function docstring within the `"""`s. The docstring tells other programmers and readers what the function does.
* Inside the function and indented 4 spaces, we place the codeblock that we want to run. In this case it is the `for` loop, that prints out each letter of `myString` on a separate line. Note how everything is indented 4 spaces PLUS what it normally would be.
* The `print()` statement at the bottom is NOT a part of the function. When the indenting stops, the function stops kind of like a conditional does.
* Below the first `print()` statement, we define a variable `myName` and set it to a string.
* On the last line of the code, we call the function with its name, parentheseses, and any arguments we have to pass it. When it hits this line, it will call the code within `print_oddly` with myString being set to the value of `myName`.

Functions are **VERY** cool, because it should stop you from having to write the same line of code more than once. Let's 
say you have to write out tons of words with the letters on different lines - why you would have to do this I have no idea - 
you can just keep calling `print_oddly()` instead of writing out that `for loop` over and over, and over again...
 
## Files
If you want to read/write from a file, it is very easy.
