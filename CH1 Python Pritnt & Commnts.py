"""
TODO What is Python : 

Python is a high-level, interpreted, general-purpose programming language.

It is known for its simple, easy-to-read syntax and versatility.

Python supports multiple programming paradigms: procedural, object-oriented, and functional.

It is widely used in web development, data science, automation, artificial intelligence, machine learning, and more.

Python code is portable and runs on various platforms (Windows, macOS, Linux).

TODO Feature of Python :
Easy to learn and use: Simple syntax, similar to English.

Interpreted language: No need to compile, runs line by line.

Dynamically typed: No need to declare variable types.

Extensive libraries: Large standard library and many third-party modules.

Community support: Large and active community.

"""
print("Hello world")

"""
The print() Function in Python : The print() function is used to display output on the screen.

It can print strings, numbers, variables, and more.

For eg. 
"""
print("Hello", "world", sep=' ', end='\n')
print("Hello world")                # Prints: Hello world
print("Python", "is", "fun")        # Prints: Python is fun
print(5 + 3)                        # Prints: 8
print("A", "B", sep="-")            # Prints: A-B
print("No newline", end='\n')         # Prints: No newline (no line break)

"""
A module is a file containing Python code (functions, variables, classes) that you can reuse in other programs.

You can create your own modules or use built-in ones.

To use a module, use the import statement.

# For eg.
"""
import math  # Importing the built-in math module

print(math.sqrt(16))  # Output: 4.0

# another Example 

from math import pi

print(pi)  # Output: 3.141592653589793

"""
TODO Python Comments : 

Comments are notes in your code for explanation or documentation.

Python ignores comments when running the code.

Single-line comment: Use # at the start of the line.

Multi-line comment: Use triple quotes (three single quotes - ''' or three double quotes - ""'') usually for docstrings or block comments.

In some code editors (like VS Code), keywords or TODOs (e.g., # TODO:) may be highlighted automatically for your convenience, 

but this is just a feature of the editor, not Python itself.

# TODO: Refactor this function
"""