"""
Module 2 — Lesson 1: Variables & Data Types
Student: [Rivera, Renz Lui B.]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[This topic focuses about teaching how variables work and about their data types]


============================================
KEY VOCABULARY
============================================
- variable:
- data type:
- int:
- float:
- string:
- boolean:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

word = "kahit ano"
num = 123
boolean = 0

print(f"\nThis two are our current variables which are 'wor = {word}' which is a string and 'num = {num}' which is a integer")
print(f"\nHere is the content of our int variable 'num': {num}")
print(f"this is the data type of num: {type(num)}")
print(f"\nHere is the content of our int variable 'num' once it's turned to a float which gives the integer a decimal: {num}")
print(f"this is the data type of float: {type(float(num))}")
print(f"\nHere is the content of our string variable 'word': {word}")
print(f"this is the data type of word: {type(word)}")
print(f"\nHere is the content of our boolean variable 'boolean' when it has no variable: {bool(boolean)}")
print(f"this is the data type of boolean: {type(bool(boolean))}")
print(f"\nAnd lastly, Here is the content of our boolean variable 'boolean' when it has a variable: {bool(boolean + 1)}")
print(f"this is the data type of boolean: {type(bool(boolean))}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[There was no mistakes here so far since all we did was explain how variables work]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
