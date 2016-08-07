# Variables in Python

In this section, we will introduce variables and strings, going indepth into both. If files are included with a 
section, it will be mentioned.


## Variables

A variable is something that holds a value that may change. Think of it like a box that you can put stuff in, look at, 
and swap out whenever you want. Look at the example below.
```python
# File
some_number = 7
print someNumber
# Endfile, output below
7
```

The code creates a variable called `someNumber` and assigns it the integer value 7. When we try to print `someNumber`, 
Python finds where we declared it and prints out the value we assigned to it. Declaring/Instantiating a variable in 
Python follows this construct:
```
my_variable_name = integer/long | string | boolean | float | Object | list | expression | dictionary  # Don't worry about dictionaries yet.
```

As you can see, a variable can be set to many different things. The name of the variable - on the left side - can be 
anything as long as it starts with a letter A-Z and/or a '_'. Try to be as specific as possible when naming variables, 
because it makes the code easier to read. If a variable holds the number of students in a class, then call it 
`num_of_students`. If you need more than one word in a variable name, split the words with an underscore and do not 
capitalize.

The right side of the declaration can be any of any type. Each of the types are explained below.


#### Integers & Longs

* Integers - Integers are positive or negative whole numbers with no decimal point. 
    - Examples: `5, 4, 7, 10, -15, 0, 100, -145`
    - Creation: Either you can just put the number like `5` or if you have a string that can be turned into a number,
    wrap it in `int(<string>)` like `int("5")` will equal `5`.
* Longs - Longs are integers of unlimited size, written like integers and followed by an "L". Use these when a number 
is too large for an Integer.
    - Examples: `10000000L, -100323434L, 134234245345L`
    - Creation: Either you can just put the number like `10000000L` or if you have a string that can be turned into a number,
    wrap it in `long(<string>)` like `long("100000000")` will equal `100000000L`.
    
    
#### String

A string is a collection of characters with a length equal to the number of characters in it. A character is any alpha-
numeric symbol - A-Z, 0-9, !@#$% - such as `"Hello World", "c", "!dfdfwer", "I am a string!"`. A string can also have 
length zero and be equivalent to `""`. Strings can be single or double quoted. 

* If you want the same quote type inside of the string, then you have to 'escape' it by putting a `\` in front of it -
example: `"He said to me, \"Woah\""`. If you don't want to escape it, then you can put `r` infront of it like so

```python
print 'C:\\nowhere'  # Will be escaped to print 'C:\nowhere'
print r'C:\\nowhere' # Will print as is. 'C:\\nowhere'
```


