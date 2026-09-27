"""
Module 2 — Lesson 3: Loops & Lists
Student: [Rivera, Renz Lui B.]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[This is a quick explanation or demo of the for loop, while loop and list where we also used conditions to make the code work]


============================================
KEY VOCABULARY
============================================
- list:
- for loop:
- while loop:
- index:
- iteration:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

while True:
  choice = input("enter 1 to keep going or 0 to stop: ")
  if choice == "1":
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
  elif choice == "0":
     break
  else:
     print("invalid input!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[The mistake i made was the part where i tried stopping the while loop inside the for loop without the if condtional statements]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
