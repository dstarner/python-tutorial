# Classes

> Object-oriented programming (OOP) is a programming language model organized around 
> objects rather than "actions" and data rather than logic. Historically, a program 
> has been viewed as a logical procedure that takes input data, processes it, and 
> produces output data.
> - http://searchsoa.techtarget.com/definition/object-oriented-programming

## Object Oriented Programming
Object Oriented programming (OOP) is a higher level programming term/philosophy that is in great use 
over the older Functional Programming. In OOP, there are your primitive variables that you have 
already seen - integers, booleans, strings... - but there are also variables that can be **objects** 
that can contain as much information as desired. Its a way to more easily represent the world around us.
Think of any object, for this we will use a car. We can identity as few or as many ways to describe the car. 

* Brand       - "Jeep"
* Make        - "Liberty"
* Year        - 2006
* Owner       - "Daniel Starner"
* # of Wheels - 4  --> You'll see why this is used.

We COULD represent all those values as different variables, but that would get very hard to follow once you 
introduce more and more cars...An easier way to handle all that data is to use a class! In Python and other 
OOP languages, classes let you define an Object - like a car - and easily assign it different attributes that 
can be pulled out and called whenever needed. You have to first declare the class - write out the abstract 
view - before you can create Objects using it. The generic way to declare a class is below. *Note: We introduce a 
new term 'kwargs' which will be explained after.*

```python
# Declare the class with a name
class Car(object):        # Declare a 'class' named 'Car' that is an 'object'
    
    num_of_wheels = "4"   # The number of wheels the car has. All cars have 4 wheels, so this is 
                          # outside of the '__init__()' function because this value never changes.
                           
    def __init__(self, brand, make, year, owner, **kwargs):  # This function is called when you create an object of 
        self.brand = brand                                   # type 'Car'. This creates all your 'descriptions'.
        self.make = make
        self.year = year                         # The four lines right here assign the values passed to the function
        self.owner = owner                       # to the attributes of the object so we can get/set them later.
        
        for k in kwargs.keys():                  # If any other values with keywords are passed, they will be added, 
            self.__setattr__(k, kwargs[k])       # say if we needed ' condition="good" ' to describe the car as well.
    
```
