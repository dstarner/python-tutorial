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
my_variable_name = integer/long | string | boolean/expression | float | Object | list | dictionary  # Don't worry about dictionaries yet.
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

Strings can be added together like so:

```python
greeting = "Hello, " + "Dan, " + " you look good today!"
print greeting
# End of file, output below
Hello, Dan, you look good today!
```

To turn a current variable into its string representation, wrap the variable in `str(value)`. If you gave it something 
like `str(5)` it will return `"5"`. If you want to print a string and number together, you must wrap the number in the 
`str()` function.


#### Boolean Expressions and Logic Operators
A Boolean value is either True or False. It is named after the British mathematician, George Boole, who first 
formulated Boolean algebra — some rules for reasoning about and combining these values. This is the basis of all modern 
computer logic. In Python, boolean values can be either `True` or `False`. 

```python
# Two different Booleans
am_i_cool = True

can_operate = False
```

An expression is a line of code that be evaluated to a Boolean. There are six boolean expression operators you should know:

```python
x == y               # Produce True if ... x is equal to y
x != y               # ... x is not equal to y
x > y                # ... x is greater than y
x < y                # ... x is less than y
x >= y               # ... x is greater than or equal to y
x <= y               # ... x is less than or equal to y

# Some examples of boolean expressions
age = 18  # Int variable
old_enough_to_get_driving_licence = age >= 16  # True
print(old_enough_to_get_driving_licence)

# Another example
number = 7
equal_to = (6 == number)  # False
```

*Boolean expressions get evaluated from most inward parenthesis to outward.*

##### Logic Operators
Coupled with Boolean expressions, Logic operators are very important to Computer Science. The three Logic Operators are 
`and`, `or`, and `not`. They are used to group multiple boolean expressions to form one boolean evaluation. They are 
good with telling if a number is in a range or not amongst other things.

```python
old_enough_to_drive = True
clean_record = False

# If they are old enough and have a clean record
low_insurance = old_enough_to_drive and clean_record

# If a drive is not old enough or has a bad record
bad_driver = not old_enough_to_drive or not clean_record

# Junior driver if their age is 16 or 17.
age = 16
junior_driver = age >=16 and age < 18
```


