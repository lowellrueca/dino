# Basic Tutorial for Scripting in Dynamo
A minimal tutorial to get started with the basics of scripting
using Python and DesignScript language

---
## Python Basics
```python
"""
Data Types
"""

# string or str
greet = "hello" 

# integer or int
num1 = 1

# double
num2 = 1.88

# boolean
liar = True
honest = False

# list
data1 = ["object1", "object2" ,"object3"]
data2 = [1, 3, 5]
data3 = ["object1", "object2" ,"object3"]

# getting the individual element from a list
# or known as indexing
d1 = data1[2]
d2 = data2[0]
d3 = data3[1]
# end of data types

# creating function is by using with the def keyword
def func_a():
    """
    A function with no parameter and no return
    Note:
        Print function works only in a separate python file
        not inside Dynamo
    """
    print("hello")

def func_b():
    """
    A function with no parameter which returning a value or an object
    """
    return "hello"

def func_c(param1):
    """
    A function with parameter and returns a value or an object
    """
    return "hello {}".format(param1)

# calling the function
func_a()
result_b = func_b()
result_c = func_c("John Wick")
```
### Utilized Python Advance Features
There are built-in and commonly used function that can be utilized commonly dealing with the list of data, similary for array and iterable type of objects namely
* map(function, iterables)
* filter(function, iterables)

Additionaly there is also a built-in function in python that is commonly used for sorting the data
* sorted(iterable, /, *, key=None, reverse=False)

For the above functions, refer to dino_core module source code how they are utilized
### Commonly used function for getting the object's properties and attributes
* dir()
* object.GetType() in dotnet
### Additional Sources
* https://docs.python.org/3/library/functions.html
* https://www.w3schools.com/python/python_intro.asp

---
## DesignScript Basics
```
/*
    Data Types
/*

// string
greet = "hello";

// integer
num = 1;

// double
num2 = 1.25;

// boolean
liar = true;
honest = false;

// list
// Dynamo 1.3 uses curly brackets to create list
// Dynamo 2.4 uses square brackets to create list
data1 = {"object1", "object2", "object3"};
data2 = {1, 2, 3};
data3 = {true, false, true};

// getting the individual element or item from the list
// or known as indexing
d1 = data1[1];
d2 = data2[0];
d3 = data3[2];
```
### Additional Sources
* https://dynamobim.org/wp-content/links/DesignScriptGuide.pdf

## Tools for Scripting
* VSCode or any code editor
* DotPeek
    - https://www.jetbrains.com/decompiler/download/#section=portable
